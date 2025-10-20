import streamlit as st
from app_home import run_home
from app_eda import run_eda
import streamlit as st
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
    :root{
      --bg: #f7fafc;
      --card: #ffffff;
      --muted: #6b7280;
      --accent: #2563eb; /* blue-600 */
      --soft: #eff6ff; /* blue-50 */
    }
    .stApp {
      background: linear-gradient(180deg,var(--bg) 0%, #eef2ff 100%);
      color: #0f1724;
      font-family: 'Inter', 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
    }
    .card{
      background: var(--card);
      padding:20px;
      border-radius:14px;
      box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
      border: 1px solid rgba(15,23,42,0.04);
    }
    .header-title{ color:var(--accent); font-weight:700 }
    .muted{ color:var(--muted); font-size:13px }
    .stSidebar { background: linear-gradient(180deg,#ffffff 0%, #f8fafc 100%); }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    # 헤더
    left, center, right = st.columns([1,3,1])
    with center:
        st.markdown("""
        <div class='card' style='text-align:center'>
          <h1 class='header-title'>🚗 자동차 구매 금액 예측</h1>
          <div class='muted'>EDA와 머신러닝을 결합해 직관적인 인사이트와 예측 결과를 제공합니다.</div>
        </div>
        """, unsafe_allow_html=True)

    # 사이드바
    st.sidebar.markdown("<div style='padding:8px 12px'><h3 style='color:#111827'>메뉴</h3></div>", unsafe_allow_html=True)
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.radio('', menu)

    if choice == 'Home':
        run_home()
    elif choice == 'EDA':
        run_eda()
    elif choice == 'ML':
        run_ml()


if __name__ == '__main__':
    main()

