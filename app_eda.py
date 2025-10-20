import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import os

def run_eda():
    st.subheader('탐색적 데이터 분석 (EDA)')
    data_path = os.path.join('.', 'data', 'Car_Purchasing_Data.csv')

    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        st.error('데이터 파일을 찾을 수 없습니다: data/Car_Purchasing_Data.csv')
        return

    st.caption('원본: Car_Purchasing_Data.csv')

    radio_menu = ['데이터프레임', '기본통계']
    radio_choice = st.radio('표시 옵션', radio_menu, horizontal=True)
    if radio_choice == radio_menu[0]:
        st.dataframe(df)
    else:
        st.dataframe(df.describe(include='all'))

    st.subheader('최대 / 최소값 확인')
    # 분석할 수치형 컬럼 리스트(첫 4개 인덱스 제외)
    numeric_cols = df.columns[4:]
    if len(numeric_cols) == 0:
        st.warning('분석할 수치형 컬럼이 없습니다.')
        return

    select_choice = st.selectbox('컬럼을 선택하세요', numeric_cols)

    min_val = df[select_choice].min()
    max_val = df[select_choice].max()
    st.info(f'{select_choice}는 {min_val} 부터 {max_val} 까지 있습니다.')

    st.subheader('상관관계 분석')
    multi_menu = numeric_cols
    choice_multi_list = st.multiselect('컬럼을 2개 이상 선택하세요', multi_menu)

    if len(choice_multi_list) >= 2:
        corr = df[choice_multi_list].corr(numeric_only=True)
        st.dataframe(corr)

        fig1, ax1 = plt.subplots(figsize=(6,4))
        sb.heatmap(data=corr, vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.8, ax=ax1)
        st.pyplot(fig1)

    st.subheader('각 컬럼간의 Pair Plot')
    # pairplot은 큰 리소스일 수 있으므로 선택적으로 보여주기
    with st.expander('Pair Plot 표시 (시간 소요 가능)'):
        pair_vars = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
        # 컬럼이 실제로 존재하는지 필터링
        pair_vars = [c for c in pair_vars if c in df.columns]
        if len(pair_vars) >= 2:
            with st.spinner('Pair plot 생성 중...'):
                g = sb.pairplot(data=df, vars=pair_vars, corner=True)
                st.pyplot(g.fig)
        else:
            st.warning('Pair plot에 필요한 컬럼이 데이터에 없습니다.')

if __name__ == "__main__":
   run_eda()