import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. 페이지 설정 (최상단 고정)
st.set_page_config(page_title="Anti-Gravity Analyzer", page_icon="🚀", layout="wide")

# 2. 타이틀 및 스타일
st.title("📊 Anti-Gravity 통합 분석기 v2.4")
st.markdown("<style>.stMetric {background-color: #f0f2f6; padding: 10px; border-radius: 10px;}</style>", unsafe_allow_html=True)

# 3. 사이드바 제어
st.sidebar.title("🚀 Control Panel")
theme_color = st.sidebar.color_picker("차트 컬러 선택", "#00FFAA")

# 4. 데이터 생성 (업로드 파일 없으면 시뮬레이션 데이터 사용)
df = pd.DataFrame({
    '실험회차': range(1, 21),
    '중력에너지': np.random.uniform(0.8, 1.2, 20),
    '안정성': np.random.uniform(85, 100, 20)
})

# 5. 메인 화면 구성 (탭)
t1, t2 = st.tabs(["📈 시각화 분석", "📄 데이터 표"])

with t1:
    st.subheader("실시간 에너지 변동 그래프")
    fig = px.line(df, x='실험회차', y='중력에너지', title="Anti-Gravity Stability Test")
    fig.update_traces(line_color=theme_color)
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    col1.metric("평균 중력수치", f"{df['중력에너지'].mean():.2f}")
    col2.metric("최고 안정성", f"{df['안정성'].max():.1f}%")

with t2:
    st.dataframe(df, use_container_width=True)

st.balloons() # 성공하면 풍선이 날아옵니다!
