import json
from tools import kalkulator, kamus_lookup, baca_file

daftar_tugas = []

def muat_tugas(path="task_list.json"):
    global daftar_tugas
    try:
        with open(path, "r", encoding="utf-8") as f:
            daftar_tugas = json.load(f)
    except FileNotFoundError:
        daftar_tugas = []

def simpan_tugas(path="task_list.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(daftar_tugas, f, indent=2, ensure_ascii=False)

def tambah_tugas(judul):
    tugas_baru = {
        "id": len(daftar_tugas) + 1,
        "judul": judul,
        "status": "belum_selesai",
        "waktu_dibuat": "sekarang"
    }
    daftar_tugas.append(tugas_baru)
    return f"Tugas '{judul}' berhasil ditambahkan dengan ID {tugas_baru['id']}"

def lihat_tugas():
    if not daftar_tugas:
        return "Tidak ada tugas yang tersimpan."
    
    hasil = "Daftar Tugas:\n"
    for tugas in daftar_tugas:
        status_icon = "✅" if tugas["status"] == "selesai" else "⏳"
        hasil += f"{status_icon} ID {tugas['id']}: {tugas['judul']} [{tugas['status']}]\n"
    return hasil

def selesaikan_tugas(task_id):
    for tugas in daftar_tugas:
        if tugas["id"] == task_id:
            tugas["status"] = "selesai"
            return f"Tugas ID {task_id} telah diselesaikan!"
    return f"Tugas ID {task_id} tidak ditemukan."

def agent_tugas(input_pengguna: str) -> str:
    teks = input_pengguna.lower().strip()

    if teks.startswith("tambah tugas "):
        judul = input_pengguna[12:].strip()
        return tambah_tugas(judul)
    
    if teks == "lihat tugas":
        return lihat_tugas()
    
    if teks.startswith("selesai tugas "):
        try:
            task_id = int(teks.replace("selesai tugas", "").strip())
            return selesaikan_tugas(task_id)
        except ValueError:
            return "Format salah. Gunakan: selesai tugas [nomor_id]"

    if "hitung" in teks:
        expr = teks.replace("hitung", "").strip()
        return kalkulator(expr)
    
    if teks.startswith("arti "):
        kata = teks.replace("arti", "").strip()
        return kamus_lookup(kata)
    
    if teks.startswith("baca file "):
        path = teks.replace("baca file", "").strip()
        return baca_file(path)

    return "Perintah tersedia: tambah tugas / lihat tugas / selesai tugas [id] / hitung / arti / baca file"

if __name__ == "__main__":
    muat_tugas()
    
    print("=== AGENT TASK MANAGER ===")
    print("Perintah:")
    print("- tambah tugas [judul_tugas]")
    print("- lihat tugas")  
    print("- selesai tugas [id]")
    print("- Tool biasa: hitung / arti / baca file")
    
    while True:
        pertanyaan = input("\nKamu: ")
        if pertanyaan.lower() in ["exit", "quit"]:
            simpan_tugas()
            print("Task list tersimpan. Agent berhenti.")
            break
        
        jawaban = agent_tugas(pertanyaan)
        print("Agent:", jawaban)