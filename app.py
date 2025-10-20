import streamlit as st
import os
from app_home import run_home
from app_eda import run_eda
from app_ml import run_ml

# 페이지 기본 설정
st.set_page_config(
    page_title='자동차 구매 금액 예측',
    page_icon='🚗',
    layout='wide',
    initial_sidebar_state='expanded'
)

# 라이트 테마 스타일 (모던, 파스텔톤)
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Noto+Sans+KR:wght@300;400;700&display=swap');
        :root{
            --bg: #f8fafc;
            --card: #ffffff;
            --muted: #64748b;
            --accent: #2563eb;
            --accent-2: #06b6d4;
        }
        .stApp {
            background: linear-gradient(180deg,var(--bg) 0%, #ffffff 100%);
            color: #0f1724;
            font-family: 'Noto Sans KR', 'Inter', 'Segoe UI', Roboto, Arial;
            -webkit-font-smoothing:antialiased;
        }
        /* header */
        .top-nav{ display:flex; align-items:center; justify-content:space-between; padding:14px 20px; margin-bottom:18px }
        .brand{ font-weight:700; color:var(--accent); font-size:20px }
        .nav-links{ color:var(--muted); font-size:14px }
        .nav-pill{ background:linear-gradient(90deg, rgba(37,99,235,0.08), rgba(6,182,212,0.04)); padding:6px 10px; border-radius:999px; color:var(--accent); font-weight:600; }
        .card{ background: var(--card); padding:18px; border-radius:12px; box-shadow: 0 8px 20px rgba(2,6,23,0.06); border:1px solid rgba(2,6,23,0.04) }
        .kpi{ text-align:center; padding:14px }
        .muted{ color:var(--muted); font-size:13px }
        footer{ color:var(--muted); padding:16px; text-align:center; font-size:13px }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    # Top navigation (brand + quick links)
    st.markdown("""
    <div class='top-nav'>
        <div style='display:flex;align-items:center;gap:12px'>
            <div style='width:44px;height:44px;background:linear-gradient(135deg,#2563eb,#06b6d4);border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700'>CP</div>
            <div class='brand'>자동차 구매 금액 예측</div>
        </div>
        <div style='display:flex;align-items:center;gap:10px'>
            <div class='nav-pill'>홈</div>
            <div class='nav-pill'>EDA</div>
            <div class='nav-pill'>ML</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 사이드바: 모델 선택, 다운로드
    st.sidebar.markdown("<div style='padding:8px 12px'><h3 style='color:#111827'>앱 메뉴</h3></div>", unsafe_allow_html=True)
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.radio('', menu)
    st.sidebar.markdown('---')
    # 모델 관리는 ML 페이지에서 처리합니다.
    st.sidebar.markdown('**데이터**')
    data_file = os.path.join('.', 'data', 'Car_Purchasing_Data.csv')
    data_bytes = None
    if os.path.exists(data_file):
        try:
            with open(data_file, 'rb') as f:
                data_bytes = f.read()
        except Exception:
            data_bytes = None

    st.sidebar.download_button('샘플 데이터 다운로드', data=data_bytes, file_name='Car_Purchasing_Data.csv', help='데이터 파일이 존재하면 다운로드됩니다.', disabled=(data_bytes is None))

    # 페이지 라우팅

    if choice == 'Home':
        run_home()
    elif choice == 'EDA':
        run_eda()
    elif choice == 'ML':
        run_ml()

    # footer
    st.markdown("<footer style='margin-top:18px; padding-top:8px; border-top:1px solid rgba(0,0,0,0.04)'>© 2025 자동차 구매 금액 예측 — Built with Streamlit</footer>", unsafe_allow_html=True)


if __name__ == '__main__':
        main()

