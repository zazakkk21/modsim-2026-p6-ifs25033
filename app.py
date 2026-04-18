import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simulasi Pembagian Lembar Jawaban (DES)")

# ==========================
# INPUT
# ==========================
N = st.number_input("Jumlah Mahasiswa", min_value=1, value=30)
seed = st.number_input("Random Seed", value=42)

if st.button("Jalankan Simulasi"):

    np.random.seed(seed)

    # ==========================
    # GENERATE SERVICE TIME
    # ==========================
    service_time = np.random.uniform(1, 3, N)

    start_time = np.zeros(N)
    finish_time = np.zeros(N)
    waiting_time = np.zeros(N)

    # ==========================
    # SIMULASI ANTRIAN
    # ==========================
    for i in range(N):
        if i == 0:
            start_time[i] = 0
        else:
            start_time[i] = finish_time[i-1]

        finish_time[i] = start_time[i] + service_time[i]
        waiting_time[i] = start_time[i]

    total_time = finish_time[-1]
    avg_waiting = np.mean(waiting_time)
    utilization = np.sum(service_time) / total_time

    # ==========================
    # OUTPUT METRICS
    # ==========================
    st.subheader("Hasil Simulasi")
    st.write(f"Total Waktu: {total_time:.2f} menit")
    st.write(f"Rata-rata Waktu Tunggu: {avg_waiting:.2f} menit")
    st.write(f"Utilisasi Meja: {utilization*100:.2f}%")

    # ==========================
    # DATAFRAME
    # ==========================
    df = pd.DataFrame({
        "Mahasiswa": np.arange(1, N+1),
        "Service Time": service_time,
        "Start Time": start_time,
        "Finish Time": finish_time,
        "Waiting Time": waiting_time
    })

    st.subheader("Tabel Simulasi")
    st.dataframe(df)

    # ==========================
    # GRAFIK
    # ==========================
    st.subheader("Grafik Waktu Tunggu")

    plt.figure()
    plt.plot(df["Mahasiswa"], df["Waiting Time"])
    plt.xlabel("Mahasiswa")
    plt.ylabel("Waktu Tunggu")
    plt.title("Waktu Tunggu per Mahasiswa")

    st.pyplot(plt)

    # ==========================
    # HISTOGRAM SERVICE TIME
    # ==========================
    st.subheader("Distribusi Waktu Pelayanan")

    plt.figure()
    plt.hist(service_time)
    plt.xlabel("Service Time")
    plt.ylabel("Frekuensi")

    st.pyplot(plt)