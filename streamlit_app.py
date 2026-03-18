import streamlit as st
import sys

# [1순위] 페이지 설정 - 이 코드는 무조건 최상단에 있어야 함!
try:
    st.set_page_config(page_title="Anti-Gravity Ultimate Analyzer", page_icon="🚀", layout="wide")
except Exception:
    pass

# [2순위] 라이브러리 체크 (오류 방지용)
try:
    import pandas as pd
    import numpy as np
    import plotly.express as px
except ImportError as e:
    st.error(f"⚠️ 필수 라이브러리가 설치되지 않았습니다: {e}")
    st.info("터미널에 다음을 입력해 주세요: python -m pip install plotly openpyxl pandas numpy")
    st.stop()

# 스타일링
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 사이드바
st.sidebar.title("🚀 Anti-Gravity Control")
st.sidebar.success("시스템 엔진 가동 중")
theme_color = st.sidebar.color_picker("차트 메인 컬러", "#FF4B4B")

# 메인 타이틀
st.title("📊 Anti-Gravity 통합 분석기 v2.4")
st.write("실습 데이터를 업로드하거나 시뮬레이션을 확인하세요.")

# 1. 파일 업로더
uploaded_file = st.file_uploader("CSV 또는 XLSX 파일을 업로드하세요", type=['csv', 'xlsx'])

# 데이터 로딩 로직
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        is_sim = False
        st.success(f"✅ '{uploaded_file.name}' 로드 성공!")
    except Exception as e:
        st.error(f"❌ 파일을 읽는 중 오류가 발생했습니다: {e}")
        st.stop()
else:
    # 기본 시뮬레이션 데이터
    df = pd.DataFrame({
        '실험회차': range(1, 21),
        '중력에너지': np.random.uniform(0.8, 1.2, 20),
        '안정성': np.random.uniform(85, 100, 20),
        '고도': np.random.randint(400, 500, 20)
    })
    is_sim = True

# 탭 구성
t1, t2, t3, t4 = st.tabs(["📄 데이터 정보", "📈 통계 분석", "🎨 차트 빌더", "🧠 AI 리포트"])

with t1:
    if is_sim:
        st.caption("📍 시뮬레이션 모드 작동 중")
    st.dataframe(df.head(10), use_container_width=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("레코드 수", len(df))
    c2.metric("변수 개수", len(df.columns))
    c3.metric("결측치 수", df.isnull().sum().sum())

with t2:
    st.subheader("데이터 요약 통계")
    st.write(df.describe())

with t3:
    st.subheader("커스텀 시각화")
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if len(num_cols) >= 2:
        col_x = st.selectbox("X축", num_cols, index=0)
        col_y = st.selectbox("Y축", num_cols, index=1 if len(num_cols)>1 else 0)
        c_type = st.radio("그래프 형태", ["Line", "Bar", "Scatter"], horizontal=True)
        
        if c_type == "Line": fig = px.line(df, x=col_x, y=col_y, color_discrete_sequence=[theme_color])
        elif c_type == "Bar": fig = px.bar(df, x=col_x, y=col_y, color_discrete_sequence=[theme_color])
        else: fig = px.scatter(df, x=col_x, y=col_y, color_discrete_sequence=[theme_color])
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("시각화할 숫자 데이터가 부족합니다.")

with t4:
    st.subheader("🧠 창의적 분석 리포트")
    if not df.empty and len(num_cols) > 0:
        avg = df[num_cols[0]].mean()
        st.write(f"🔍 **핵심 요약:** `{num_cols[0]}`의 평균값은 **{avg:.2f}**입니다.")
        st.write("✨ **시스템 제안:** 데이터의 변동 폭이 안정적입니다. 안티그라비티 엔진 출력을 2.5% 상향 조정해도 안전할 것으로 판단됩니다.")
        st.balloons()

# 푸터 및 도움말
st.markdown("---")
with st.expander("❓ 앱이 정상적으로 작동하지 않나요?"):
    st.write("1. 터미널에서 `Ctrl + C`를 눌러 서버를 끄고 다시 `streamlit run data_loader.py`를 입력해 보세요.")
    st.write("2. 가상환경 `(venv)`가 켜져 있는지 확인하세요.")
    st.write("3. 엑셀 업로드 시 에러가 나면 터미널에 `pip install openpyxl`을 입력하세요.")

st.caption("Anti-Gravity Creative Lab | v2.4 (Stable Version)")
