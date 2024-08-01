# Automated Makerspace Tour - Quickstart Quide

This is a project aimed to automate the makerspace tour when Jake is not in the office. 
The aim is to use speech recognition and basic http requests to communicate with the TonyPI robot.

## Getting Started

These instructions will help you set up the project on your local machine.

### Prerequisites

Make sure you have Python 3+ installed. You can download it from [python.org](https://www.python.org/downloads/). Or request access lol.

### Cloning the Repository



     git clone https://github.com/oneteamAvery/makerspace_tour.git


## Setting up virtual environment
1. **Create the environment**

Navigate to the project directory and run the following command to create a virtual environment. You can name it venv or choose a different name.

   
    python -m venv venv


2. **Activate the virtual environment**
   - Windows
     ```sh
     source venv\Scripts\activate
   - Mac & Linux
     ```sh
     source venv/bin/activate
     
After activation you should see `(venv)` or what ever name you set your virtual enviornment in your terminal prompt, this indicates that the environment is active.
Small footnote (if you are using the most current version of python [3.12], you may have to install all dependencies one by one!)
## Installing Dependencies

     
     pip install -r requirements.txt

## Running the Project 
**Run the app**
  
     python app.py

## Deactivate the Virtual Environment
When you are done with the app, you can just deactivate it with this command: 

  ```sh
  deactivate
