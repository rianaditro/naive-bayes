import streamlit as st

from model.predictor import get_prediction


st.write("Naive Bayes Classifier")

# st.form()

with st.form("user_input"):
    st.write("INPUT DATA")
    fakultas = st.selectbox("FAKULTAS", [
    'Ekonomi', 'Hukum', 'Ilmu Komputer', 
    'Ilmu Sosial Dan Ilmu Politik', 'Kedokteran', 
    'Keguruan Dan Ilmu Pendidikan', 'Kesehatan Masyarakat', 
    'Matematika Dan Ilmu Pengetahuan Alam', 'Pertanian', 'Teknik'
    ])

    jns_kelamin = st.selectbox("JENIS KELAMIN", ['Laki-Laki', 'Perempuan'])

    eks_gaji = st.selectbox("EKSPEKTASI GAJI", ['Diatas 4 Juta', 'Dibawah 4 Juta'])

    lokasi = st.selectbox("LOKASI KERJA", ['Dalam Daerah Dan Sekitarnya', 'Luar Daerah'])

    submit = st.form_submit_button("Submit")

    user_input = {
        'FAKULTAS': fakultas,
        'JENIS KELAMIN': jns_kelamin,
        'EKSPEKTASI GAJI': eks_gaji,
        'LOKASI KERJA': lokasi
    }

    if submit:
        prediction = get_prediction(user_input)
        st.write(prediction)
