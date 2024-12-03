import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import os

def calculate_nps(df):
    """
    Calculate Net Promoter Score from DataFrame
    """
    promoters = len(df[df['score'] >= 9])
    detractors = len(df[df['score'] <= 6])
    total_responses = len(df)
    
    nps = ((promoters - detractors) / total_responses) * 100
    return round(nps, 2)

def categorize_nps_segment(score):
    """
    Categorize NPS score into segments
    """
    if score <= 6:
        return 'Detractors'
    elif score <= 8:
        return 'Passives'
    else:
        return 'Promoters'

def get_nps_insights(nps_score):
    """
    Provide business insights based on NPS score
    """
    insights = {
        'low': {
            'score_range': 'Below 0',
            'interpretation': 'Critical Customer Experience Issues',
            'recommendations': [
                'Conduct in-depth customer interviews',
                'Review and overhaul customer service processes',
                'Implement immediate improvement initiatives',
                'Create a comprehensive customer feedback mechanism'
            ]
        },
        'improving': {
            'score_range': '0-30',
            'interpretation': 'Room for Significant Improvement',
            'recommendations': [
                'Develop targeted customer experience enhancement programs',
                'Identify and address key pain points',
                'Implement regular customer feedback loops',
                'Train staff on customer satisfaction techniques'
            ]
        },
        'good': {
            'score_range': '30-50',
            'interpretation': 'Solid Customer Satisfaction',
            'recommendations': [
                'Continue current customer experience strategies',
                'Identify areas for incremental improvements',
                'Develop loyalty programs',
                'Encourage and incentivize positive reviews'
            ]
        },
        'excellent': {
            'score_range': '50-70',
            'interpretation': 'Outstanding Customer Loyalty',
            'recommendations': [
                'Maintain current high-quality service standards',
                'Develop referral programs',
                'Create exclusive customer experiences',
                'Use promoters as brand ambassadors'
            ]
        },
        'world_class': {
            'score_range': '70-100',
            'interpretation': 'World-Class Customer Experience',
            'recommendations': [
                'Continue innovating customer experience',
                'Share best practices across the organization',
                'Develop advanced customer retention strategies',
                'Create case studies and success stories'
            ]
        }
    }
    
    if nps_score < 0:
        return insights['low']
    elif nps_score < 30:
        return insights['improving']
    elif nps_score < 50:
        return insights['good']
    elif nps_score < 70:
        return insights['excellent']
    else:
        return insights['world_class']

def create_nps_visualizations(df):
    """
    Create NPS visualizations
    """
    # Segment Distribution Pie Chart
    segment_counts = df['segment'].value_counts()
    pie_chart = px.pie(
        values=segment_counts.values, 
        names=segment_counts.index, 
        title='NPS Segment Distribution',
        color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1']
    )
    
    # Score Distribution Histogram
    hist_chart = px.histogram(
        df, 
        x='score', 
        title='Score Distribution',
        labels={'score': 'NPS Score', 'count': 'Number of Responses'},
        color_discrete_sequence=['#45B7D1']
    )
    
    return pie_chart, hist_chart

def save_survey_response(name, email, score, feedback):
    """
    Save survey response to CSV
    """
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, 'nps_responses.csv')
    
    # Check if file exists, if not create with headers
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=['name', 'email', 'score', 'feedback', 'segment', 'timestamp'])
        df.to_csv(file_path, index=False)
    
    # Read existing data
    df = pd.read_csv(file_path)
    
    # Add new response
    new_response = pd.DataFrame([{
        'name': name,
        'email': email,
        'score': score,
        'feedback': feedback,
        'segment': categorize_nps_segment(score),
        'timestamp': pd.Timestamp.now()
    }])
    
    # Append and save
    df = pd.concat([df, new_response], ignore_index=True)
    df.to_csv(file_path, index=False)
    
    return df