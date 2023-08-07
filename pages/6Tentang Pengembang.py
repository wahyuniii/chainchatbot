import streamlit as st

# Menghilangkan tombol Menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Mengganti Background dengan gambar
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://64.media.tumblr.com/c4c1bd94c65785b4a514ed9daf4e52ba/15b0e93ac3051dd5-a4/s500x750/f29a79e3543c6e729b4e8a3155dc024bf8fb8062.pnj");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba{0, 0, 0, 0};
}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stSidebar"] {
background-image: url("https://64.media.tumblr.com/152064486152a5cfc2d8d496d065bf18/8fa834b135127abc-c5/s2048x3072/51987f8137cc4a912da3c6e178e72578ac38c801.pnj");
background-size: cover;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Mulai Title
st.title("Tentang Pengembang")
st.write("---")

tab1, tab2 = st.tabs(["Pengembang", "Dosen Pembimbing"])

with tab1:
    st.image("https://64.media.tumblr.com/71cc949c33c2a11f8ebfeec4da8ed25f/8668cd133f446a1c-7e/s1280x1920/26ebef31acf2b00120788f09d4f749628dd4d867.pnj", width=200)

    st.write("---")
    st.write("Nama: Wahyuni")
    st.write("Alamat: Cilacap, Indonesia")
    st.write("Instansi: Universitas Negeri Semarang")
    st.write("Fakultas: Ilmu Pendidikan")
    st.write("Jurusan: Pendidikan Guru Sekolah Dasar")
    
with tab2:
    st.image("https://simpeg.unnes.ac.id/index.php/simpeg_portofolio/load_photo/198312172009122003")
    st.write("Nama: Ibu Desi Wulandari, S.Pd., M.Pd.")
    st.write("NIP: 198312172009122003")
    st.write("Jabatan: Lektor Universitas Negeri Semarang")

st.write("---")
st.write("---")
st.write("Untuk saran dan masukan hub: 085758447988")


#Ganti Page Berdampingan
st.markdown(
    """
    <style>
    .stButton button {
        font-size: 18px;
        background-color: #ff8c00; /* Ubah dengan kode warna coklat pastel yang diinginkan */
        color: white;
        width:100%
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("---")

from streamlit_extras.switch_page_button import switch_page

want_to_menu = st.button("\u25C0   Menu")
if want_to_menu:
   switch_page("Menu")



