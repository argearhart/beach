# Project Data Dictionary  
## Overview  
This file provides a data dictionary for the datasets used for the project.  

### Beach Nourishment PSDS

- **State:** The state where the beach is located.  
  - Data Type: object  
- **Location:** Specific location or name of the beach.  
  - Data Type: object  
- **Year Completed:** When the nourishment was completed.
  - Data Type: int64
- **Primary Funding Source:** Source of funding for the project.
 - Data Type: object
- **Justification:** Reason for the nourishment project.
  - Data Type: object
- **Length (ft):** Length of the area nourished, in feet.
  - Data Type: int64
- **Volume (CY):** Volume of sand/material used, in cubic yards.
  - Data Type: int64
- **Total Cost:** Cost of the nourishment project.
  - Data Type: int64
- **Year Completed CPI:** Consumer Price Index for the year completed.
  - Data Type: float64
- **Adjusted Cost (2022):** Cost adjusted to 2022 dollars.
  - Data Type: float64
- **Total Cost/CY:** Cost per cubic yard.
  - Data Type: float64
- **Adjusted Cost/CY:** Cost per cubic yard, adjusted to 2022 dollars.
  - Data Type: float64
- **CY/Foot:** Cubic yards used per foot of beach.
  - Data Type: float64
- **Current CPI:** Most recent Consumer Price Index value.
  - Data Type: float64

### US Stations Linear Sea Level Trends
- **Station ID:** Unique identifier for the measurement station.
  - Data Type: int64 
- **Station Name:** Name of the station (split into City and State for clarity).

- **First Year - Last Year:** Range of years for which data is available.
  - Data Type: int64 
- **Year Range:** Specific years covered.
  - Data Type: int64 
- **Percent Complete:** Completeness of the data.
  - Data Type: int64 
- **MSL Trends mm per yr:** Mean sea level trend in millimeters per year.
  - Data Type: float64 
- **plus minus CI mm yr:** Confidence interval for the mean sea level trend.
  - Data Type: float64 
- **MSL Trend ft per century:** Mean sea level trend in feet per century.
  - Data Type: float64 
- **95 CI ft century:** 95% confidence interval for the trend per century.
  - Data Type: float64 
- **Latitude - Longitude:** Geographic coordinates of the station.
  - Data Type: float64 
- **City:** 
  - Data Type: object  
- **State:** 
  - Data Type: object
- **Region:**
  - Data Type: object
- **Overall Change mm:**  
  - Data Type: float64
  
### Global Mean Sea Level
- **Time:** Timestamp of the measurement.
- **GMSL:** Global mean sea level.
- **GMSL uncertainty:** Uncertainty in the global mean sea level measurement.
- **year:** Extracted year from the Time column.

### Climate Change
- **Date:** Date of the observation.
- **Location:** Location of the observation.
- **Country:** Country of the observation.
- **Temperature:** Temperature measurement.
- **CO2 Emissions:** Volume of CO2 emissions.
- **Sea Level Rise:** Amount of sea level rise observed.
- **Precipitation:** Amount of precipitation.
- **Humidity:** Humidity level.
- **Wind Speed:** Speed of the wind.
- **Year:** Year of the observation extracted from the Date.

### Disasters
Detailed information about natural disasters including year, type, location, damages, and impacts.