import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. Page Setup
st.set_page_config(page_title="NST Pune Admissions 2026", layout="wide")
st.title("🛡️ NST Pune Admissions Command Center")

# 2. Connection to your specific Spreadsheet
# Using your provided ID: 11ZO_i5nZ_9PDWebHAtqR8aL3SAjxsWCZUb6Y-SyuG9Q
url = "https://docs.google.com/spreadsheets/d/11ZO_i5nZ_9PDWebHAtqR8aL3SAjxsWCZUb6Y-SyuG9Q/edit?gid=0#gid=0"

conn = st.connection("gsheets", type=GSheetsConnection)

try:
    # Read the data
    df = conn.read(spreadsheet=url)
    
    # 3. Sidebar Navigation
    view = st.sidebar.radio("Select Dashboard View", ["Founder View", "Manager View", "Raw Data"])

    if view == "Founder View":
        st.header("Strategic Executive View")
        # Logic: Metrics for the Founder
        col1, col2 = st.columns(2)
        col1.metric("Total Prospects/Leads", len(df))
        col2.metric("Target Capacity", "480 Seats")
        
        st.write("### Enrollment Velocity")
        st.line_chart(df.index) # Example trend chart

    elif view == "Manager View":
        st.header("Operations & Counselor Performance")
        st.info("Daily Target: 7 Payments")
        # Assuming Counselor names are in the sheet - this will auto-generate a performance chart
        if not df.empty:
            st.write("### Admissions by Counselor")
            # We use the 5th column as a fallback if names aren't clear
            st.bar_chart(df.iloc[:, 0].value_counts()) 

    else:
        st.header("Full Admissions Sheet")
        st.dataframe(df)

except Exception as e:
    st.error("Connection Error: Please ensure your Google Sheet is set to 'Anyone with the link can view'.")
    st.write(e)
