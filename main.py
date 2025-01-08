import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(
    page_title="아름다운 웹사이트",
    page_icon="✨",
    layout="wide"
)

# 메인 제목
st.title("✨ 나의 첫번째 앱 ✨")
st.subheader("Streamlit으로 만든 아름다운 웹사이트에 오신 것을 환영합니다! 🌈")
st.markdown("---")

# 배너 이미지 추가
st.image(
    "https://source.unsplash.com/1200x400/?nature,landscape",
    caption="아름다운 자연을 담은 배너",
    use_column_width=True
)

# 컬럼을 활용한 레이아웃
col1, col2 = st.columns(2)

with col1:
    st.header("🌟 멋진 기능 소개")
    st.write("""
    이 웹사이트는 다음과 같은 기능을 제공합니다:
    - 데이터를 생성하고 다운로드
    - 아름다운 그래프 시각화
    - 사용자 인터페이스로 손쉬운 탐색
    """)
    st.write("아래 버튼을 눌러 새로운 기능을 탐색하세요!")

with col2:
    st.header("📊 데이터 미리보기")
    sample_data = pd.DataFrame({
        "항목": ["A", "B", "C", "D"],
        "값": [23, 45, 56, 78]
    })
    st.dataframe(sample_data)

# 데이터 생성 및 다운로드 섹션
st.markdown("---")
st.header("📋 데이터 생성 및 다운로드")
rows = st.slider("데이터의 행 수를 선택하세요", 5, 50, 10)
cols = st.slider("데이터의 열 수를 선택하세요", 2, 5, 3)
data = pd.DataFrame(
    np.random.rand(rows, cols),
    columns=[f"Column {i+1}" for i in range(cols)]
)
st.write("생성된 데이터:")
st.dataframe(data)
st.download_button(
    label="📥 데이터 다운로드",
    data=data.to_csv(index=False).encode("utf-8"),
    file_name="generated_data.csv",
    mime="text/csv"
)

# 그래프 시각화 섹션
st.markdown("---")
st.header("📊 그래프 시각화")
graph_type = st.selectbox("그래프 유형을 선택하세요", ["Sine Wave", "Cosine Wave", "Random Scatter"])

x = np.linspace(0, 10, 100)

if graph_type == "Sine Wave":
    y = np.sin(x)
    title = "Sine Wave"
elif graph_type == "Cosine Wave":
    y = np.cos(x)
    title = "Cosine Wave"
else:
    x = np.random.rand(100)
    y = np.random.rand(100)
    title = "Random Scatter"

fig, ax = plt.subplots()
ax.plot(x, y, marker='o', color="skyblue") if graph_type != "Random Scatter" else ax.scatter(x, y, color="orange")
ax.set_title(title, fontsize=16)
ax.grid(True)
st.pyplot(fig)

# 푸터
st.markdown("---")







