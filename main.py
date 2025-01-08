import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 메인 제목
st.title("🌟 나의 첫번째 앱 🌟")
st.markdown("**Streamlit을 활용해 나만의 웹앱을 만들어보세요!** 🚀")

# 사용자 이름 입력
name = st.text_input("당신의 이름을 입력해주세요:", placeholder="예: 홍길동")
if name:
    st.write(f"안녕하세요, **{name}** 님! 앱에 오신 것을 환영합니다! 🎉")

# 사이드바 메뉴
st.sidebar.title("📌 메뉴")
menu_option = st.sidebar.radio("원하는 기능을 선택하세요:", ["홈", "데이터 생성", "그래프 시각화"])

# 홈 섹션
if menu_option == "홈":
    st.subheader("🏠 홈 화면")
    st.image("https://source.unsplash.com/800x400/?nature,technology", caption="Streamlit과 함께하는 멋진 앱", use_column_width=True)
    st.write("""
    이 앱은 Streamlit으로 만들어졌습니다.  
    아래 사이드바를 통해 데이터를 생성하거나 그래프를 시각화해보세요!
    """)

# 데이터 생성 섹션
elif menu_option == "데이터 생성":
    st.subheader("📋 데이터 생성")
    rows = st.slider("데이터 행 수 선택", 5, 100, 10)
    cols = st.slider("데이터 열 수 선택", 2, 5, 3)
    data = pd.DataFrame(np.random.randn(rows, cols), columns=[f"Column {i+1}" for i in range(cols)])
    st.write("생성된 데이터 프레임:")
    st.dataframe(data)
    st.download_button("📥 데이터 다운로드", data.to_csv(index=False).encode("utf-8"), "random_data.csv", "text/csv")

# 그래프 시각화 섹션
elif menu_option == "그래프 시각화":
    st.subheader("📊 그래프 시각화")
    st.write("**Sine Wave와 Cosine Wave를 시각화합니다.**")
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    fig, ax = plt.subplots()
    ax.plot(x, y1, label="Sine Wave", color="blue")
    ax.plot(x, y2, label="Cosine Wave", color="orange")
    ax.legend()
    ax.set_title("Sine & Cosine Waves")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    st.pyplot(fig)

# 푸터
st.markdown("---")
st.markdown("**💡 참고:** 이 앱은 Streamlit으로 개발되었습니다.")
st.markdown("[Streamlit 문서 보기](https://docs.streamlit.io/)")





