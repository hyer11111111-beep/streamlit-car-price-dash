import streamlit as st
# 모델 불러오기 위한 라이브러리
import joblib
import pandas as pd
import os
from io import BytesIO


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

    # 모델 선택 / 업로드
    st.markdown('**모델 관리**')
    model_dir = os.path.join('.', 'model')
    os.makedirs(model_dir, exist_ok=True)
    available_models = [f for f in os.listdir(model_dir) if f.endswith('.pkl')]
    chosen_model = st.selectbox('로컬 모델 선택', options=['(없음)'] + available_models)
    uploaded_file = st.file_uploader('새 모델 업로드 (.pkl)', type=['pkl'])
    if uploaded_file is not None:
        save_path = os.path.join(model_dir, uploaded_file.name)
        with open(save_path, 'wb') as out:
            out.write(uploaded_file.getbuffer())
        st.success(f'업로드 완료: {uploaded_file.name}')
        chosen_model = uploaded_file.name

    model_path = os.path.join(model_dir, chosen_model) if chosen_model and chosen_model != '(없음)' else None

    if st.button('예측하기!'):
        if model_path is None or not os.path.exists(model_path):
            st.error('선택된 모델이 없습니다. 모델을 선택하거나 업로드하세요.')
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

        # 결과 카드
        if pred_val < 0:
            st.warning('구매 금액 예측이 어렵습니다.')
        else:
            price = int(round(pred_val))
            col_a, col_b = st.columns([2,3])
            with col_a:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.metric('예측 금액 (달러)', f"{price:,}")
                st.markdown("</div>", unsafe_allow_html=True)
            with col_b:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.write('입력 요약')
                st.json(df_new.to_dict(orient='records'))
                st.markdown("</div>", unsafe_allow_html=True)

            # 예측 결과 다운로드
            result_df = df_new.copy()
            result_df['predicted_price'] = price
            csv_bytes = result_df.to_csv(index=False).encode('utf-8')
            st.download_button('예측 결과 다운로드 (CSV)', data=csv_bytes, file_name='prediction.csv')


if __name__ == "__main__":
    run_ml()

