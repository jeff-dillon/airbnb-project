# Airbnb Data Analysis

This is a capstone project for the Code:You Data Analysis course. This project 
will analyze Airbnb data to uncover useful correlations/trends and guide 
decision making in investing in STR properties.

**Goal:**
Determine the optimal neighborhood / size / price for investment.

Steps:
1. List (or research) key metrics for Short Term Rentals.
2. Determine data needed to support.
3. Review available data.
4. Identify the type of analysis that can be done and list the questions that can be answered.
5. Clean the data.
6. Analyze the data and answer the questions.
7. Visualize the analysis.

## Getting Started

1. Clone this repo.
2. Create a virtual environment and install the packages listed in the `requirements.txt` file.
3. Open the `src/01_discover.ipynb` file to view the raw data.
4. Run the `src/02_clean.py` script to clean the raw data.
5. Run the `src/03_analyze.ipynb` file to view the analysis.



## Capstone Project Criteria

1. This README file provides information about the project and how to use the code.
2. `data/README.md` provides data dictionary for the data used in the project.
3. `src/01_discover.ipynb` is a jupyter notebook using pandas to understand the raw data files.
4. `src/02_clean.py` use pandas to clean a dataset
5. `src/realestate.py` create custom classes and methods
6. `src/03_analyze.ipynb` use pandas to aggregate and plot the data

## Project Layout

At a high level, all data is stored in the `data/` directory and all python code is stored in the `src/` directory.

| File | Description |
| ---- | ----------- |
| `README.md` | general information about the project |
| `data/raw` | raw data files |
| `data/clean` | cleaned data files |
| `data/README.md` | Data dictionary for the raw data used in the project. |
| `src/01_discover.ipynb` | Jupyter notebook for data discovery. This notebook shows the thought process for the analysis. Includes research on the project topic, identification of data needed, identification of cleaning needed. |
| `src/02_clean.py` | Automated the data cleaning script. This script takes in the raw data files and performs cleaning including removing unnecessary columns, renaming columns, removing unnecessary rows, adding calculated fields, etc. |
| `src/03_analyze.ipynb` | Jupyter notebook for data analysis. Aggregates and plots the data to answer the project questions. |
| `src/realestate.py` | This is a custom python module with real estate properties and methods. This is where we define some of the values that are used in real estate calculations like mortgage interest rate, mortgage term, downpayment %, and short term rental management fee. This is also where we keep some of the logic for calculating real-estate specific fields like monthly mortgage rate, revenue per property, and net operating income. |