# NPS Survey Dashboard
### Overview
- This Streamlit application provides a comprehensive Net Promoter Score (NPS) survey and analysis tool. It allows businesses to:

    - Collect customer feedback
    - Calculate NPS
    - Visualize customer segments
    - Get actionable insights

- Here is the Dashboard:

![alt text](image.png)


### Features
    - Interactive NPS Survey
    - Real-time NPS Calculation
    - Segment Distribution Visualization
    - Actionable Business Insights
    - Data Export Functionality
## Setup Instructions
- Prerequisites
    - Python 3.8+
    - pip (Python Package Manager)
### Installation Steps
- Clone the repository
- Create a virtual environment


`python -m venv venv`
`source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`
- Install dependencies

`pip install -r requirements.txt`
- Run the Streamlit App

`streamlit run app.py`

### How to Use
    - Navigate through different sections using the sidebar
    - Complete the survey in the "Survey" section
    - View analysis in "NPS Analysis"
    - Get insights in the "Insights" section
    - Download data in "Download Data"
    - Data Storage
    - Survey responses are stored in data/nps_responses.csv
    - Automatically creates the file on first survey submission
### Customization
    - Modify utils.py to adjust NPS calculation or insights
    - Update visualizations in the utility functions


You Can also find the Application via the link: https://desmondonam-nps-application-app-v3i927.streamlit.app/