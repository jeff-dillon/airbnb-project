import logging
import os
import pandas as pd
from realestate import SeattleRealEstate

def main():
    # start the logging
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info("start cleaning process")

    # change the working directory to src/ directory so the relative paths will work
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # clean the airbnb listing data
    logging.info("clean the airbnb listing data")
    listings = pd.read_excel("../data/raw/Tableau Full Project.xlsx", sheet_name=0)

    # clean the housing cost data
    logging.info("clean the housing cost data")
    cost_by_neighborhood = pd.read_csv("../data/raw/Home_Cost_By_Neighborhood.csv")
    cost_by_bedrooms = pd.read_csv("../data/raw/Home_Cost_by_Bedrooms.csv")

    logging.info("end cleaning process")

if __name__ == "__main__":
    main()
