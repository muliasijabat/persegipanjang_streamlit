import streamlit as st

st.title('Hitung Luas Persegi Panjang')

st.write("Masukkan nilai panjang dan lebar di bawah ini:")
panjang = st.number_input("Panjang:")
lebar = st.number_input("Lebar:")
hitung = st.button("Hitung luas")

if hitung:
    luas = panjang * lebar
    st.write("Luas Persegi Panjang adalah:", luas)
