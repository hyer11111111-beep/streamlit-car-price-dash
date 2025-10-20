import streamlit as st
import joblib
import pandas as pd
from components.ui import styled_input, styled_button

def run_ml():
    st.subheader('구매 금액 예측하기')
    st.info('아래 정보를 입력하면, 금액을 예측해 드립니다.')

    gender_list = ['여자', '남자']
    gender = st.radio('성별을 입력하세요', gender_list)
    
    gender_data = 0 if gender == gender_list[0] else 1

    age = styled_input('나이 입력', min_value=20, max_value=90, value=30)
    salary = styled_input('연봉 입력 (달러)', min_value=10000, value=50000)
    debt = styled_input('카드빚 입력 (달러)', min_value=0, value=0)
    worth = styled_input('자산 입력(달러)', min_value=10000, step=1000, value=100000)

    if styled_button('예측하기!'):
        regressor = joblib.load('./model/regressor.pkl')
        new_data = [{'Gender': gender_data, 'Age': age, 'Annual Salary': salary, 'Credit Card Debt': debt, 'Net Worth': worth}]    
        df_new = pd.DataFrame(data=new_data)
        y_pred = regressor.predict(df_new)  

        if y_pred < 0:
            st.warning('구매 금액 예측이 어렵습니다.')
        else:
            price = format(round(y_pred[0]), ',') 
            st.info(f'예측한 금액은 {price} 달러입니다.')