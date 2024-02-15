import streamlit as st
import pandas as pd
import plotly.express  as px

st.set_page_config(layout="wide")
st.markdown("# 연도 별 국내 지역의 방문자 수")
st.sidebar.markdown("# 연도 별 국내 지역의 방문 자 수 표와 그래프입니다.")

# 페이지 구성
df = pd.read_csv("static/domestic_tour_en.csv")

col1, col2 = st.columns([2, 4])

with col1:
    st.write("\n\n")
    st.table(df)


with col2:
    st.line_chart(df.set_index(df.columns[0]).transpose())
    st.markdown("출처: 문화체육관광부,「국민여행조사」, 2022, 2024.02.15, 국내여행 횟수")