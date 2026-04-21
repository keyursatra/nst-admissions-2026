import streamlit as st
from shubham_gsheets import connect # 2026 optimized connector

# 1. Page Config
st.set_page_config(page_title="NST Pune Admissions 2026", layout="wide")
st.title("🛡️ NST Pune Admissions Command Center")

# 2. Data Connection
SHEET_ID = "11ZO_i5nZ_9PDWebHAtqR8aL3SAjxsWCZUb6Y-SyuG9Q"
# Connect logic using secrets for security
conn = st.connection("gsheets", type=connect)
df = conn.read(spreadsheet=SHEET_ID)

# 3. Sidebar - Founder & Manager Toggle
view = st.sidebar.selectbox("Choose View", ["Founder View", "Manager View"])

if view == "Founder View":
    st.header("Executive Summary")
    total_paid = len(df[df['Status'] == 'Paid'])
    st.metric("Total Admissions", f"{total_paid} / 480", f"{round((total_paid/480)*100, 1)}%")
    st.write("### Revenue Health")
    st.info(f"Projected Maintenance Fund: ₹{total_paid * 93750:,.2f}")

else:
    st.header("Operations Tracking")
    st.write("### Counselor Performance (Run Rate: 7/day)")
    performance = df.groupby('Counselor')['Payment Date'].count()
    st.bar_chart(performance)
