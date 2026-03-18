import streamlit as st
import pandas as pd
import plotly.express as px
import random
import time

# 1. 페이지 설정
st.set_page_config(page_title="Nina's Mental Lab", page_icon="🧪", layout="wide")

# 2. 스타일링 (네온 그린 & 블랙 컨셉 - 개발자 느낌 물씬!)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ff41; }
    .stButton>button { background-color: #00ff41; color: black; border-radius: 10px; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #008f11; color: white; }
    h1, h2, h3 { color: #00ff41 !important; font-family: 'Courier New', monospace; }
    .stSlider [data-baseweb="slider"] { color: #00ff41; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧪 Nina's Mental Logic Lab v5.0")
st.write("오늘 당신의 멘탈 상태를 논리적으로 데이터화하여 처방전을 내립니다.")

# 3. 데이터 및 로직
quotes = [
    "프랑스어로 'C'est la vie'라고 하죠. 에러 좀 나면 어때요? 인생이 그런 거지.",
    "폭풍우가 지나가면 무지개가 뜨듯, 오늘 이 어려움들도 결국 성장의 거름이 될 거예요.",
    "논리가 부족하면 목소리라도 커야 합니다. 하지만 당신은 둘 다 갖췄군요!",
    "완벽주의는 피곤해요. 오늘 조퇴한 당신이 진정한 승리자입니다.",
    "불필요한 로그(Log)가 너무 많이 찍히네요. 레벨을 'Error'로 상향 조정합니다.",
    "가끔은 쉼표(,)가 마침표(.)보다 중요합니다. 오늘 고뇌는 더 멀리 가기 위한 쉼표예요.",
    "잠시 서버를 재부팅(Reboot)하는 시간입니다. 내일은 더 맑은 정신으로 만나요."
    
]

colors = {
    "심해의 블루": "#0077b6",
    "열정의 레드": "#e63946",
    "평화의 그린": "#2a9d8f",
    "자유의 옐로우": "#e9c46a",
    "시크한 퍼플": "#6d597a",
    "새벽의 그레이": "#4a4e69", # 추가 1: 차분하고 고급스러운 느낌
    "네온 라임": "#ccff00"     # 추가 2: 톡 쏘는 ENTP의 에너지 느낌
}


# 4. 레이아웃 (2개 탭)
tab1, tab2 = st.tabs(["📊 멘탈 분석기", "🌈 컬러 처방전"])

with tab1:
    st.subheader("오늘의 멘탈 로그 분석")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("당신의 현재 지수를 설정하세요.")
        stress = st.slider("스트레스 지수", 0, 100, 50)
        happiness = st.slider("행복 지수", 0, 100, 70)
        anger = st.slider("빡침 지수", 0, 100, 20)
        
        if st.button("📈 분석 결과 도출"):
            with st.spinner("알고리즘 가동 중..."):
                time.sleep(1.5)
                st.success("분석 완료!")
                st.balloons()
    
    with col2:
        # 데이터프레임 생성 및 Plotly 차트 (조교님이 깔아준 거!)
        data = pd.DataFrame({
            '항목': ['스트레스', '행복', '빡침'],
            '수치': [stress, happiness, anger]
        })
        fig = px.line_polar(data, r='수치', theta='항목', line_close=True, 
                            title="당신의 멘탈 레이더망", template="plotly_dark")
        fig.update_traces(fill='toself', line_color='#00ff41')
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("니나의 시크한 처방전")
    if st.button("💊 처방전 받기"):
        c_name, c_code = random.choice(list(colors.items()))
        st.markdown(f"### 오늘의 추천 컬러: <span style='color:{c_code}'>{c_name}</span>", unsafe_allow_html=True)
        st.info(random.choice(quotes))
        st.snow()

st.markdown("---")
st.caption("Nina's Logic Lab | v5.0 | '조퇴는 지능 순' 캠페인 중")
