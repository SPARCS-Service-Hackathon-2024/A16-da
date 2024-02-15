import streamlit as st
import pandas as pd
import plotly.express  as px

st.set_page_config(layout="wide")
st.markdown("# 관광 여행정보 획득경로")
st.sidebar.markdown("# 관광 여행정보 획득경로 막대 그래프 페이지입니다.")

def bar_chart(*geo):
    bar_df = edited_df[edited_df["선택"]]
    fig = px.bar(bar_df,
                 title="관광 여행정보 획득경로 막대 차트",
                y='값',
                color="구분",
                hover_data='값')
    return fig


# 페이지 구성
df = pd.read_csv("static/tour_process.csv")
#st.title("지역 별 관광객 수")

pivot_table = pd.pivot_table(df,index="구분",values=["값"],aggfunc="mean")
pivot_table["선택"] = pivot_table["값"].apply(lambda x: False)

col1, col2 = st.columns([2, 3])

with col1:
    st.write("\n\n")
    edited_df = st.data_editor(pivot_table)

edited_df["구분"] = edited_df.index
select = list(edited_df[edited_df["선택"]]["구분"])

with col2:
    # Bar chart 탭
    st.plotly_chart(bar_chart())
    st.markdown("출처: 문화체육관광부,「국민여행조사」, 2022, 2024.02.14, 관광여행 정보 획득 경로 (1순위)")