# Analysis of sea level trends, storm data, and beach renourishment projects

## Introduction

After watching a beach renourishment project take place, I began to wonder how effective these efforts are in light of rising sea levels, increasing storms, and other climate factors.  My focus for this project is to demonstrate the skills I have gained in the CodeU Data Analytics program.  During the time period of the class, a winter storm washed away 14,000 tons of sand that had been trucked in to the beach at Salisbury, MA [article](https://apnews.com/article/salisbury-massachusetts-beach-dunes-washed-away-cb64913e5592979aacb230c5f318efee).  Originally, I thought to attempt to develop a predictive model about how long it would take for sea levels to reclaim an area that had a project like these.  Given how one storm washed away the completed beach project in one weekend, future analysis could explore economic factors to determine the benefits of these projects. 

 *** 
## **_Currently, this project will only work on Windows_**

## Project Overview

The project aims to analyze sea level trends, storm data, and beach renourishment projects.  The primary objective is to identify factors that impact beach renourishment projects on US beaches in the Gulf of Mexico. 

## Features
1. Loading data: Read two data files (xlsx, csv)  
2. Clean and operate on the data while combining them.    
  * Clean data and perform pandas merge with two data sets, calculate some new values  
3. Visualize / Present   
  * Utilized Plotly, Matplotlib and Seaborn throughout to create visualizations.  *images are saved in the images folder*  
  * Tableau [dashboard](https://public.tableau.com/views/BeachAnalysisProject/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link)   *in progress*    
4. Best practices
  * Utilized virtual environment and instructions in readme  
  * Custom data dictionary 
5. Interpretation of data
  * Code annotated with markdown cells, code comments, README.me file
  * Annotated .py files  

## Technical Insight:
- **Programming Environment:** Utilization of Jupyter Notebooks within Visual Studio Code for code development and documentation.
- **Python Libraries:**
    - Pandas for data manipulation and analysis.
    - NumPy for numerical data processing.
    - Matplotlib and Seaborn for data visualization.
    - Ploytly for data visualization
- **Data Cleaning:** Standardize column names, data types (date/time), identify outliers, and other info.
- **Data Integration:** Merge/concatenate multiple data sources.
- **Summary/Statistics:** Calculate descriptive statistics to understand the relationship of data by locations, dates, natural disasters, etc. 
- **Data Visualization:** Utilize libraries such as Matplotlib, Seaborn, and Plotly to create visualizations for exploring patterns, trends, and presenting.
- **Documentation:** Document the analysis process, including data preprocessing steps, exploratory data analysis, and insights gained.
- **Reporting:** Prepare a report/presentation summarizing key findings, insights, and visual outputs from the analysis.

 *** 
  
## Gathering the Data
The data used for the project includes the following:  

| Data Set | Description |
| ----- | -----|   
| [Beach Nourishment Master Database from the Program for the Study of Developed Shorelines](https://beachnourishment.wcu.edu/glossary) | Under the constant revision, the PSDS beach nourishment database contains attribute information on the general location of sand placement, primary funding source and funding type, the volume of sediment emplacement (in cubic yards), length of beach nourished (in feet) and cost. |   
| [All Natural Disasters 1900-2021/EOSDIS](https://www.kaggle.com/datasets/brsdincer/all-natural-disasters-19002021-eosdis) | In this dataset, you will see the natural disasters of all countries. |   
| [U.S. Linear Relative Sea Level (RSL) trends and 95% Confidence Intervals (CI) in mm/year and in ft/century](https://tidesandcurrents.noaa.gov/sltrends/mslUSTrendsTable.html) | The rate of mean sea level rise or fall has been determined for 117 long-term water level stations. |
|*Not currently included in this project analysis* |   
| [Climate Insights Dataset](https://www.kaggle.com/datasets/goyaladi/climate-insights-dataset) |  This dataset provides valuable insights into the ongoing changes in our climate. It encompasses a comprehensive collection of temperature records, CO2 emissions data, and sea level rise measurements |   
| [Global Average Absolute Sea Level Change](https://www.kaggle.com/datasets/somesh24/sea-level-change) | Cumulative changes in sea level for the world’s oceans since 1880, based on a combination of long-term tide gauge measurements and recent satellite measurements. | 

Access Requirements: No special access requirements.  


*** 

### Installation  
#### How to Run the Project   
**Before you begin, ensure you have met the following requirements:**    
You have installed Python. This project was developed using Python 3.12.0. If you don't have Python installed or if you need to upgrade your current version, you can download it from the [official Python website](https://www.python.org/downloads/).  

You have installed Git, which is necessary to clone the repository. If you don't have Git installed, you can download it from the [Git](https://git-scm.com/downloads).  

**Follow these steps to run the project on your local machine:**  
#### Clone the repository  
1. Fork the [repository]( https://github.com/argearhart/beach/)  
2. Clone the repository to your Github account  
3. Access the repository from your command line or preferred CMD software  
4. Install a virtual environment.   

*It's recommended to create a virtual environment to keep the project's dependencies isolated from your system's Python environment. You can create a virtual environment using the following command:*  

On Windows:  python -m venv venv  
On macOS and Linux: python3 -m venv venv  
This will create a new virtual environment named venv in your current directory.  

#### Activate the virtual environment using the following command:   

On Windows:   

```python
.\venv\Scripts\activate
```

On macOS and Linux:   

```python
source venv/bin/activate
```
  
*Your prompt should change to indicate that you are now operating within a Python virtual environment.*  

#### Install the required packages by running the following command:  

```python
pip install -r requirements.txt
```
  
You are now ready to run the project!   

#### Run the .ipynb file:
If you have Jupyter Notebook installed, enter jupyter notebook and open the .ipynb file.  

If you are using Visual Studio Code, open the .ipynb file and run the cells using the run button that appears at the top left of each cell.  

To deactivate the virtual environment when you are done, simply type deactivate in your terminal.  

---
### Project Notebooks
Run the project notebooks from 01 to 05.  The notebook 05main utilizes files created in 01 through 04.  

Notebook 06 sea levels looks at global mean sea levels.  In the future, we may look at more global data.    
