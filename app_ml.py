import streamlit as st
# 모델 불러오기 위한 라이브러리
import joblib
import pandas as pd
import os


def run_ml():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader('구매 금액 예측하기')
    st.write('아래 정보를 입력하면, 학습된 모델로 자동차 구매 금액을 예측합니다.')
    st.markdown("</div>", unsafe_allow_html=True)

    # 입력 레이아웃을 컬럼으로 정리
    col1, col2, col3 = st.columns(3)
    gender_list = ['여자', '남자']
    with col1:
        gender = st.radio('성별을 입력하세요', gender_list, horizontal=True)
        gender_data = 0 if gender == '여자' else 1

    with col2:
        age = st.number_input('나이 입력', min_value=18, max_value=100, value=30)

    with col3:
        salary = st.number_input('연봉 입력 (달러)', min_value=0, value=50000, step=1000)

    col4, col5 = st.columns(2)
    with col4:
        debt = st.number_input('카드빚 입력 (달러)', min_value=0, value=1000, step=100)
    with col5:
        worth = st.number_input('자산 입력(달러)', min_value=0, value=50000, step=1000)

    model_path = os.path.join('.', 'model', 'regressor.pkl')

    if st.button('예측하기!'):
        if not os.path.exists(model_path):
            st.error('모델 파일을 찾을 수 없습니다: model/regressor.pkl')
            return

        try:
            regressor = joblib.load(model_path)
        except Exception as e:
            st.error(f'모델 로드 실패: {e}')
            return

        new_data = [{'Gender': gender_data, 'Age': age, 'Annual Salary': salary,
                     'Credit Card Debt': debt, 'Net Worth': worth}]
        df_new = pd.DataFrame(new_data)

        try:
            y_pred = regressor.predict(df_new)
            pred_val = float(y_pred[0])
        except Exception as e:
            st.error(f'예측 중 오류가 발생했습니다: {e}')
            return

        if pred_val < 0:
            st.warning('구매 금액 예측이 어렵습니다.')
        else:
            price = f"{int(round(pred_val)):,}"
            st.success(f'예측한 금액은 {price} 달러입니다.')


if __name__ == "__main__":
    run_ml()

