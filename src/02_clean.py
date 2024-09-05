import logging
import os
import pandas as pd
from realestate import SeattleRealEstate

def clean_market_data(neighborhood, beds):
    logging.info(" - filter the bedrooms columns")
    beds = beds[["Bedrooms", "Median Sale Price"]]

    logging.info(" - rename the bedrooms columns")
    beds = beds.rename(columns={"Bedrooms":"bedrooms",
                                "Median Sale Price":"median_price"})

    # change the type of the median_price column to int
    logging.info(" - change the type of the bedrooms median_price column to int")
    beds["median_price"] = beds["median_price"].str.replace("$","")
    beds["median_price"] = beds["median_price"].str.replace(",","")
    beds["median_price"] = beds["median_price"].astype('int')

    # calculate the adjustment %
    logging.info(" - calculate the bedroom adjustments")
    price_basis = beds.loc[beds["bedrooms"] == "3"]["median_price"].values[0]
    beds["adjustment"] = (beds["median_price"]/price_basis)

    # select just the columns we are interested in
    logging.info(" - filter the neighborhood columns")
    market = neighborhood[["Map Area","Median Price, 2020"]]
    
    # change the type of the median price column to int
    logging.info(" - change the type of the neighborhood median price column to int")
    market["Median Price, 2020"] = market["Median Price, 2020"].str.replace("$","")
    market["Median Price, 2020"] = market["Median Price, 2020"].str.replace(",","")
    market["Median Price, 2020"] = market["Median Price, 2020"].astype('int')

    # rename the columns
    logging.info(" - rename the columns")
    market = market.rename(columns={"Map Area" : "neighborhood", 
                                    "Median Price, 2020" : "median_price"})

    # add the bedroom columns
    logging.info(" - add the bedroom columns")
    def adjust_br(row, br):
        return row["median_price"] * beds["adjustment"].loc[beds["bedrooms"] == br]
    
    market["one_br"] = market.apply(adjust_br, br="1", axis=1).astype('int')
    market["two_br"] = market.apply(adjust_br, br="2", axis=1).astype('int')
    market["three_br"] = market.apply(adjust_br, br="3", axis=1).astype('int')
    market["four_br"] = market.apply(adjust_br, br="4", axis=1).astype('int')
    market["five_plus_br"] = market.apply(adjust_br, br="5 or more", axis=1).astype('int')

    # filter out the rows we don't need
    logging.info(" - filter out the neighborhood rows we don't need")
    market = market.loc[market["neighborhood"].isin(["Belltown/Downtown",
                                                    "Ballard/Greenlake",
                                                    "East Side–South of I-90",
                                                    "North Seattle",
                                                    "Queen Anne/Magnolia",
                                                    "SODO/Beacon Hill",
                                                    "Southeast Seattle",
                                                    "West Seattle", 
                                                    "Central Seattle"])]
    
    return market


def clean_listing_data(listings):

    logging.info("- filter our the columns we don't need")
    clean = listings[["id", "name", "neighbourhood_group_cleansed", 
                      "property_type", "room_type", "bedrooms","price", 
                      "availability_30" ]]
    
    logging.info("- filter our the rows we don't need")
    clean = clean.loc[clean["property_type"].isin(['Apartment', 'House', 
                                                   'Cabin', 'Condominium'])]
    
    clean = clean.loc[clean["room_type"] == "Entire home/apt"]

    logging.info("- create the RPP field")
    clean["rpp"] = clean["price"] * clean["availability_30"]

    return clean

def main():
    # start the logging
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info("start cleaning process")

    # change the working directory to src/ directory so the relative paths will work
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # clean the housing cost data
    logging.info("clean the housing cost data")
    cost_by_neighborhood = pd.read_csv("../data/raw/Home_Cost_By_Neighborhood.csv")
    cost_by_bedrooms = pd.read_csv("../data/raw/Home_Cost_by_Bedrooms.csv")
    seattle_housing_market = clean_market_data(cost_by_neighborhood, cost_by_bedrooms)
    seattle_housing_market.to_csv("../data/clean/seattle_housing_market_data.csv", index=False)

    # clean the airbnb listing data
    logging.info("clean the airbnb listing data")
    listings = pd.read_excel("../data/raw/Tableau Full Project.xlsx", sheet_name=0)
    clean_listings = clean_listing_data(listings)
    clean_listings.to_csv("../data/clean/seattle_airbnb_listings.csv", index=False)

    # sre = SeattleRealEstate()

    logging.info("end cleaning process")

if __name__ == "__main__":
    main()
