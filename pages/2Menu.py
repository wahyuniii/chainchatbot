import streamlit as st
import requests
from streamlit_lottie import st_lottie


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
st.header("Hai teman-teman, Perkenalkan Aku Chainbot :wave:")

#Lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://assets10.lottiefiles.com/private_files/lf30_rg5wrsf4.json"
lottie_html = f'<div class="lottie" style="background-color: #FF000;"><lottie-player src="{lottie_url_hello}" background="transparent" speed="1" loop autoplay></lottie-player></div>'
st.markdown(lottie_html, unsafe_allow_html=True)
lottie_hello = load_lottieurl(lottie_url_hello)

st_lottie(lottie_hello, key="hello")

st.subheader("Mari kita belajar bersama mata pelajaran IPAS BAB 2 (Harmoni dalam Ekosistem)")
st.subheader ("Silahkan pilih salah satu menu dibawah ini")

st.write("---")

from streamlit_extras.switch_page_button import switch_page
import streamlit as st

# Tambahkan CSS untuk mengubah warna latar belakang tombol menjadi warna coklat pastel
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

# Tombol CP, Tujuan Pembelajaran, dan Alur Tujuan Pembelajaran
want_to_cp = st.button("CP, Tujuan Pembelajaran, ATP")
if want_to_cp:
    switch_page("CP, Tujuan Pembelajaran, ATP")

# Tombol Topik A
want_to_topikA = st.button("Topik A (Memakan dan Dimakan)")
if want_to_topikA:
    switch_page("Topik A (Memakan dan Dimakan)")

# Tombol Topik B
want_to_topikB = st.button("Topik B (Transfer Energi Antarmakhluk Hidup)")
if want_to_topikB:
    switch_page("Topik B (Transfer Energi Antarmakhluk Hidup)")

# Tombol About
want_to_about = st.button("Tentang Pengembang")
if want_to_about:
    switch_page("Tentang Pengembang")
