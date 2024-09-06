import logging
import os
import pandas as pd
from realestate import SeattleRealEstate

# Automated cleaning script
# This file reads in raw data filese, performs cleaning steps, and writes out
# clean data files that can be used for analysis.

def clean_market_data(neighborhood : pd.DataFrame, beds :  pd.DataFrame) -> pd.DataFrame:
    """
    This function contains all of the cleaning steps for the seatlle real estate
    market data.
    param: neighborhood - raw DataFrame of housing cost by neighborhood
    param: beds - raw DataFrame of housing cost by # of bedrooms
    return: Clean DataFrame of housing cost by neighborhood and # bedrooms
    """

    # This function cleans the seattle housing market data
    # It takes in two raw data frames (cost by bedrooms, cost by nieghborhood)
    # and returns a single, clean, data frame.
    #
    # Cleaning steps:
    # 1) remove unneeded columns
    # 2) rename the columns
    # 3) change price columns from string to int
    # 4) calculate the % change in price by # of bedrooms
    # 5) calculate the price by bedrooms for each neighborhood
    # 6) remove records for neighborhoods we don't need
    # 7) return a clean dataframe

    # 1) remove unneeded columns
    logging.debug(" - filter the bedrooms columns")
    beds = beds[["Bedrooms", "Median Sale Price"]]

    logging.debug(" - filter the neighborhood columns")
    market = neighborhood[["Map Area","Median Price, 2020"]]

    # 2) rename the columns
    logging.debug(" - rename the bedrooms columns")
    beds = beds.rename(columns={"Bedrooms":"bedrooms",
                                "Median Sale Price":"median_price"})
    
    logging.debug(" - rename the neighborhood columns")
    market = market.rename(columns={"Map Area" : "neighborhood", 
                                    "Median Price, 2020" : "median_price"})

    # 3) change price columns from string to int
    logging.debug(" - change the type of the bedrooms median_price column to int")
    beds["median_price"] = beds["median_price"].str.replace("$","")
    beds["median_price"] = beds["median_price"].str.replace(",","")
    beds["median_price"] = beds["median_price"].astype('int')

    logging.debug(" - change the type of the neighborhood median price column to int")
    market["median_price"] = market["median_price"].str.replace("$","")
    market["median_price"] = market["median_price"].str.replace(",","")
    market["median_price"] = market["median_price"].astype('int')

    # 4) calculate the % change in price by # of bedrooms
    logging.debug(" - calculate the bedroom adjustments")
    price_basis = beds.loc[beds["bedrooms"] == "3"]["median_price"].values[0]
    beds["adjustment"] = (beds["median_price"]/price_basis)

    
    # 5) calculate the price by bedrooms for each neighborhood
    logging.debug(" - add the bedroom columns")
    def adjust_br(row, br):
        return row["median_price"] * beds["adjustment"].loc[beds["bedrooms"] == br]
    
    market["one_br"] = market.apply(adjust_br, br="1", axis=1).astype('int')
    market["two_br"] = market.apply(adjust_br, br="2", axis=1).astype('int')
    market["three_br"] = market.apply(adjust_br, br="3", axis=1).astype('int')
    market["four_br"] = market.apply(adjust_br, br="4", axis=1).astype('int')
    market["five_plus_br"] = market.apply(adjust_br, br="5 or more", axis=1).astype('int')

    # 6) remove records for neighborhoods we don't need
    logging.debug(" - filter out the neighborhood rows we don't need")
    market = market.loc[market["neighborhood"].isin(["Belltown/Downtown",
                                                    "Ballard/Greenlake",
                                                    "East Side–South of I-90",
                                                    "North Seattle",
                                                    "Queen Anne/Magnolia",
                                                    "SODO/Beacon Hill",
                                                    "Southeast Seattle",
                                                    "West Seattle", 
                                                    "Central Seattle"])]
    
    market = market.set_index('neighborhood')
    
    # 7) return a clean dataframe
    return market


def clean_listing_data(listings : pd.DataFrame, market : pd.DataFrame) -> pd.DataFrame:
    """
    This function contains all of the cleaning steps for the airbnb listings data.
    param: listings - raw DataFrame of airbnb listings
    param: market - clean DataFrame of housing cost by neighborhood and # bedrooms
    return: Clean DataFrame of airbnb listings augmented with housing cost data
    """

    # This function cleans the airbnb listings data.
    # it takes in the raw listings data and the clean housing market data and
    # returns a clean listings data frame.
    #
    # Cleaning steps:
    # 1) drop the columns we don't need
    # 2) filter our the rows we don't need (property_type, room_type, bedrooms)
    # 3) create new fields (days_occupied, rpp, re_neighborhood, re_home_price, noi)
    # 4) return the clean listings data

    # 1) drop the columns we don't need
    logging.debug("- filter our the columns we don't need")
    listings = listings[["id", "name", "neighbourhood_group_cleansed", 
                      "property_type", "room_type", "bedrooms","price", 
                      "availability_30" ]]
    
    # 2) filter our the rows we don't need (property_type, room_type, bedrooms)
    logging.debug("- filter out the property types we don't need")
    listings = listings.loc[listings["property_type"].isin(['Apartment', 'House', 
                                                   'Cabin', 'Condominium'])]
    
    logging.debug("- filter out the room_types we don't need")
    listings = listings.loc[listings["room_type"] == "Entire home/apt"]

    logging.debug("- filter our the listings that have 0 bedrooms")
    listings = listings.loc[listings["bedrooms"] >= 1]

    # 3) create new fields (days_occupied, rpp, re_neighborhood, re_home_price, noi)
    logging.debug("- create a new field that has the number of days the listing is occupied in a month")
    listings["days_occupied"] = listings.apply(lambda x: 30 - x.availability_30, axis=1)

    logging.debug("- create a new field for the Revenue Per Property (RPP)")
    sre = SeattleRealEstate()
    listings["rpp"] = listings.apply(lambda x: 
                                     sre.calculate_rpp(x.price, x.days_occupied), axis=1)

    logging.debug("- create the re_neighborhood field")
    listings["re_neighborhood"] = listings.apply(lambda x: 
                                                 sre.lookup_neighorhood(x.neighbourhood_group_cleansed), axis=1)
    logging.debug("- filter out 'Other' neighborhoods")
    listings = listings.loc[listings["re_neighborhood"] != "Other"]

    logging.debug("- create the re_home_price field")
    listings["re_home_price"] = listings.apply(lambda x: 
                                               sre.calculate_home_price(x.re_neighborhood, 
                                                                        x.bedrooms, market), axis=1)

    logging.debug("- create the noi field")
    listings["noi"] = listings.apply(lambda x: 
                                     sre.calculate_noi(x.price, 
                                                       x.days_occupied, 
                                                       x.re_home_price), axis=1)
    
    
    # 4) return the clean listings data
    return listings


def main():
    # The main() function has the main flow for the cleaning script

    # Step 1) First we set up logging so that we can see the progress of the script
    #           while it is running
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.info("start cleaning process")

    # Step 2) Next we make sure that the script is set to run from the correct directory
    #           This is needed to ensure the relative paths will work as expected.
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Step 3) Now we clean the housing cost data and write the clean data out to a new file.
    logging.info("clean the housing cost data")
    cost_by_neighborhood = pd.read_csv("../data/raw/Home_Cost_By_Neighborhood.csv")
    cost_by_bedrooms = pd.read_csv("../data/raw/Home_Cost_by_Bedrooms.csv")
    seattle_housing_market = clean_market_data(cost_by_neighborhood, cost_by_bedrooms)
    seattle_housing_market.to_csv("../data/clean/seattle_housing_market_data.csv")

    # Step 4) Finally we clean the airbnb listing data and write the clean data out to a new file.
    logging.info("clean the airbnb listing data")
    listings = pd.read_excel("../data/raw/Tableau Full Project.xlsx", sheet_name=0)
    clean_listings = clean_listing_data(listings, seattle_housing_market)
    clean_listings.to_csv("../data/clean/seattle_airbnb_listings.csv", index=False)

    logging.info("end cleaning process")


if __name__ == "__main__":
    main()
