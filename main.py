import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 앱 제목
st.title("✨ 신기한 Streamlit 웹앱 ✨")

# 사용자 입력
name = st.text_input("👋 당신의 이름은?", placeholder="여기에 이름을 입력하세요")
st.write(f"환영합니다, **{name}**! 🎉")

# 슬라이더로 데이터 생성
st.subheader("📊 랜덤 데이터 그래프")
num_points = st.slider("데이터 포인트 수를 선택하세요", 10, 100, 50)

# 데이터 생성 및 시각화
data = pd.DataFrame({
    "x": np.random.rand(num_points),
    "y": np.random.rand(num_points)
})
fig, ax = plt.subplots()
ax.scatter(data["x"], data["y"], c="skyblue", alpha=0.7, s=50)
ax.set_title("랜덤 데이터 시각화")
st.pyplot(fig)

# 컬러 피커
st.subheader("🎨 색상 선택")
color = st.color_picker("좋아하는 색상을 선택하세요", "#00f900")
st.write(f"선택한 색상은: **{color}**입니다!")

# 인터랙티브 버튼
if st.button("👉 나만의 메시지 보기"):
    st.success(f"{name}, 오늘도 멋진 하루 되세요! 🌟")

# 사이드바
st.sidebar.title("📌 사이드바 메뉴")
st.sidebar.write("이곳은 사이드바입니다!")
sidebar_option = st.sidebar.selectbox("원하는 옵션을 선택하세요", ["옵션 1", "옵션 2", "옵션 3"])
st.sidebar.write(f"선택한 옵션은: **{sidebar_option}**입니다!")

# 하단 텍스트
st.info("Streamlit으로 만든 인터랙티브 웹앱, 재미있게 사용해보세요! 😎")

