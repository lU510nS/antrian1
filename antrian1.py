import streamlit as st

# Judul aplikasi
st.title("Model Antrian PT. Barokah")

st.markdown("""
Aplikasi ini menghitung parameter antrian berdasarkan model **M/M/1**  
dengan asumsi:  
- Kedatangan pelanggan mengikuti distribusi **Poisson**  
- Waktu pelayanan mengikuti distribusi **Eksponensial**
""")

# Input dari user
λ = st.number_input("Rata-rata kedatangan pelanggan per jam (λ)", min_value=1.0, value=15.0)
μ = st.number_input("Rata-rata pelayanan pelanggan per jam (μ)", min_value=1.0, value=20.0)

if μ <= λ:
    st.error("Laju pelayanan (μ) harus lebih besar dari laju kedatangan (λ) agar sistem stabil.")
else:
    # Perhitungan model M/M/1
    ρ = λ / μ
    L = λ / (μ - λ)
    W = 1 / (μ - λ)
    Wq = λ / (μ * (μ - λ))

    # Tampilkan hasil
    st.subheader("Hasil Perhitungan:")
    st.write(f"Tingkat utilisasi server (ρ): {ρ:.2f} atau {ρ*100:.1f}%")
    st.write(f"Rata-rata jumlah pelanggan dalam sistem (L): {L:.2f} orang")
    st.write(f"Rata-rata waktu dalam sistem (W): {W:.2f} jam atau {W*60:.0f} menit")
    st.write(f"Rata-rata waktu menunggu dalam antrean (Wq): {Wq:.2f} jam atau {Wq*60:.0f} menit")
