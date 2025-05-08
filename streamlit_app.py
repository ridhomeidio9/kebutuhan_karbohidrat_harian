import streamlit as st

st.set_page_config(page_title="Kalkulator Karbohidrat", layout="centered")

st.title("Kalkulator Kebutuhan Karbohidrat Harian")

st.markdown("""
Karbohidrat adalah sumber energi utama bagi tubuh. Mereka terbagi menjadi dua jenis:

- **Karbohidrat Sederhana**: Seperti gula pasir dan sirup jagung.
- **Karbohidrat Kompleks**: Seperti buah-buahan, sayuran, kacang-kacangan, dan biji-bijian utuh.

Karbohidrat kompleks lebih sehat karena dicerna lebih lambat dan membantu mengontrol kadar gula darah.
""")

# Input pengguna
gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
age = st.slider("Usia Anda (tahun)", 10, 80, 25)

# Fungsi untuk menghitung kebutuhan karbohidrat
def
