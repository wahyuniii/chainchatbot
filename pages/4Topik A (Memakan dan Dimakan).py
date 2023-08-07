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
st.title("TOPIK A (MEMAKAN DAN DIMAKAN)")
st.write("---")

tab1, tab2 = st.tabs(["MATERI TOPIK A", "KUIS TOPIK A"])

with tab1:
    st.header("Rantai Makanan dan Jaring-jaring Makanan")
    st.write("---")
    st.image("https://64.media.tumblr.com/651ca81f31a21c54020ff36fe178d011/0e1e99238729638b-b1/s640x960/dd442b3ca8f38f9e1528cd445b096cdc1601e512.pnj")
    st.subheader("Apa maksud dari gambar di atas?")
    st.write("Semua makhluk hidup membutuhkan energi untuk tetap hidup. Manusia mendapatkan makanan dengan mengolah bahan-bahan makanan yang ada di alam. Lalu, bagaimana dengan hewan dan tumbuhan? Bagaimana mereka mendapatkan makanan sebagai sumber energi?")
    st.write("Untuk menjawab pertanyaan tersebut, mari pelajari bersama mengenai rantai makanan dan jaring-jaring makanan di bawah ini!")
    submit = st.button("Rantai makanan dan jaring-jaring makanan?  \u2193")
    if submit:
        st.write("Dalam sebuah ekosistem, makhluk hidup bisa menjadi sumber energi untuk makhluk hidup lainnya. Sumber energi berarti sumber makanan. Hubungan makan dan dimakan antarmakhluk hidup untuk memperoleh energi dapat membentuk rantai makanan dan jaring-jaring makanan.")
        tab3, tab4 = st.tabs(["Rantai Makanan", "Jaring-jaring Makanan"])
        with tab3:
            st.write("Rantai makanan adalah peristiwa makan dan dimakan antara mahluk hidup dengan urutan tertentu.")
            st.write("Perhatikan rantai makanan berikut!")
            st.image('https://64.media.tumblr.com/4f1bb28938a8cdb90a5b337d764d7105/6b9b425866057822-ed/s540x810/6122829c36ae021fccab313c574d902cb6efac4b.pnj')
            st.write("Gambar di atas merupakan contoh yang menunjukkan hubungan makan dan dimakan antarmakhluk hidup. Sederhananya, kita bisa menggambarkan hubungan ini dalam bentuk rantai makanan seperti berikut.")
            st.write("Rumput → Belalang → Tikus → Ular → Elang → Jamur ")
            st.write("Pada rantai makanan diatas, kita bisa melihat alur makan sebagai berikut:")
            st.write("a. Rumput sebagai produsen")
            st.write("b. Belalang sebagai konsumen tingkat 1")
            st.write("c. Tikus sebagai konsumen tingkat 2")
            st.write("d. Ular sebagai konsumen tingkat 3")
            st.write("e. Burung elang sebagai konsumen tingkat 4")
            st.write("f. Jamur sebagai dekomposer")
                    
            with st.expander("Contoh rantai makanan"):
                st.write("Berikut beberapa contoh rantai makanan")
                st.image('https://64.media.tumblr.com/2b6bb79a18e5df072e88a650add260f9/f566c5f256d57d2b-93/s540x810/ff0f792dee6dd495ad5f3a68de0f247afda58bbd.pnj', 'Rantai makanan di laut')
                st.image('https://64.media.tumblr.com/872d9db9a3bece93ae2e4dce2d4c3b10/2b3ef267959d7dde-2f/s250x400/f6c7d168985db994b0af04d8af36e7bbe8b0f828.pnj', 'Rantai makanan yang pendek')
                                
        with tab4:
            st.write("Jaring-jaring makanan adalah sekumpulan rantai makanan yang saling berhubungan. Jaring-jaring makanan dibentuk dari beberapa rantai makanan.")
            st.image('https://2.bp.blogspot.com/-FNFZfpQVBPw/W8LX_k3YU7I/AAAAAAAAQng/2p5590igcRMv3xE_KNfqCKQkqd1TDJNlgCLcBGAs/s1600/gurun.jpg', 'contoh jaring-jaring makanan')
            st.write("Umumnya, di dalam suatu ekosistem tidak hanya terdiri atas satu rantai makanan. Hal ini karena konsumen tingkat 1 dapat memakan berbagai produsen. Satu jenis produsen juga dapat dimakan oleh berbagai macam konsumen tingkat 1. Begitu pula dengan konsumen tingkat 2 dan 3 yang bisa memakan berbagai jenis hewan. Karenanya, pada suatu ekosistem hubungan makan dan dimakan digambarkan dengan jaring-jaring makanan yang merupakan kumpulan dari rantai makanan.")
            
            
        st.write("---")
        st.write("---")
        st.write("Untuk lebih memahami mengenai rantai makanan dan jaring-jaring makanan, Mari amati video berikut ini!")
        st.video("https://youtube.com/watch?v=Hlloahtfe7o&feature=share")
        st.write("---")
        st.write("Nah setelah kalian mengamati video pembelajaran tersebut, tentu sekarang kalian sudah paham tentang Rantai makanan dan Jaring-jaring makanan")
        st.write("Untuk mengukur pemahaman kalian, mari kerjakan kuis dengan menekan tombol KUIS TOPIK A pada bagian atas")
        
# KUIS
with tab2:
    def generate_questions():
        questions = [
            {
                'type': 'text',
                'question': 'Rantai makanan adalah hubungan makan dan dimakan dalam suatu ekosistem sebagai upaya untuk mendapatkan ....',
                'options': ['A. Gaya', 'B. Gerak', 'C. Energi', 'D. Usaha'],
                'answer': 'C. Energi'
            },
            {
                'type': 'image',
                'question': 'Perhatikan gambar rantai makanan berikut!',
                'image': 'https://imgix2.ruangguru.com/assets/miscellaneous/png_u2vbwu_6032.png',
                'question': 'Makhluk hidup yang berperan sebagai konsumen tingkat 2 pada rantai makan di bawah ini yaitu ....',
                'options': ['A. Belalang', 'B. Burung Elang', 'C. Padi', 'D. Katak'],
                'answer': 'D. Katak'
            },
            {
                'type': 'image',
                'question': 'Perhatikan pengelompokkan hewan berikut!',
                'image': 'https://64.media.tumblr.com/70d489cc8c8ae75916bb8655543403e4/55ab4aa3bc060fdb-75/s500x750/6c6f08191a897f87c2c6da8c594682f206946a17.pnj',
                'options': ['A. 1 dan 2', 'B. 2 dan 3', 'C. 3 dan 4', 'D. 1 dan 4'],
                'answer': 'B. 2 dan 3'
            },
            {
                'type': 'text',
                'question': 'Makhluk hidup yang dapat memproduksi makanannya sendiri disebut ....',
                'options': ['A. Produsen', 'B. Konsumen tingkat 1', 'C. Konsumen tingkat 2', 'D. Dekomposer'],
                'answer': 'A. Produsen'
            },
            {
                'type': 'image',
                'question': 'Makhluk hidup yang tepat untuk mengisi rantai makanan di bawah ini adalah ....',
                'image': 'https://64.media.tumblr.com/458d758d25002bc1baf1ae80e3ae654d/79734ff208408ba5-76/s1280x1920/e73e0db641d4822167dab32674a6d6a6d817fda3.pnj',
                'options': ['A. Ikan teri', 'B. Ikan besar', 'C. Singa laut', 'D. Paus orca'],
                'answer': 'B. Ikan besar'
            },
            {
                'type': 'image',
                'question': 'Perhatikan rantai makan berikut!',
                'image': 'https://64.media.tumblr.com/998a7a135c261c4ecb92421cbcf23c63/b3a346b4769bc241-58/s500x750/9c87d79ee567b664af11c5dcff1ddb084a9c6935.pnj',
                'options': ['A. Kupu-kupu merupakan puncak rantai makanan', 'B. Ular berperan sebagai pengurai', 'C. Katak mendapat energi dari ular', 'D. Bunga dapat berfotosintesis'],
                'answer': 'D. Bunga dapat berfotosintesis'
            },
            {
                'type': 'text',
                'question': 'Makhluk hidup yang bertugas menguraikan senyawa organik (bangkai, daun busuk, dan sebagainya) menjadi nutrisi yang tersimpan dalam tanah disebut ....',
                'options': ['A. Predator', 'B. Produsen', 'C. Dekomposer', 'D. Konsumen'],
                'answer': 'C. Dekomposer'
            },
            {
                'type': 'image',
                'question': 'Pernyataan berikut yang benar terkait jaring-jaring makanan berikut adalah ....',
                'image': 'https://64.media.tumblr.com/bccc843de5e622477a542bf68b6ed9c5/fb5377e50b8afd60-e3/s1280x1920/8a06b0c26599a059da36d842d32b256622478cf9.jpg',
                'options': ['A. Serigala mendapatkan energi dari tikus', 'B. Rumput mendapatkan energi dari kelinci', 'C. Burung hantu mendapatkan energi dari elang', 'D. Ular mendapatkan energi dari elang'],
                'answer': 'A. Serigala mendapatkan energi dari tikus'
            },
            {
                'type': 'text',
                'question': 'Pada ekosistem laut yang berperan sebagai produsen adalah ....',
                'options': ['A. Fitoplankton', 'B. Padi', 'C. Cacing', 'D. Ikan kecil'],
                'answer': 'A. Fitoplankton'
            },
            {
                'type': 'text',
                'question': 'Budi melakukan percobaan dengan memasukkan sampah organik ke dalam tanah. Budi membuat dua lubang di dalam tanah. Sampah pada lubang pertama langsung dimasukkan kedalam lubang, sedangkan sampah pada lubang kedua dibungkus plastik terlebih dahulu baru dikubur dalam tanah. Setelah beberapa minggu, kedua lubang dibuka. Sampah yang dikubur menggunakan plastik masih utuh, dan sampah yang tidak dibungkus plastik sudah menyatu dengan tanah. Percobaan yang dilakukan Budi membuktikan bahwa ....',
                'options': ['A. Terdapat produsen dalam tanah', 'B. Terdapat predator dalam tanah', 'C. Terdapat dekomposer dalam tanah', 'D. Terdapat konsumen dalam tanah'],
                'answer': 'C. Terdapat dekomposer dalam tanah'
            },
        ]
        return questions

    def display_question(question):
        if question['type'] == 'text':
            st.write('**Pertanyaan:**', question['question'])
            selected_option = st.radio('Pilih jawaban Anda:', question['options'])
        elif question['type'] == 'image':
            st.write('**Pertanyaan:**', question['question'])
            st.image(question['image'], use_column_width=True)
            selected_option = st.radio('Pilih jawaban Anda:', question['options'])
        else:
            pass
        return selected_option

    def main():
        st.title('Kuis Topik A- Makan dan Dimakan')
        st.write('Jawablah pertanyaan-pertanyaan berikut!')
        
        questions = generate_questions()
        num_questions = len(questions)
        current_question = 0
        score = 0

        if 'current_question' in st.session_state:
            current_question = st.session_state.current_question
        if 'score' in st.session_state:
            score = st.session_state.score

        if current_question < num_questions:
            selected_option = display_question(questions[current_question])
            st.write('---')
            if st.button('Next', key='next_button', help='Jawaban Anda akan dikunci saat tombol Next ditekan'):
                if selected_option == questions[current_question]['answer']:
                    score += 1
                current_question += 1
        else:
            st.write('Anda telah menjawab semua pertanyaan.')
            st.write('Skor akhir Anda:', score, '/', num_questions)

        st.session_state.current_question = current_question
        st.session_state.score = score

    if __name__ == '__main__':
        main()


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
st.write("---")
st.write("---")


from streamlit_extras.switch_page_button import switch_page

col1, col2= st.columns(2)
with col1:
   want_to_menu = st.button("\u25C0   Menu")
if want_to_menu:
   switch_page("Menu")
 
with col2:
   want_to_pemb = st.button("Next   \u25B6   Topik B (Transfer Energi Antarmakhluk Hidup)")
if want_to_pemb:
   switch_page("Topik B (Transfer Energi Antarmakhluk Hidup)")
