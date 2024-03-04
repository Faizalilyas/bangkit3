import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/Faizalilyas/DataAnalisDicoding-/main/bike.csv")  

def plot_bike_rental_by_hour(bike_df):
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x=bike_df['hour'],
        y=bike_df['count_cr_hour'],
        estimator=sum,
        errorbar=None,
        palette="viridis"
    )
    #plt.title("Pola Peminjaman Sepeda Berdasarkan Jam", fontsize=15)
    plt.xlabel("Jam", fontsize=12)
    plt.ylabel("Jumlah Peminjaman", fontsize=12)
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())

    # Paragraf deskripsi
    st.write("""Terdapat pola harian yang jelas dalam penggunaan sistem peminjaman 
    sepeda dalam penggunaan sistem peminjaman sepeda, terlihat pola yang konsisten setiap harinya. 
    Pola ini memiliki dua puncak di pagi dan sore hari. 
    Jam-jam sibuk dan jam-jam sepi menunjukkan perbedaan pola yang signifikan. 
    Faktor yang mungkin memengaruhi pola ini termasuk komuter, aktivitas, cuaca, dan ketersediaan sepeda.""")

    # Subjudul untuk rekomendasi
    st.subheader("Rekomendasi:")

    # List rekomendasi
    st.write("""
    - Meningkatkan jumlah sepeda di stasiun peminjaman untuk mengurangi antrian di jam-jam sibuk.
    - Mendorong penggunaan sepeda di luar jam-jam sibuk dengan menawarkan program dan promosi.
    - Memantau tren dan menyesuaikan strategi sesuai kebutuhan.""")


def plot_bike_rental_by_month(bike_df):
    bike_df['date'] = pd.to_datetime(bike_df['date'])  
    date_month_df = bike_df.resample(rule='M', on='date').agg({
        "count_cr_day": "sum"
    })
    date_month_df.index = date_month_df.index.strftime('%Y-%m')
    date_month_df = date_month_df.reset_index()

    plt.figure(figsize=(10, 5))
    plt.plot(date_month_df["date"], date_month_df["count_cr_day"], marker='o', linewidth=2, color="#72BCD4")
    #plt.title("Perkembangan Sistem Peminjaman Sepeda (2011-2012)", fontsize=20, pad=20)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt.gcf()) 

    st.write("""Terjadi penurunan penggunaan sistem peminjaman sepeda dari tahun 2011 ke 2012. 
    Fluktuasi musiman yang signifikan juga terlihat, dengan puncak penggunaan di musim panas 
    dan terendah di musim dingin. Faktor-faktor yang mungkin memengaruhi tren ini termasuk musim, 
    harga, ketersediaan infrastruktur bersepeda, dan faktor lain seperti acara publik, promosi, 
    dan tren gaya hidup.""")

    # Subjudul untuk rekomendasi
    st.subheader("Rekomendasi:")

    # List rekomendasi
    st.write("""
    - Melakukan analisis lebih lanjut untuk mengidentifikasi faktor-faktor yang paling signifikan dalam memengaruhi penggunaan sepeda.
    - Meningkatkan infrastruktur bersepeda untuk membuat penggunaan sepeda lebih aman dan nyaman.
    - Menawarkan program dan promosi untuk mendorong penggunaan sepeda, terutama di luar musim panas.
    - Memantau tren dan menyesuaikan strategi sesuai kebutuhan..""") 

def plot_bike_rental_by_workday(bike_df):
    rent_workday = bike_df.groupby(by='workingday_day').agg({
        "count_cr_day": ["sum", "mean"]
    }).sort_values(by=("count_cr_day", "sum"), ascending=False).reset_index()

    plt.figure(figsize=(8, 6))
    sns.barplot(x=("workingday_day"), y=("count_cr_day", "sum"), data=rent_workday)
    #plt.title("Total Peminjaman Sepeda Berdasarkan Hari Kerja", fontsize=15)
    plt.xlabel("Hari Kerja", fontsize=12)
    plt.ylabel("Total Peminjaman", fontsize=12)
    plt.xticks(rotation=0)
    plt.tight_layout()
    st.pyplot(plt.gcf())

    st.write("""Terdapat perbedaan yang signifikan dalam tingkat peminjaman sepeda antara hari kerja 
    dan akhir pekan. Pada hari kerja tingkat peminjaman lebih tinggi dengan puncak peminjaman 
    terjadi pada jam 08:00-09:00 dan 17:00-18:00""")

    # Subjudul untuk rekomendasi
    st.subheader("Rekomendasi:")

    # List rekomendasi
    st.write("""
    - Meningkatkan persediaan sepeda di stasiun peminjaman pada hari kerja dan jam-jam sibuk
    - Mendorong penggunaan sepeda di luar jam-jam sibuk melalui program diskon atau insentif untuk mengurangi kepadatan pada jam sibuk.
    - Menyesuaikan jadwal layanan, seperti peningkatan frekuensi pengiriman sepeda pada jam-jam sibuk, untuk memenuhi kebutuhan pengguna
    - Terus memantau dan menganalisis tren peminjaman sepeda untuk memahami strategi operasional secara efektif.""")   

def plot_bike_rental_by_season(bike_df):
    by_season = bike_df.groupby("season_day").count_cr_day.sum().sort_values(ascending=False).reset_index()

    colors = ['#FFBE98', '#FEECE2', '#F7DED0', '#E2BFB3']

    plt.figure(figsize=(10, 5))
    sns.barplot(
        y="count_cr_day",
        x="season_day",
        data=by_season.sort_values(by="count_cr_day", ascending=False),
        palette=colors
    )
    #plt.title("Peminjaman Sepeda Berdasarkan Musim", loc="center", fontsize=15)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='x', labelsize=12)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.tight_layout()
    st.pyplot(plt.gcf())  

    st.write("""Terdapat pola musiman yang jelas dalam penggunaan sistem peminjaman sepeda. 
    Puncak penggunaan terjadi di musim panas (Juni-Agustus). 
    Penurunan penggunaan terjadi di musim dingin (Desember-Februari).""")

    # Subjudul untuk rekomendasi
    st.subheader("Rekomendasi:")

    # List rekomendasi
    st.write("""
    - Meningkatkan infrastruktur bersepeda untuk membuat penggunaan sepeda lebih aman dan nyaman.
    - Menawarkan program dan promosi untuk mendorong penggunaan sepeda di luar musim panas.
    - Memantau tren dan menyesuaikan strategi sesuai kebutuhan.""")

def main():
    st.title("Dashboard Peminjaman Sepeda :sparkles:")
    bike_df = load_data()
    st.sidebar.image("https://raw.githubusercontent.com/Faizalilyas/Praktikum-Keamanan-Informasi-1/main/pngwing.com.png", use_column_width=True)
    tab = st.sidebar.radio("Tab Analisa", ["Peminjaman per Jam", "Perkembangan Sistem", "Peminjaman per Hari Kerja", "Peminjaman per Musim"])

    if tab == "Peminjaman per Jam":
        st.header("Analisa pola peminjaman sepeda berubah sepanjang hari berdasarkan jam")
        plot_bike_rental_by_hour(bike_df)
    elif tab == "Perkembangan Sistem":
        st.header("Analisia tren penggunaan sistem peminjaman sepeda (2011-2012)")
        plot_bike_rental_by_month(bike_df)
    elif tab == "Peminjaman per Hari Kerja":
        st.header("Analisa perbedaan pola peminjaman sepeda antara hari-hari kerja dan akhir pekan")
        plot_bike_rental_by_workday(bike_df)
    elif tab == "Peminjaman per Musim":
        st.header("Analisa peminjaman sepeda berdasarkan musim")
        plot_bike_rental_by_season(bike_df)

if __name__ == "__main__":
    main()
