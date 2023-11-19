import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title('Dash Board')

    # Load the data
    data = pd.read_csv('data_for_dash.csv')

    # Add your Streamlit components and Plotly plots here
    # For example, you can create a line plot using Plotly and display it with Streamlit:
    fig = px.line(data, x='ACTIVITY_DATE', y='REVENUE')
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()