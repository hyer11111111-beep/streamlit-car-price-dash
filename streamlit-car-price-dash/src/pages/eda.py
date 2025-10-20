import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from src.utils.data_loader import load_data

def run_eda():
    st.title('Exploratory Data Analysis')
    st.markdown("### 자동차 구매 데이터 분석")
    
    # 데이터 불러오기
    df = load_data('./data/Car_Purchasing_Data.csv')
    
    st.subheader('데이터 미리보기')
    st.dataframe(df)

    st.subheader('기본 통계')
    st.dataframe(df.describe())

    st.subheader('최대 / 최소값 확인')
    min_max_menu = df.columns[4:]
    select_choice = st.selectbox('컬럼을 선택하세요', min_max_menu)

    st.info(f'{select_choice}는 {int(df[select_choice].min())} 부터 {int(df[select_choice].max())} 까지 있습니다.')

    st.subheader('상관관계 분석')
    multi_menu = df.columns[4:]
    choice_multi_list = st.multiselect('컬럼을 2개 이상 선택하세요', multi_menu)

    if len(choice_multi_list) >= 2:
        correlation_matrix = df[choice_multi_list].corr(numeric_only=True)
        st.dataframe(correlation_matrix)

        fig1 = plt.figure()
        sb.heatmap(data=correlation_matrix, vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.8)
        st.pyplot(fig1)

    st.subheader('각 컬럼 간의 Pair Plot')
    fig2 = sb.pairplot(data=df, vars=['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount'])
    st.pyplot(fig2)

if __name__ == "__main__":
    run_eda()