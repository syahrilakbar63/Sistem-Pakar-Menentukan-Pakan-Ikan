from flask import Flask, request, render_template
app = Flask(__name__)

# Modul Basis Pengetahuan

# Fakta-fakta
jenis_ikan = ["lele", "gurame", "nila", "mas", "patin", "bawal"]
umur_ikan = ["burayak", "juvenile", "dewasa", "tua"]
pakan_ikan = ["pelet", "cacing", "pur", "udang"]

# Aturan-aturan
aturan = {
    "lele": {"burayak": "pelet", "juvenile": "pelet", "dewasa": "pelet", "tua": "pelet"},
    "gurame": {"burayak": "cacing", "juvenile": "cacing", "dewasa": "pur", "tua": "pur"},
    "nila": {"burayak": "pelet", "juvenile": "pelet", "dewasa": "pur", "tua": "pur"},
    "mas": {"burayak": "pelet", "juvenile": "pelet", "dewasa": "pur", "tua": "pur"},
    "patin": {"burayak": "pelet", "juvenile": "udang", "dewasa": "udang", "tua": "udang"},
    "bawal": {"burayak": "pelet", "juvenile": "udang", "dewasa": "udang", "tua": "udang"}
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