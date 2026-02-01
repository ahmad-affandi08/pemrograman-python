def kalkulator(expr: str) -> float:
    """
    Tool kalkulator sederhana.
    expr contoh: "2+3*4"
    """
    try:
        return eval(expr)
    except Exception as e:
        return f"Error kalkulator: {e}"

KAMUS = {
    "python": "Bahasa pemrograman populer untuk otomasi, data, dan AI.",
    "agent": "Program yang bisa merencanakan dan memakai tool untuk menyelesaikan tujuan.",
    "llm": "Model bahasa besar yang menghasilkan teks berdasarkan konteks."
}

def kamus_lookup(kata: str) -> str:
    kata = kata.lower().strip()
    return KAMUS.get(kata, "Kata tidak ditemukan di kamus.")

def baca_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "File tidak ditemukan."
    except Exception as e:
        return f"Error baca file: {e}"

def konversi_suhu(celsius: float) -> str:
    """
    Tool konversi suhu - Mini Exercise E (Pilihan 1)
    """
    try:
        fahrenheit = (celsius * 9/5) + 32
        return f"{celsius}°C = {fahrenheit}°F"
    except Exception as e:
        return f"Error konversi suhu: {e}"

def hitung_bmi(berat: float, tinggi: float) -> str:
    """
    Tool hitung BMI - Mini Exercise E (Pilihan 2)
    berat dalam kg, tinggi dalam meter atau cm (auto-detect)
    """
    try:
        # Auto-detect: jika tinggi > 3, artinya dalam cm, convert ke meter
        if tinggi > 3:
            tinggi_meter = tinggi / 100
            note = f" (tinggi {tinggi} cm = {tinggi_meter} m)"
        else:
            tinggi_meter = tinggi
            note = f" (tinggi {tinggi} m)"
            
        bmi = berat / (tinggi_meter ** 2)
        
        if bmi < 18.5:
            kategori = "Kurus"
        elif bmi < 25:
            kategori = "Normal"
        elif bmi < 30:
            kategori = "Gemuk"
        else:
            kategori = "Obesitas"
            
        return f"BMI: {bmi:.2f} - Kategori: {kategori}{note}"
    except Exception as e:
        return f"Error hitung BMI: {e}"

def cari_kata_dalam_file(kata: str, path: str) -> str:
    """
    Tool search kata dalam file - Mini Exercise E (Pilihan 3)
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            isi = f.read()
        
        jumlah = isi.lower().count(kata.lower())
        return f"Kata '{kata}' ditemukan {jumlah} kali dalam file '{path}'"
    except FileNotFoundError:
        return "File tidak ditemukan."
    except Exception as e:
        return f"Error cari kata: {e}"

def ringkas_file(path: str) -> str:
    """
    Tool ringkas file - Bonus F
    Ambil 2 kalimat pertama sebagai ringkasan
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            isi = f.read().strip()
        
        kalimat = isi.split('. ')
        if len(kalimat) >= 2:
            ringkasan = '. '.join(kalimat[:2])
            if not ringkasan.endswith('.'):
                ringkasan += '.'
            return f"Ringkasan file '{path}':\n{ringkasan}"
        else:
            return f"Ringkasan file '{path}':\n{isi}"
            
    except FileNotFoundError:
        return "File tidak ditemukan."
    except Exception as e:
        return f"Error ringkas file: {e}"

if __name__ == "__main__":
    print("=== UJI TOOLS PRAKTIKUM 7 ===")
    print("D1. Tool Kalkulator:")
    print("2+3*4 =", kalkulator("2+3*4"))
    print("10/0 =", kalkulator("10/0"))
    
    print("\nD2. Tool Kamus:")
    print("python →", kamus_lookup("python"))
    print("robot →", kamus_lookup("robot"))
    
    print("\nD3. Tool Baca File:")
    print(baca_file("materi.txt"))
    
    print("\nE. Mini Exercise - Semua Pilihan Tools:")
    print("Tool 1 - Konversi Suhu:")
    print("25°C →", konversi_suhu(25))
    print("0°C →", konversi_suhu(0))
    
    print("\nTool 2 - Hitung BMI:")
    print("70kg, 1.75m →", hitung_bmi(70, 1.75))
    print("80kg, 1.60m →", hitung_bmi(80, 1.60))
    
    print("\nTool 3 - Cari Kata dalam File:")
    print("Cari 'python' →", cari_kata_dalam_file("python", "materi.txt"))
    print("Cari 'AI' →", cari_kata_dalam_file("AI", "materi.txt"))