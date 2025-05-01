import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import requests
from PIL import Image
from PyPDF2 import PdfReader

# set page config ini diatas karena di tidak bisa membaca ketika st.text apapun itu 
# mau st.title atau st.header dll ditidak dapat membacanya maka di eror jadi saya oindahkan ke atas
st.set_page_config(page_title="Dashboard Saham TPI", layout="wide")


st.sidebar.title("📈 Dashboard Saham TISE")
st.sidebar.markdown("Selamat datang di dashboard analisis saham berbasis Streamlit.")

uploaded_file = st.sidebar.file_uploader("Upload file data (.csv)", type=["csv"])
if uploaded_file is not None:
    st.sidebar.success("📁 File berhasil diunggah!")

st.sidebar.subheader("Filter Saham")
pilih_saham = st.sidebar.selectbox("Pilih Saham:", ["BBRI", "TLKM", "BBCA", "ANTM", "GOTO"])

st.sidebar.subheader("Rentang Tahun")
tahun_awal = st.sidebar.slider("Tahun Awal", 2000, 2025, 2015)
tahun_akhir = st.sidebar.slider("Tahun Akhir", 2000, 2025, 2024)

st.sidebar.subheader("Filter Sektor")
sektor = st.sidebar.multiselect(
    "Pilih Sektor:",
    ["Energi", "Keuangan", "Kesehatan", "Konsumsi", "Teknologi", "Properti"],
    default=["Keuangan", "Teknologi"]
)

# Tautan Eksternal
st.sidebar.markdown("📎 [Lihat di Yahoo Finance](https://finance.yahoo.com)", unsafe_allow_html=True)
st.sidebar.markdown("📘 [IDX Resmi](https://www.idx.co.id)")

# Logo / Branding
st.sidebar.image("https://img.icons8.com/ios-filled/500/stocks-growth.png", width=100)


st.title("Welcome to my streamlit app")
st.text('''Perkenalkan nama saya muhammad akmal, saya sorang mahasisswa jurusan bisnis digital, ini tugas pertama saya di app streamlit''')
st.header("pendahuluan tugas")
st.subheader("bagian pertama : pengunaan element text")
st.caption("disclamer dulu ini hanya tugas, jadi kalau ada kesalahan mohon dimaafkan")
st.code('import numpy as np, pandas as pd, ploty.express as px, streamlit as st, requests')
st.latex(r'Rumus regresi sederhana: Y = a + bX')
st.markdown('contoh pengaturan tesk: **teks tebal** dan _teks miring_ serta [link](https://akmalllsaham01.streamlit.app/)')

link = 'https://webapi.bps.go.id/v1/api/list/model/data/lang/ind/domain/0000/var/2266/key/[WebAPI_KEY]'
response = requests.get(link)

#if response.status_code == 200:
    #data=response.json()
    #df=pd.DataFrame(data)
    #st.dataframe(df)
    #print(data)
    
#else:
    #st.write('codenya salah')
    
uploaded_file = st.file_uploader("silahkan pilih file", type="csv" )

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data)

else:
    st.write("data yg anda upload gagal di baca")

data_saya ={
    "nama" :['muhammad akmal', 'iqbal', 'dwi'],
    "umur" :[17, 18, 19],
    "universitas":['universitas negeri unm', 'universitas negeri unhas', 'universitas negeri uin']
}

df = pd.DataFrame(data_saya)
st.write('Tabel data saya')
st.dataframe(df)

df = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
    )  

st.write(df)

#matric

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Harga Saham", value="Rp 5.000", delta="+3%")
with col2:
    st.metric(label="Volume Dagang", value="1,2 Juta", delta="+10%")
with col3:
    st.metric(label="Perobahan Harian", value="-50", delta="-1%")

col1, col2 = st.columns(2)


df = pd.DataFrame(
    np.random.randn(30, 3),
    columns=['x', 'y', 'z']
    )  
st.line_chart(df)

df = pd.DataFrame(
    np.random.randn(30, 3),
    columns=['a', 'b', 'c']
    )  
st.area_chart(df)

df = pd.DataFrame(
    np.random.randn(30, 3),
    columns=['a', 'b', 'c']
    )  
st.bar_chart(df)


data = pd.DataFrame({
    'lat': [-6.2088, -7.2504, -6.9147],  # Jakarta, Surabaya, Bandung
    'lon': [106.8456, 112.7688, 107.6098],
})
st.write("**Lokasi Kantor Perusahaan Sekuritas**")
st.map(data)





st.title("📈 Dashboard Saham TPI 5 Tahun")

data = pd.DataFrame({
    'Tahun': [2018, 2019, 2020, 2021, 2022],
    'Harga Saham': [1500, 1700, 1300, 1900, 2100],
    'Volume': [200000, 220000, 180000, 240000, 260000]
})

fig_saham = px.line(
    data,
    x='Tahun',
    y='Harga Saham',
    markers=True,
    text='Harga Saham',
    title="📊 Tren Harga Saham TPI",
    labels={'Harga Saham': 'Harga per Lembar', 'Tahun': 'Tahun'},
    template='plotly_white'
)

fig_saham.update_traces(textposition="top center")
fig_saham.update_layout(title_x=0.5)

fig_volume = px.bar(
    data,
    x='Tahun',
    y='Volume',
    color='Tahun',
    title="📦 Volume Transaksi Tahunan",
    labels={'Volume': 'Jumlah Volume'},
    template='plotly_dark'
)

fig_volume.update_layout(title_x=0.5)

coll, col2 = st.columns(2)
with coll:
    st.plotly_chart(fig_saham, use_container_width=True)
with col2:
    st.plotly_chart(fig_volume, use_container_width=True)

st.divider()
st.caption('Dibuat dengan ❤️ menggunakan Streamlit dan Plotly')



with st.form("form_saham"):
    nama_emiten = st.text_input("Nama Emiten")
    kode_saham = st.text_input("Kode Saham (Ticker)")
    alamat = st.text_area("Alamat Perusahaan")
    sektor = st.selectbox("Sektor", ["Keuangan", "Kesehatan", "Energi", "Teknologi", "Manufaktur", "Properti"])
    harga_awal = st.number_input("Harga Awal (Rp)", min_value=0.0)
    harga_akhir = st.number_input("Harga Akhir (Rp)", min_value=0.0)
    tanggal = st.date_input("Tanggal Transaksi")
    volume = st.number_input("Volume Saham", min_value=0)
    rekomendasi = st.radio("Rekomendasi Analis", ["Buy", "Hold", "Sell"])
    catatan = st.text_area("Catatan Analis")
    rating = st.slider("Rating Saham", 1, 10)
    
    # Tambahan: Foto & Kamera
    foto_ktp = st.file_uploader("Upload foto ktp")
    foto_face = st.camera_input("Ambil foto face")

    submitted = st.form_submit_button("Kirim Data")

if submitted:
    st.success(f"Data saham *{kode_saham} - {nama_emiten}* berhasil dikirim! 📈")

    # Tampilkan foto jika ada
    if foto_ktp:
        st.image(foto_ktp, caption="Foto KTP", use_column_width=True)
    if foto_face:
        st.image(foto_face, caption="Foto face dari Kamera", use_column_width=True)


image = Image.open("Pani.jpeg")
st.image(image, caption='saham.jpg')

st.image("https://sl.bing.net/hwgoqUEezxk", caption='gambar idx', use_column_width=True)

##dari dari file lokal
#st.video("barca.mp4")
#menampilkan vidio dari url
st.video("https://www.youtube.com/watch?v=W9HuTy_bioY")

##menampilkan sound dari file lokal
#st.audio("stecu.mp3")
#menampilak vidio dari url
st.audio("https://soundcloud.com/soundhelix/soundhelix-song-1?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")

uploaded_file = st.file_uploader("silahkan pilih file PDF or Excel", type=["pdf", "xlsx"])

if uploaded_file is not None:
    st.write("file berhasil di upload")
    st.write(uploaded_file.name)
    st.download_button("download", uploaded_file)   
    

# Menampilkan PDF
uploaded_pdf = st.file_uploader("Pilih file PDF", type=["pdf"])

if uploaded_pdf is not None:
    reader = PdfReader(uploaded_pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    st.write(text)


# Menampilkan HTML langsung
html_code = """
<h3> saya adalah seorang mahasiswa</h3>
<p>saya sedang belajar streamlit</p>
"""
st.markdown(html_code, unsafe_allow_html=True)



# Membuat dua kolom
col1, col2 = st.columns(2)

# Menampilkan konten di kolom pertama
with col1:
    st.header("Saham A")
    st.write("Ini adalah saham backdoor")
    st.button("Beli Saham A")

# Menampilkan konten di kolom kedua
with col2:
    st.header("Saham B")
    st.write("Ini adalah saham yg ownwenya kurang bagus")
    st.button("Beli Saham B")

import streamlit as st

with st.expander("Klik untuk melihat detail saham"):
    st.write("Berikut ini adalah informasi tambahan tentang saham pilihan Anda.")
    if st.button("Mau lihat charnya?"):
        st.markdown("[klik here](https://www.msn.com/id-id/ekonomi/daftarpantau?id=bn91jc&tab=Recent&ocid=winp2fptaskbarhover&cvid=324c1ec44ef840c8926e4d96400acbf5&ei=2)",unsafe_allow_html=True)


