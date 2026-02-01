from tools import kalkulator, kamus_lookup, baca_file, konversi_suhu, hitung_bmi, cari_kata_dalam_file, ringkas_file

def log_interaksi(user_input, agent_output):
    with open("log_agent.txt", "a", encoding="utf-8") as f:
        f.write(f"USER: {user_input}\nAGENT: {agent_output}\n---\n")

def agent_jawab(user_input: str) -> str:
    teks = user_input.lower()

    if "hitung" in teks:
        expr = teks.replace("hitung", "").strip()
        hasil = kalkulator(expr)
        return f"Hasil perhitungan: {hasil}"

    if teks.startswith("arti "):
        kata = teks.replace("arti", "").strip()
        hasil = kamus_lookup(kata)
        return f"Arti '{kata}': {hasil}"

    if teks.startswith("baca file "):
        path = teks.replace("baca file", "").strip()
        hasil = baca_file(path)
        return f"Isi file '{path}':\n{hasil}"

    if teks.startswith("konversi "):
        try:
            celsius = float(teks.replace("konversi", "").strip())
            hasil = konversi_suhu(celsius)
            return f"Konversi suhu: {hasil}"
        except ValueError:
            return "Format: konversi [angka]. Contoh: konversi 25"

    if teks.startswith("bmi "):
        try:
            parts = teks.replace("bmi", "").strip().split()
            if len(parts) == 2:
                berat = float(parts[0])
                tinggi = float(parts[1])
                hasil = hitung_bmi(berat, tinggi)
                return f"Hasil BMI: {hasil}"
            else:
                return "Format: bmi [berat] [tinggi]. Contoh: bmi 70 1.75"
        except ValueError:
            return "Format: bmi [berat] [tinggi]. Contoh: bmi 70 1.75"

    if teks.startswith("cari ") and " di " in teks:
        try:
            parts = teks.replace("cari", "").strip().split(" di ")
            if len(parts) == 2:
                kata = parts[0].strip()
                file_path = parts[1].strip()
                hasil = cari_kata_dalam_file(kata, file_path)
                return hasil
            else:
                return "Format: cari [kata] di [file]. Contoh: cari python di materi.txt"
        except:
            return "Format: cari [kata] di [file]. Contoh: cari python di materi.txt"

    if teks.startswith("ringkas file "):
        path = teks.replace("ringkas file", "").strip()
        hasil = ringkas_file(path)
        return hasil

    return "Saya belum punya tool untuk itu. Coba: hitung / arti / baca file / konversi / bmi / cari [kata] di [file] / ringkas file."

if __name__ == "__main__":
    print("=== AGENT RULE-BASED PRAKTIKUM 7 ===")
    print("Ketik 'exit' atau 'quit' untuk keluar")
    print("Kata kunci: hitung / arti / baca file / konversi / bmi / cari [kata] di [file] / ringkas file")
    print("-" * 80)
    
    while True:
        q = input("\nKamu: ")
        if q.lower() in ["exit", "quit"]:
            print("Agent berhenti.")
            break
        
        jawaban = agent_jawab(q)
        print("Agent:", jawaban)
        log_interaksi(q, jawaban)