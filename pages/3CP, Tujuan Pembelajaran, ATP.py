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
st.subheader("Berikut merupakan Capaian Pembelajaran (CP), Tujuan Pembelajaran, dan Alur Tujuan Pembelajaran (ATP) pada materi ini")
st.write("##")

# Menambahkan CSS untuk mengatur warna latar belakang tab menjadi biru
st.markdown(
    """
    <style>
   .streamlit-tabs.stHorizontal > .tabs {
        background-color: blue;
    }
    .streamlit-tabs.stHorizontal > .tabs .tab[data-baseweb="tab"] {
        background-color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs(["Capaian Pembelajaran (CP)", "Tujuan Pembelajaran", " ALur Tujuan Pembelajaran (ATP)"])

with tab1:
   st.header("Capaian Pembelajaran (CP)")
   st.image("https://64.media.tumblr.com/0e7f02c2b423e81c9fd30bf10c10c5db/36ed59391e9ac7b6-2d/s1280x1920/f0c34240ccd2a6a3af36053672e9475d98ca4c0b.pnj")
with tab2:
   st.header("Tujuan Pembelajaran")
   st.image("https://64.media.tumblr.com/7839e4cf848ca78314c3b929f7c999c5/828bf371ae23f282-80/s1280x1920/03bd87b2041fed6e9b861904243df29745a386c1.pnj")

with tab3:
   st.header("Alur Tujuan Pembelajaran(ATP)")
   st.image("https://64.media.tumblr.com/52ee4698a25f5554c2f74b31bf5bb072/6bf41baa76eb041c-e9/s1280x1920/2cbdc26b56c2ce35cb13916db4c6d855a5866e45.pnj")

st.write("---")


# Tulis
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

from streamlit_extras.switch_page_button import switch_page

col1, col2= st.columns(2)
with col1:
   want_to_menu = st.button("\u25C0   Menu")
if want_to_menu:
   switch_page("Menu")
 
with col2:
   want_to_pemb = st.button("Next   \u25B6   Topik A (Memakan dan Dimakan)")
if want_to_pemb:
   switch_page("Topik A (Memakan dan Dimakan)")
