import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random
import time

# 1. 페이지 설정 (최상단 고정)
st.set_page_config(page_title="Nina's Secret Taro Lab", page_icon="🔮", layout="wide")

# 2. 타이틀 및 스타일링 (시크하게!)
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 15px; width: 100%; border: none; padding: 12px; font-size: 18px; font-weight: bold; transition: all 0.3s; }
    .stButton>button:hover { background-color: #9d4edd; transform: scale(1.02); }
    .stAlert { background-color: #2a2a2a; color: white; border: 1px solid #7b2cbf; border-radius: 10px; }
    h1, h2, h3 { color: #9d4edd !important; font-family: 'Georgia', serif; }
    .stTabs [data-baseweb="tab-list"] { background-color: #1a1a1a; }
    .stTabs [data-baseweb="tab"] { color: #ffffff; font-size: 16px; font-family: 'Georgia', serif; }
    .stTabs [data-baseweb="tab"]:hover { color: #9d4edd; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 Nina's Secret Taro Lab v4.5")
st.markdown("### 당신의 운명, '시크한 논리'로 해석해 드립니다.")

# 3. 사이드바 (컨트롤 패널)
st.sidebar.title("🚀 Lab Control")
lab_mode = st.sidebar.radio("연구 모드 선택", ["오늘의 미스터리 타로", "성격 & 에너지 분석"])

# 4. 데이터 (타로 카드 및 성격 유형)
taro_cards = {
    "The Fool": "🎈 **바보**: 새로운 시작, 모험, 무모함. 오늘 당신의 논리가 조금 무모할 수도? 하지만 즐기세요! (C'est la vie!)",
    "The Magician": "✨ **마법사**: 창조, 기술, 의지력. 당신의 박학다식함이 빛을 발할 날입니다! (Très bien!)",
    "The High Priestess": "🌙 **여사제**: 직관, 신비, 내면의 지혜. 오늘은 논리보다 '느낌'을 믿어보세요.",
    "The Empress": "🌿 **여황제**: 풍요, 모성, 자연. 당신의 창의력이 결실을 맺을 것입니다.",
    "The Emperor": "👑 **황제**: 권위, 구조, 통제. 가끔은 당신의 논리로 세상을 통제하고 싶죠?",
    "The Lovers": "💖 **연인**: 사랑, 조화, 선택. 오늘은 중요한 선택을 해야 할 수도 있습니다.",
    "The Chariot": "🚜 **전차**: 승리, 의지, 통제. 당신의 목표를 향해 거침없이 나아가세요! (Allez!)",
    "Strength": "🦁 **힘**: 용기, 인내, 부드러운 힘. 당신의 논리력은 당신의 가장 큰 힘입니다.",
}

mbti_types = {
    "ENTP": "💡 **발명가**: 박학다식하고 독창적이며 창의적입니다. 끊임없이 새로운 아이디어를 제안하고 논쟁을 즐깁니다.",
    "INTP": "🧠 **아이디어뱅크**: 비평적인 관점을 가지고 있으며 논리적이고 분석적입니다. 지적 호기심이 강합니다.",
    "INTJ": "🎯 **전략가**: 독창적이고 독립적이며 비판적입니다. 목표를 달성하기 위해 집요하게 파고듭니다.",
    "ENTJ": "📢 **지도자**: 단호하고 솔직하며 리더십이 있습니다. 목표를 달성하기 위해 조직을 이끄는 능력이 탁월합니다.",
}

# 5. 메인 화면 구성 (탭)
t1, t2 = st.tabs(["🔮 미스터리 타로", "📊 성격 & 에너지"])

with t1:
    st.subheader("오늘의 미스터리 타로")
    st.write("시크한 논리로 당신의 타로 카드를 해석합니다.")
    if st.button("🃏 운명의 카드 뽑기"):
        with st.spinner("운명의 카드를 섞는 중..."):
            time.sleep(2) # 애니메이션 효과
            card_name, card_desc = random.choice(list(taro_cards.items()))
            st.success(f"당신이 뽑은 카드는: **{card_name}**입니다!")
            st.info(card_desc)
            st.balloons() # 성공 세리머니!

with t2:
    st.subheader("박학다식 성격 분석 & 에너지")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("당신의 MBTI 유형을 입력하고 분석 결과를 확인해 보세요.")
        user_mbti = st.selectbox("당신의 MBTI", list(mbti_types.keys()))
        if st.button("🧠 성격 분석 시작"):
            st.markdown(f"**{user_mbti}** 유형의 분석 결과입니다:")
            st.warning(mbti_types[user_mbti])
            st.snow() # 성격 분석 성공!
            
    with col2:
        st.write("오늘 당신의 지적 호기심과 논리 에너지를 측정합니다.")
        intel_energy = st.slider("지적 호기심", 0, 100, 80)
        logic_energy = st.slider("논리 에너지", 0, 100, 95)
        
        # Plotly 그래프 (v2.4 환경 호환)
        energy_df = pd.DataFrame({
            '에너지 유형': ['지적 호기심', '논리 에너지'],
            '수치': [intel_energy, logic_energy]
        })
        fig = px.bar(energy_df, x='에너지 유형', y='수치', color='에너지 유형', title="오늘의 에너지 리포트")
        fig.update_layout(plot_bgcolor='#1a1a1a', paper_bgcolor='#1a1a1a', font_color='#ffffff')
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Nina's Secret Taro Lab에서 측정한 신뢰도 99.9%의 에너지 리포트입니다.")

# 푸터 (푸터는 심플하게)
st.markdown("---")
st.caption("Nina's Secret Taro Lab | v4.5 | Powered by Gemini & Nina's 시크한 논리")
