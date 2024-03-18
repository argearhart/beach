# Analysis of sea level trends, storm data, climate change, and the impacts of beach renourishment projects

## Introduction
After watching a beach renourishment project take place, I began to wonder how effective these efforts are in light of rising sea levels, increasing storms, and other climate factors.  My focus for this project is to demonstrate the skills I have gained in the CodeU Data Analytics program.  During the time period of the class, a winter storm washed away 14,000 tons of sand that had been trucked in to the beach at Salisbury, MA [article](https://apnews.com/article/salisbury-massachusetts-beach-dunes-washed-away-cb64913e5592979aacb230c5f318efee).  Originally, I thought to attempt to develop a predictive model about how long it would take for sea levels to reclaim an area that had a project like these.  Given how quickly one storm washed away the beach in this instance, I believe a meaningful predictive model would be extremely difficult to develop if not close to impossible. 

## Project Overview
The project aims to analyze sea level trends, storm data, and climate change indicators.  The primary objective is to look at the effects of various environmental, geographical, climate factors that impact beach renourishment projects on US beaches in the Gulf of Mexico. 


### Features
1. Read two data files (xlsx, csv)
2. Clean data and perform pandas merge with two data sets
3. Matplotlib and seaborn visualizations
4. Tableau dashboard
5. Virtual environment and instructions in readme
6. Use markdown cells, clear code comments, README.me file

## 
---
### Installation

**Before you begin, ensure you have met the following requirements:**
You have installed Python. This project was developed using Python 3.12.0. If you don't have Python installed or if you need to upgrade your current version, you can download it from the [official Python website](https://www.python.org/downloads/).

You have installed Git, which is necessary to clone the repository. If you don't have Git installed, you can download it from the [official Git website](https://git-scm.com/downloads).

**Follow these steps to run the project on your local machine:**
### Clone the repository
1. Open a terminal/Command Prompt.
    - On Windows, you can use Command Prompt or PowerShell.
    - On Unix-based systems (Linux, macOS), use the terminal. 

2. Navigate to the directory where you want the cloned repository to be placed by using the cd command in your terminal followed by the path of the directory.

Then you can clone this repository by running the following command in your terminal:

Navigate to the cloned directory

Change your current directory to the cloned repository's directory:

Set up a virtual environment

It's recommended to create a virtual environment to keep the project's dependencies isolated from your system's Python environment. You can create a virtual environment using the following command:

On Windows:  python -m venv venv
On macOS and Linux: python3 -m venv venv
This will create a new virtual environment named venv in your current directory.

Activate the virtual environment

Activate the virtual environment using the following command:

On Windows:  

```python
.\venv\Scripts\activate
```

On macOS and Linux: 

```source venv/bin/activate```

Your prompt should change to indicate that you are now operating within a Python virtual environment.

Install the required packages

Install the required packages by running the following command:

```pip install -r requirements.txt```

You're now ready to run the project!

Run the .ipynb file:

If you have Jupyter Notebook installed, enter jupyter notebook and open the .ipynb file.
If you are using Visual Studio Code, open the .ipynb file and run the cells using the run button that appears at the top left of each cell.
To deactivate the virtual environment when you're done, simply type deactivate in your terminal.



