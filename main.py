import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="멋진 웹사이트",
    page_icon="✨",
    layout="centered"
)

# 제목 및 소개
st.title("✨ 나의 첫번째 웹사이트 ✨")
st.markdown("**Streamlit으로 간단하면서도 멋진 웹앱을 만들어봅시다!** 🌟")

# 이미지 추가
st.image(
    "https://source.unsplash.com/800x400/?nature,technology",
    caption="아름다운 자연과 기술의 조화",
    use_column_width=True
)

# 데이터 생성 및 표시
st.header("📋 랜덤 데이터 생성")
rows = st.slider("생성할 데이터의 행 수", 5, 50, 10)
cols = 5  # 고정된 열 수
data = pd.DataFrame(np.random.randn(rows, cols), columns=[f"열 {i+1}" for i in range(cols)])
st.write("랜덤 데이터 미리보기:")
st.dataframe(data)

# 그래프 표시
st.header("📊 간단한 데이터 시각화")
if st.button("📈 그래프 보기"):
    st.line_chart(data)

# 사용자 메시지
name = st.text_input("이름을 입력하세요", placeholder="여기에 이름을 입력하세요")
if name:
    st.success(f"안녕하세요, {name}님! 이 앱을 즐겨주세요! 😊")

# 푸터
st.markdown("---")
st.markdown("**💡 이 앱은 Streamlit으로 제작되었습니다.**")





