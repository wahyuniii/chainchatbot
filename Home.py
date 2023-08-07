import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_extras.stateful_button import button


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
st.title("HALO DENGAN CHAINBOT DISINI :wave:")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://assets6.lottiefiles.com/packages/lf20_gaj4x0te.json"
lottie_html = f'<div class="lottie" style="background-color: #FF000;"><lottie-player src="{lottie_url_hello}" background="transparent" speed="1" loop autoplay></lottie-player></div>'
st.markdown(lottie_html, unsafe_allow_html=True)
lottie_hello = load_lottieurl(lottie_url_hello)

st_lottie(lottie_hello, key="hello")

# Menambahkan CSS untuk mengatur teks menjadi rata tengah, besar, dan latar belakang teks
import streamlit as st


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

st.markdown(
    """
    <style>
    .my-text {
        font-size: 16px;
    }
    .stTextInput input {
        background-color: #FFAE69;
    }
    .stTextInput label {
        font-size: 20px;
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="my-text">Untuk mulai belajar, tuliskan Namamu pada kolom dibawah ini kemudian tekan Submit  \u2193  \u2193  \u2193</p>', unsafe_allow_html=True)

my_input = st.text_input(st.session_state["my_input"])

submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.markdown(f"Selamat datang **{my_input}**, Chainbot siap menemani belajarmu")
    st.write("Sebelum memulai belajar, bacalah petunjuk penggunaan Chainbot terlebih dahulu ya")
    st.image("https://64.media.tumblr.com/1fed3438310f3293e0b083f06b84a305/b180ac5da060bf4a-03/s400x600/489aec1befbc6cd2e44471e2746f2071531f6e9c.pnj")

# Tulis