import streamlit as st

def run_home():
    st.title('자동차 구매 금액 예측 앱')
    st.subheader('자동차 데이터를 분석하고 예측하는 앱입니다.')
    st.info('이 앱은 캐글에 있는 Car_Purchasing_Data.csv 파일을 사용하여 자동차 구매 금액을 예측합니다.')
    st.text('탐색적 데이터 분석과 머신러닝 모델을 통해 예측 결과를 제공합니다.')
    st.image('./assets/car.jpg', use_column_width=True)

    st.markdown(
        """
        ### 사용 방법
        1. **탐색적 데이터 분석(EDA)** 메뉴를 선택하여 데이터의 통계 및 시각화를 확인하세요.
        2. **구매 금액 예측하기(ML)** 메뉴를 선택하여 필요한 정보를 입력하고 예측 결과를 확인하세요.
        """
    )

if __name__ == "__main__":
    run_home()