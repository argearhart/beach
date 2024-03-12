# Beach
# Installation
**Before you begin, ensure you have met the following requirements:**
You have installed Python. This project was developed using Python 3.12.0. If you don't have Python installed or if you need to upgrade your current version, you can download it from the official Python website.

You have installed Git, which is necessary to clone the repository. If you don't have Git installed, you can download it from the official Git website.

**Follow these steps to run the project on your local machine:**
#Clone the repository

Navigate to the directory where you want the cloned repository to be placed by using the cd command in your terminal followed by the path of the directory.

Then you can clone this repository by running the following command in your terminal:

Navigate to the cloned directory

Change your current directory to the cloned repository's directory:

Set up a virtual environment

It's recommended to create a virtual environment to keep the project's dependencies isolated from your system's Python environment. You can create a virtual environment using the following command:

On Windows:

python -m venv venv
On macOS and Linux:

python3 -m venv venv
This will create a new virtual environment named venv in your current directory.

Activate the virtual environment

Activate the virtual environment using the following command:

On Windows:

.\venv\Scripts\activate
On macOS and Linux:

source venv/bin/activate
Your prompt should change to indicate that you are now operating within a Python virtual environment.

Install the required packages

Install the required packages by running the following command:

pip install -r requirements.txt
You're now ready to run the project!

Run the .ipynb file:

If you have Jupyter Notebook installed, enter jupyter notebook and open the .ipynb file.
If you are using Visual Studio Code, open the .ipynb file and run the cells using the run button that appears at the top left of each cell.
To deactivate the virtual environment when you're done, simply type deactivate in your terminal.
