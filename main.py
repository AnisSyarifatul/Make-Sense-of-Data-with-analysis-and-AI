import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("dataset.csv")

X = data[["ipk", "kehadiran"]]
y = data["status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

prediksi = model.predict(X_test)
akurasi = accuracy_score(y_test, prediksi)

print("=== PREDIKSI KELULUSAN ===")
print(f"Akurasi model: {akurasi:.2%}")

ipk = float(input("Masukkan IPK: "))
kehadiran = float(input("Masukkan kehadiran (%): "))

data_baru = pd.DataFrame(
    [[ipk, kehadiran]],
    columns=["ipk", "kehadiran"]
)

hasil = model.predict(data_baru)[0]
print("Hasil prediksi:", hasil)