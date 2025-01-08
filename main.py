import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 앱 제목
st.title("🌟 나의 첫번째 앱 🌟")

# 서브 타이틀
st.subheader("Streamlit을 활용한 간단하고 신기한 웹앱")

# 사용자 입력
st.write("**당신의 이름을 입력해 주세요!** 😊")
name = st.text_input("이름", placeholder="여기에 이름을 입력하세요")
if name:
    st.write(f"환영합니다, **{name}** 님! 🎉")

# 사이드바
st.sidebar.title("📌 사이드바 메뉴")
st.sidebar.markdown("**여기에서 옵션을 선택할 수 있습니다!**")
sidebar_option = st.sidebar.selectbox("원하는 옵션을 선택하세요", ["홈", "데이터 보기", "그래프 보기"])

# 홈 섹션
if sidebar_option == "홈":
    st.image("https://source.unsplash.com/800x400/?nature,water", caption="자연을 느껴보세요! 🌿", use_column_width=True)
    st.write("""
    ### Streamlit 소개
    Streamlit은 데이터 시각화와 대화형 웹 애플리케이션 개발을 쉽게 할 수 있도록 도와주는 파이썬 프레임워크입니다.
    아래에서 다양한 기능을 탐색해 보세요!
    """)

# 데이터 보기 섹션
elif sidebar_option == "데이터 보기":
    st.write("### 랜덤 데이터 생성 및 확인 📋")
    rows = st.slider("데이터의 행 수를 선택하세요", 5, 50, 10)
    cols = st.slider("데이터의 열 수를 선택하세요", 2, 5, 3)
    data = pd.DataFrame(np.random.randn(rows, cols), columns=[f"Column {i+1}" for i in range(cols)])
    st.dataframe(data)

# 그래프 보기 섹션
elif sidebar_option == "그래프 보기":
    st.write("### 간단한 그래프 시각화 📊")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, color="blue", label="Sine Wave")
    ax.legend()
    ax.set_title("Sine Wave Graph")
    st.pyplot(fig)

# 푸터
st.markdown("---")
st.markdown("### 💡 참고: 이 앱은 Streamlit으로 제작되었습니다.")
st.markdown("[더 많은 아이디어 보기](https://docs.streamlit.io/)")


