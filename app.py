import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import os

from utils_ import (
    calculate_nps, 
    get_nps_insights, 
    create_nps_visualizations,
    save_survey_response
)

def main():
    st.set_page_config(
        page_title="NPS Survey Dashboard", 
        page_icon="📊", 
        layout="wide"
    )

    # Sidebar Navigation
    st.sidebar.title("NPS Survey Dashboard")
    app_mode = st.sidebar.radio(
        "Navigate", 
        ["Survey", "NPS Analysis", "Insights", "Download Data"]
    )

    # Survey Page
    if app_mode == "Survey":
        st.title("Customer Satisfaction Survey")
        
        with st.form("nps_survey"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            
            st.write("How likely are you to recommend us to a friend or colleague?")
            score = st.slider(
                "Likelihood (0 = Not at all likely, 10 = Extremely likely)", 
                0, 10, 5
            )
            
            feedback = st.text_area("Additional Feedback (Optional)")
            
            submit_button = st.form_submit_button("Submit Survey")
            
            if submit_button:
                if name and email:
                    # Save survey response
                    df = save_survey_response(name, email, score, feedback)
                    
                    st.success("Thank you for your feedback!")
                    st.balloons()
                else:
                    st.error("Please provide your name and email.")

    # NPS Analysis Page
    elif app_mode == "NPS Analysis":
        st.title("NPS Analysis")
        
        # Check if data exists
        data_file = 'data/nps_responses.csv'
        if os.path.exists(data_file):
            df = pd.read_csv(data_file)
            
            # Calculate overall NPS
            nps_score = calculate_nps(df)
            st.metric("Net Promoter Score", f"{nps_score}%")
            
            # Create visualizations
            col1, col2 = st.columns(2)
            
            with col1:
                pie_chart, _ = create_nps_visualizations(df)
                st.plotly_chart(pie_chart)
            
            with col2:
                _, hist_chart = create_nps_visualizations(df)
                st.plotly_chart(hist_chart)
        else:
            st.warning("No survey data available. Please submit a survey first.")

    # Insights Page
    elif app_mode == "Insights":
        st.title("NPS Insights")
        
        # Check if data exists
        data_file = 'data/nps_responses.csv'
        if os.path.exists(data_file):
            df = pd.read_csv(data_file)
            nps_score = calculate_nps(df)
            
            insights = get_nps_insights(nps_score)
            
            st.subheader(f"NPS Score: {nps_score}%")
            st.subheader(f"Interpretation: {insights['interpretation']}")
            
            st.write("### Recommendations:")
            for rec in insights['recommendations']:
                st.write(f"- {rec}")
        else:
            st.warning("No survey data available. Please submit a survey first.")

    # Download Data Page
    elif app_mode == "Download Data":
        st.title("Download NPS Data")
        
        # Check if data exists
        data_file = 'data/nps_responses.csv'
        if os.path.exists(data_file):
            df = pd.read_csv(data_file)
            
            st.dataframe(df)
            
            # Download button
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download NPS Data as CSV",
                data=csv,
                file_name="nps_survey_responses.csv",
                mime="text/csv"
            )
        else:
            st.warning("No survey data available. Please submit a survey first.")

if __name__ == "__main__":
    main()