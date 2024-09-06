import mortgage
import pandas as pd

# The realestate package has one class "SeattleRealEstate" that contains
# proprerties and methods to calculate real estate metrics.
#
# SeattleRealEstate Class
#
# Variables:
# + mortgage_rate               the APR to be used in mortgage calculations
# + management_fee              the % of short term rental revenue charged as a fee by property management companies
# + downpayment                 the % of the purchase price required for a short term rental downpayment
# + loan_term                   the length of the loan for a short term rental mortgage
#
# Methods:
# + lookup_neighorhood()        find the MLS neighborhood given an airbnb neighborhood
# + calculate_noi()             calculate the net operating income of a listing
# + calculate_rpp()             calculate the revenue per property of a listing
# + calculate_downpayment()     calculate the downpayment needed for a listing
# + calculate_home_price()      calculate the home sale price for a listing
 
class SeattleRealEstate:

    def __init__(self, mortgage_rate : float = 0.075, 
                management_fee : float = 0.1,
                downpayment : float = 0.25,
                loan_term : int = 30):
        # set the default values for all variables
        self.mortgage_rate = mortgage_rate
        self.management_fee = management_fee
        self.downpayment = downpayment
        self.loan_term = loan_term


    def lookup_neighorhood(self, airbnb_neighborhood:str) -> str :
        """Returns the corresponding Seattle Real Estate Neighborhood given an 
        AirBnB Neighborhood
        @param airbnb_neighborhood - the neighborhood to look up
        @return - the Seattle real estate neighborhood 
        """
        # There is a 1 to Many relationship between the Real Estate Neighborhood
        # and the AirBnB neighborhood
        #
        # Real Estate Neighborhood = AirBnB Neighborhood(s)
        #
        # Ballard/Greenlake	= Ballard
        # Belltown/Downtown	= Downtown, Cascade, Capitol Hill
        # Central Seattle	= Central Area
        # East Side–South of I-90	= Rainier Valley
        # North Seattle	= Northgate, Lake City, University District
        # Queen Anne/Magnolia	= Queen Anne, Magnolia, Interbay
        # SODO/Beacon Hill	= Beacon Hill
        # Southeast Seattle	= Seward Park
        # West Seattle	= Delridge, West Seattle
        neighborhood_mapping = {
            "Ballard" : "Ballard/Greenlake",
            "Downtown" : "Belltown/Downtown",
            "Cascade" : "Belltown/Downtown",
            "Capitol Hill" : "Belltown/Downtown",
            "Central Area" : "Central Seattle",
            "Rainier Valley" : "East Side–South of I-90",
            "Northgate" : "North Seattle",
            "Lake City" : "North Seattle",
            "University District" : "North Seattle",
            "Queen Anne" : "Queen Anne/Magnolia",
            "Magnolia" : "Queen Anne/Magnolia",
            "Interbay" : "Queen Anne/Magnolia",
            "Beacon Hill": "SODO/Beacon Hill",
            "Seward Park" : "Southeast Seattle",
            "Delridge" : "West Seattle",
            "West Seattle" : "West Seattle"
            }
        
        if airbnb_neighborhood in neighborhood_mapping:
            return neighborhood_mapping[airbnb_neighborhood]
        else:
            return "Other"


    def calculate_noi(self, nightly_rate : float, days_occupied : int, house_price : int) -> float :
        """
        returns the net operating income of a property
        param: nightly rate
        param: days_occupied
        param: house price
        return: net operating income
        """
        # Step 1) calculate the loan amount (price - downpayment)
        loan_amount = house_price - self.calculate_downpayment(house_price)

        # Step 2) use the mortgage package to create a loan object
        loan = mortgage.Loan(loan_amount, self.mortgage_rate, self.loan_term)

        # Step 3) use the loan object to get the monthly payment
        mortgage_expense = float(loan.monthly_payment)

        # Step 4) calculate the revenue per property
        monthly_revenue = self.calculate_rpp(nightly_rate, days_occupied)

        # Step 5) calculate the management expense
        management_expense = float(monthly_revenue * self.management_fee)

        # Step 6) return the net operating income
        return round(monthly_revenue - mortgage_expense - management_expense, 2)
    

    def calculate_rpp(self, nightly_rate : float, days_occupied : int) -> float :
        """
        returns the revenue per property
        param: nightly rate
        param: days_occupied
        return: revenue per property
        """
        return nightly_rate * days_occupied


    def calculate_downpayment(self, home_price) -> float :
        """
        returns the downpayment amount in dollars
        param: home_price
        return: downpayment amount
        """
        return home_price * self.downpayment

    
    def calculate_home_price(self, neighborhood : str, beds : float, market : pd.DataFrame) -> float :
        """
        returns the home price in dollars based on the neighborhood and number
        of bedrooms
        param: neighborhood
        param: beds - number of bedrooms
        return: home price in dollars
        """
        # market data looks like:
        #
        # neighborhood, median_price, one_br, two_br, three_br, four_br, five_plus_br
        # North Seattle,800000,488249,647482,800000,1008992,1125899 
        # Queen Anne/Magnolia,895000,546229,724370,895000,1128810,1259599
        #
        # use the neighborhood to find the correct row in the market data
        # use the # bedrooms to find the correct column in the market data
        if beds <= 1:
            return market.loc[neighborhood, "one_br"]
        elif beds == 2:
            return market.loc[neighborhood, "two_br"]
        elif beds == 3:
            return market.loc[neighborhood, "three_br"]
        elif beds == 4:
            return market.loc[neighborhood, "four_br"]
        elif beds >= 5:
            return market.loc[neighborhood, "five_plus_br"]
        else:
            return 
