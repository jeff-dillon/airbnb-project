import mortgage

class SeattleRealEstate:

    loan_term = 30              # 30 year loan term
    downpayment = 0.25          # 25% downpayment for investment property

    def __init__(self, mortgage_rate : float = 0.075, management_fee : float = 0.1):
        self.mortgage_rate = mortgage_rate
        self.management_fee = management_fee

    def lookup_neighorhood(airbnb_neighborhood:str) -> str :
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
        return neighborhood_mapping[airbnb_neighborhood]
    

    def calculate_noi(self, nightly_rate : float, days_occupied : int, house_price : int) -> float :
        """
        returns the net operating income of a property
        param: nightly rate
        param: days_occupied
        param: house price
        return: net operating income
        """
        loan_amount = house_price * (1 - self.downpayment)
        loan = mortgage.Loan(loan_amount, self.mortgage_rate, self.loan_term)
        mortgage_expense = loan.monthly_payment

        monthly_revenue = self.calculate_rpp(nightly_rate, days_occupied)

        management_expense = monthly_revenue * self.management_fee

        return monthly_revenue - mortgage_expense - management_expense
    

    def calculate_rpp(nightly_rate : float, days_occupied : int) -> float :
        """
        returns the revenue per property
        param: nightly rate
        param: days_occupied
        return: revenue per property
        """
        return nightly_rate * days_occupied