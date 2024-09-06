import mortgage
import pandas as pd

class SeattleRealEstate:

    def __init__(self, mortgage_rate : float = 0.075, 
                management_fee : float = 0.1,
                downpayment : float = 0.25,
                loan_term : int = 30):
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
        loan_amount = house_price - self.calculate_downpayment(house_price)
        loan = mortgage.Loan(loan_amount, self.mortgage_rate, self.loan_term)
        mortgage_expense = float(loan.monthly_payment)

        monthly_revenue = self.calculate_rpp(nightly_rate, days_occupied)

        management_expense = float(monthly_revenue * self.management_fee)

        return round(monthly_revenue - mortgage_expense - management_expense,2)
    

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

    
    def calculate_home_price(self, neighborhood, beds, market : pd.DataFrame) -> float :
        """
        returns the home price in dollars based on the neighborhood and number
        of bedrooms
        param: neighborhood
        param: beds - number of bedrooms
        return: home price in dollars
        """
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
            return 0
