import pandas as pd

# Crear un dataset de ejemplo con características típicas del dataset de phishing
data = {
    "url_length": [54, 120, 35, 88, 102, 76, 43, 95, 66, 140],
    "num_subdirs": [2, 8, 1, 5, 7, 3, 2, 6, 4, 9],
    "has_at_symbol": [0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
    "has_https": [1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
    "num_redirects": [0, 3, 0, 1, 4, 0, 0, 2, 1, 5],
    "class": [0, 1, 0, 1, 1, 0, 0, 1, 0, 1]  # 0=Legítima, 1=Phishing
}

df_sample = pd.DataFrame(data)

# Guardar en CSV
csv_path = "data/phishing_sample.csv"
df_sample.to_csv(csv_path, index=False)

csv_path