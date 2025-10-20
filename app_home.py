import streamlit as st
import pandas as pd
import os


def run_home():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header('자동차 구매 금액 예측')
    st.write('데이터 시각화(EDA)와 머신러닝을 통해 자동차 구매 금액을 예측합니다. 좌측 메뉴에서 기능을 선택하세요.')
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([2,3])
    data_path = os.path.join('.', 'data', 'Car_Purchasing_Data.csv')

    # 데이터 요약 카드
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        if os.path.exists(data_path):
            try:
                df = pd.read_csv(data_path)
                rows, cols = df.shape
                st.subheader('데이터 요약')
                st.metric('행 수', rows)
                st.metric('열 수', cols)
                if rows > 0:
                    st.caption('상위 5개 샘플')
                    st.dataframe(df.head())
            except Exception as e:
                st.error(f'데이터 로드 중 오류가 발생했습니다: {e}')
        else:
            st.warning('데이터 파일을 찾을 수 없습니다: data/Car_Purchasing_Data.csv')
        st.markdown("</div>", unsafe_allow_html=True)

    # 설명과 이미지
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader('앱 설명')
        st.write('이 앱은 간단한 UI로 데이터를 탐색하고, 학습된 모델로 구매 금액을 예측합니다. 모델은 `model/regressor.pkl`에 있어야 합니다.')
        img_path = os.path.join('.', 'image', 'car.jpg')
        if os.path.exists(img_path):
            st.image(img_path, use_column_width=True, caption='Sample Car')
        else:
            st.info('표시할 이미지가 없습니다. image/car.jpg 경로를 확인하세요.')
        st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    run_home()