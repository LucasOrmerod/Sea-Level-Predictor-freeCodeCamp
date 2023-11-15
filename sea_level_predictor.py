import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("./epa-sea-level.csv")

    years = df["Year"]
    sea_level = df["CSIRO Adjusted Sea Level"]
  
    # Create scatter plot
    plt.scatter(years, sea_level)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(years, sea_level)
    earliest_year = df["Year"].min()
    latest_year = 2051
    lobf_data = {
      "Year": [],
      "CSIRO Adjusted Sea Level": []
    }
    for year in range (earliest_year, latest_year):
      lobf_data["Year"] = [year for year in range (earliest_year, latest_year)]
      lobf_data["CSIRO Adjusted Sea Level"] = [slope * year + intercept for year in range(earliest_year, latest_year)]

    plt.plot(lobf_data["Year"], lobf_data["CSIRO Adjusted Sea Level"], color="red")

    # Create second line of best fit
    lobf_data2 = {
      "Year": [],
      "CSIRO Adjusted Sea Level": []
    }
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df.loc[df["Year"] >= 2000]["Year"], df.loc[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"])
    for year in range (2000, 2051):
      lobf_data2["Year"] = [year for year in range(2000, 2051)]
      lobf_data2["CSIRO Adjusted Sea Level"] = [slope2 * year + intercept2 for year in range(2000, 2051)]
      plt.plot(lobf_data2["Year"], lobf_data2["CSIRO Adjusted Sea Level"], color="blue")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()