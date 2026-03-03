import streamlit as st

st.title("Benim İlk Streamlit Uygulamam")

isim = st.text_input("Adınızı girin")

if isim:
    st.write(f"Merhaba {isim} 👋")
