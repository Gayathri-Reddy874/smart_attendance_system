import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import mysql.connector
import pandas as pd
from datetime import datetime
from config import DB_CONFIG

st.set_page_config(page_title="Smart Attendance Dashboard", layout="wide")

st.title("📊 Smart Attendance Dashboard")

conn = mysql.connector.connect(**DB_CONFIG)

df = pd.read_sql("SELECT * FROM attendance_new ORDER BY id DESC", conn)

if df.empty:
    st.warning("No data found")
    st.stop()

df["date"] = pd.to_datetime(df["date"])

total = len(df)
unique = df["name"].nunique()

today = pd.to_datetime(datetime.now().date())
today_count = df[df["date"] == today].shape[0]

c1, c2, c3 = st.columns(3)
c1.metric("Total", total)
c2.metric("Unique", unique)
c3.metric("Today", today_count)

st.dataframe(df, use_container_width=True)

st.subheader("Person Count")
st.bar_chart(df["name"].value_counts())

st.subheader("Daily Trend")
st.line_chart(df.groupby(df["date"].dt.date).size())

st.success("System Running Successfully")