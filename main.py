import streamlit as st

st.title("나의 첫번째 앱")

st.text('n\n')

st.write('안녕하세요,저는 😎입니다')
st.write('저의 이메일 주소는 24_10522@daejin.sen.hs.kr입니다')


st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
