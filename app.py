from flask import Flask, request, render_template
app = Flask(__name__)

# Modul Basis Pengetahuan

# Fakta-fakta
jenis_ikan = ["lele", "gurame", "nila", "mas", "patin", "bawal", "cupang", "guppy", "mujair", "tawes", "belanak", "sepat siam", "gabus"]
umur_ikan = ["burayak (0-5 hari)", "juvenile (6-15 hari)", "dewasa (16-30 hari)", "tua (31 hari ke atas)"]
pakan_ikan = ["pelet", "cacing", "pur", "udang", "kutu air"]

# Aturan-aturan
aturan = {
    "lele": {"burayak (0-5 hari)": "pelet", "juvenile (6-15 hari)": "pelet", "dewasa (16-30 hari)": "pelet", "tua (31 hari ke atas)": "pelet"},
    "gurame": {"burayak (0-5 hari)": "cacing", "juvenile (6-15 hari)": "cacing", "dewasa (16-30 hari)": "pur", "tua (31 hari ke atas)": "pur"},
    "nila": {"burayak (0-5 hari)": "pelet", "juvenile (6-15 hari)": "pelet", "dewasa (16-30 hari)": "pur", "tua (31 hari ke atas)": "pur"},
    "mas": {"burayak (0-5 hari)": "pelet", "juvenile (6-15 hari)": "pelet", "dewasa (16-30 hari)": "pur", "tua (31 hari ke atas)": "pur"},
    "patin": {"burayak (0-5 hari)": "pelet", "juvenile (6-15 hari)": "udang", "dewasa (16-30 hari)": "udang", "tua (31 hari ke atas)": "udang"},
    "bawal": {"burayak (0-5 hari)": "pelet", "juvenile (6-15 hari)": "udang", "dewasa (16-30 hari)": "udang", "tua (31 hari ke atas)": "udang"},
    "cupang": {"burayak (0-5 hari)": "kutu air", "juvenile (6-15 hari)": "kutu air", "dewasa (16-30 hari)": "kutu air", "tua (31 hari ke atas)": "kutu air"},
    "guppy": {"burayak (0-5 hari)": "kutu air", "juvenile (6-15 hari)": "kutu air", "dewasa (16-30 hari)": "kutu air", "tua (31 hari ke atas)": "kutu air"},
    "mujair": {"burayak (0-5 hari)": "pelet", "juvenile (6-15 hari)": "pelet", "dewasa (16-30 hari)": "pelet", "tua (31 hari ke atas)": "pelet"},
    "tawes": {"burayak (0-5 hari)": "pelet", "juvenile (6-15 hari)": "pelet", "dewasa (16-30 hari)": "pelet", "tua (31 hari ke atas)": "pelet"},
    "belanak": {"burayak (0-5 hari)": "pelet", "juvenile (6-15 hari)": "pelet", "dewasa (16-30 hari)": "pelet", "tua (31 hari ke atas)": "pelet"},
    "sepat siam": {"burayak (0-5 hari)": "pelet", "juvenile (6-15 hari)": "pelet", "dewasa (16-30 hari)": "pelet", "tua (31 hari ke atas)": "pelet"},
    "gabus": {"burayak (0-5 hari)": "pelet", "juvenile (6-15 hari)": "pelet", "dewasa (16-30 hari)": "pelet", "tua (31 hari ke atas)": "pelet"}
}


# Modul Mesin Inferensi

def backward_chaining(jenis_ikan, umur_ikan):
    """
    Fungsi untuk menentukan pakan ikan yang tepat berdasarkan jenis dan umur ikan.

    Args:
        jenis_ikan (str): Jenis ikan.
        umur_ikan (str): Umur ikan.

    Returns:
        str: Jenis pakan ikan yang tepat.
    """

    # Mencocokkan fakta dengan aturan
    return aturan.get(jenis_ikan, {}).get(umur_ikan, "Tidak ditemukan aturan yang sesuai")

@app.route('/', methods=['GET', 'POST'])
def index():
    pakan_ikan = ''
    rule = ''
    if request.method == 'POST':
        jenis_ikan = request.form.get('jenis_ikan')
        umur_ikan = request.form.get('umur_ikan')
        pakan_ikan = backward_chaining(jenis_ikan, umur_ikan)
        rule = f"{jenis_ikan} {umur_ikan} -> {pakan_ikan}"
    return render_template('index.html', pakan_ikan=pakan_ikan, rule=rule)

if __name__ == "__main__":
    app.run(debug=True)
