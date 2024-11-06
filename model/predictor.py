import pickle
import pandas as pd
import sklearn

# User Input
FAKULTAS = [
    'Ekonomi', 'Hukum', 'Ilmu Komputer', 
    'Ilmu Sosial Dan Ilmu Politik', 'Kedokteran', 
    'Keguruan Dan Ilmu Pendidikan', 'Kesehatan Masyarakat', 
    'Matematika Dan Ilmu Pengetahuan Alam', 'Pertanian', 'Teknik']
JNS_KELAMIN = ['Laki-Laki', 'Perempuan']
EKS_GAJI = ['Diatas 4 Juta', 'Dibawah 4 Juta']
LOKASI = ['Dalam Daerah Dan Sekitarnya', 'Luar Daerah']

# Prediction result
MASA_TUNGGU = ["3 bulan atau kurang", "3 bulan lebih"]

# Mapping key to constant variable
mapping_dict = {
    'FAKULTAS': FAKULTAS,
    'JENIS KELAMIN': JNS_KELAMIN,
    'EKSPEKTASI GAJI': EKS_GAJI,
    'LOKASI KERJA': LOKASI
}


# Load model
with open('model/naive_bayes_modeling.pkl', 'rb') as f:
    model = pickle.load(f)


def get_prediction(user_input: dict):
    # Replace user_input to store index instead of string
    for key, value in user_input.items():
        user_input[key] = mapping_dict[key].index(value)

    user_input = pd.DataFrame(user_input, index=[0])
    predicted_int = model.predict(user_input)[0]

    return MASA_TUNGGU[predicted_int]