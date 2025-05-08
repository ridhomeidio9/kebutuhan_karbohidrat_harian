import streamlit as st

# Data kebutuhan karbohidrat per hari (gram) berdasarkan usia, jenis kelamin, dan status fisiologis
kebutuhan_karbo = {
    'Laki-laki': {
        (10, 12): 300,
        (13, 15): 350,
        (16, 18): 400,
        (19, 29): 430,
        (30, 49): 415,
        (50, 64): 340,
        (65, 80): 275,
        (81, 150): 235
    },
    'Perempuan': {
        (10, 12): 280,
        (13, 18): 300,
        (19, 29): 360,
        (30, 49): 340,
        (50, 64): 280,
        (65, 80): 230,
        (81, 150): 200
    }
}

def get_kebutuhan(usia, jenis_kelamin, status):
    # Menentukan kebutuhan dasar
    kebutuhan = None
    for (usia_min, usia_max), nilai in kebutuhan_karbo[jenis_kelamin].items():
        if usia_min <= usia <= usia_max:
            kebutuhan = nilai
            break
    if kebutuhan is None:
        kebutuhan = 0

    # Menyesuaikan untuk ibu hamil dan menyusui
    if status == 'Hamil':
        kebutuhan += 40  # Rata-rata tambahan
    elif status == 'Menyusui':
        kebutuhan += 50  # Rata-rata tambahan

    return kebutuhan

def halaman_beranda():
    st.title("Apa itu Karbohidrat?")
    st.markdown("""
    Karbohidrat adalah nutrisi penting yang berperan sebagai sumber energi utama bagi tubuh. Mereka terbagi menjadi dua jenis:

    - **Karbohidrat Sederhana**: Seperti gula pasir, brown sugar, dan sirup jagung.
    - **Karbohidrat Kompleks**: Seperti buah-buahan, sayuran, kacang-kacangan, dan biji-bijian utuh.

    Karbohidrat kompleks lebih sehat karena dicerna lebih lambat dan membantu mengontrol kadar gula darah.

    ### Kebutuhan Karbohidrat Harian

    Idealnya, sekitar 45%–65% dari total asupan kalori harian berasal dari karbohidrat. Jumlah pastinya bervariasi berdasarkan usia, jenis kelamin, dan kondisi fisiologis seperti kehamilan atau menyusui.

    **Contoh**:
    - Laki-laki usia 19–29 tahun: 430 gram/hari
    - Perempuan usia 19–29 tahun: 360 gram/hari
    - Ibu hamil: Tambahan sekitar 40 gram/hari
    - Ibu menyusui: Tambahan sekitar 50 gram/hari

    Sumber: [Alodokter](https://www.alodokter.com/kebutuhan-karbohidrat-per-hari-dan-cara-memenuhinya)
    """)

def halaman_kalkulator():
    st.title("Kalkulator Kebutuhan Karbohidrat Harian")

    with st.form("form_kebutuhan"):
        usia = st.number_input("Usia Anda (tahun)", min_value=10, max_value=100, value=25)
        jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        status = st.selectbox("Status Fisiologis", ["Normal", "Hamil", "Menyusui"])
        submitted = st.form_submit_button("Hitung")

    if submitted:
        kebutuhan = get_kebutuhan(usia, jenis_kelamin, status)
        if kebutuhan == 0:
            st.warning("Data kebutuhan karbohidrat untuk usia tersebut tidak tersedia.")
        else:
            st.success(f"Kebutuhan karbohidrat harian Anda adalah sekitar **{kebutuhan} gram**.")

            st.markdown("""
            ### Contoh Pemenuhan Kebutuhan Karbohidrat
            Berikut beberapa contoh makanan dan kandungan karbohidratnya:

            | Makanan                   | Porsi             | Karbohidrat (gram) |
            |---------------------------|-------------------|--------------------|
            | Nasi putih                | 1 centong (100 gr)| 40                 |
            | Nasi merah                | 1 centong (100 gr)| 32.5               |
            | Oats                      | 1 mangkuk         | 54                 |
            | Pisang (besar)            | 1 buah            | 31                 |
            | Ubi rebus                 | 1 mangkuk (200 gr)| 42                 |
            | Jeruk (kecil)             | 1 buah (100 gr)   | 15.5               |
            | Apel (kecil)              | 1 buah (100 gr)   | 16                 |
            | Kacang merah              | 100 gr            | 21.5               |
            | Spageti                   | 100 gr            | 73                 |
            | Roti gandum               | 1 lembar          | 14                 |
            | Bayam                     | 100 gr            | 6                  |
            | Susu sapi                 | 1 gelas           | 8.6                |

            Sumber: [Alodokter](https://www.alodokter.com/kebutuhan-karbohidrat-per-hari-dan-cara-memenuhinya)
            """)

# Navigasi halaman
st.sidebar.title("Navigasi")
halaman = st.sidebar.radio("Pilih Halaman", ["Beranda", "Kalkulator"])

if halaman == "Beranda":
    halaman_beranda()
else:
    halaman_kalkulator()

