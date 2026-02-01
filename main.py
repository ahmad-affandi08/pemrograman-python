from agent_rule_based import agent_jawab
from agent_memory_basic import agent_jawab as agent_memori, simpan_chat, tampilkan_ringkas_chat, save_memory, load_memory
from agent_multistep import run_agent as agent_multi
from agent_task_manager import agent_tugas

def log_interaksi(input_pengguna, output_agent):
    with open("log_agent.txt", "a", encoding="utf-8") as f:
        f.write(f"USER: {input_pengguna}\nAGENT: {output_agent}\n---\n")



def tampilkan_menu():
    print("\n" + "="*70)
    print("🤖 SELAMAT DATANG DI AGENT PYTHON - PRAKTIKUM 7 & 8")
    print("="*70)
    print("🚀 Tersedia 4 jenis agent canggih:")
    print("   🔧 Agent Rule-Based - 6 tools (Praktikum 7: kalkulator, kamus, file, suhu, BMI, cari kata)")
    print("   🧠 Agent Memory - Ingat percakapan + simpan ke JSON")
    print("   🔄 Agent Multi-Step - Plan → Act → Observe → Reflect")
    print("   📋 Agent Task Manager - Kelola daftar tugas")
    print("-" * 70)
    print("🎯 Pilih mode operasi:")
    print("1. 🔧 Agent Rule-Based - Tool tradisional (Praktikum 7)")
    print("2. 🧠 Agent Memory - Chat dengan memori")
    print("3. 🔄 Agent Multi-Step - Tugas bertahap")
    print("4. 📋 Agent Task Manager - Kelola tugas")
    print("5. 🧪 Demo Otomatis - Test semua agent")
    print("6. 📊 Lihat Log - History percakapan")
    print("7. 🚪 Keluar")
    print("="*70)

def chat_agent_memory():
    print("\n🧠 MODE AGENT MEMORY")
    print("-" * 50)
    print("💡 Agent ini mengingat percakapan selama sesi!")
    print("📝 Ketik 'ringkas chat' untuk lihat percakapan terakhir")
    print("🚪 Ketik 'exit' untuk keluar")
    print("-" * 50)
    
    load_memory()
    print("💾 Memori chat berhasil dimuat!")
    
    while True:
        try:
            user_input = input("\n👤 Anda: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                save_memory()
                print("💾 Memori tersimpan ke memory_chat.json")
                print("🤖 Agent: Sampai jumpa! 👋")
                break
                
            if not user_input:
                continue
                
            simpan_chat("user", user_input)
            jawaban = agent_memori(user_input)
            simpan_chat("agent", jawaban)
            
            print(f"🤖 Agent: {jawaban}")
            
        except KeyboardInterrupt:
            save_memory()
            print("\n💾 Memori tersimpan ke memory_chat.json")
            print("\n🤖 Agent: Sampai jumpa! 👋")
            break

def chat_agent_multistep():
    print("\n🔄 MODE AGENT MULTI-STEP")
    print("-" * 50)
    print("🎯 Agent ini dapat menjalankan tugas bertahap!")
    print("📋 Perintah tersedia:")
    print("   • buat ringkasan file [nama]")
    print("   • analisis nilai file [nama]")
    print("   • buat quiz dari file [nama]")
    print("🚪 Ketik 'exit' untuk keluar")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n👤 Anda: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("🤖 Agent: Sampai jumpa! 👋")
                break
                
            if not user_input:
                continue
                
            hasil = agent_multi(user_input)
            print(f"🤖 Agent: {hasil}")
            log_interaksi(user_input, hasil)
            
        except KeyboardInterrupt:
            print("\n🤖 Agent: Sampai jumpa! 👋")
            break

def chat_agent_tasks():
    print("\n📋 MODE AGENT TASK MANAGER")
    print("-" * 50)
    print("📝 Agent untuk mengelola daftar tugas!")
    print("💼 Perintah tersedia:")
    print("   • tambah tugas [judul]")
    print("   • lihat tugas")
    print("   • selesai tugas [id]")
    print("🚪 Ketik 'exit' untuk keluar")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n👤 Anda: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("🤖 Agent: Sampai jumpa! 👋")
                break
                
            if not user_input:
                continue
                
            jawaban = agent_tugas(user_input)
            print(f"🤖 Agent: {jawaban}")
            
        except KeyboardInterrupt:
            print("\n🤖 Agent: Sampai jumpa! 👋")
            break

def demo_semua_agent():
    print("\n🧪 DEMO SEMUA AGENT PRAKTIKUM 8")
    print("=" * 60)
    
    print("\n1️⃣  Testing Agent Rule-Based:")
    print("Input: hitung 10+5*2")
    hasil1 = agent_jawab("hitung 10+5*2")
    print(f"Output: {hasil1}")
    
    print("\n2️⃣  Testing Agent Memory:")
    print("Input: arti python")
    hasil2 = agent_memori("arti python")
    print(f"Output: {hasil2}")
    
    print("\n3️⃣  Testing Agent Multi-Step:")
    print("Input: buat ringkasan file materi.txt")
    hasil3 = agent_multi("buat ringkasan file materi.txt")
    print(f"Output: {hasil3}")
    
    print("\n4️⃣  Testing Agent Task Manager:")
    print("Input: lihat tugas")
    hasil4 = agent_tugas("lihat tugas")
    print(f"Output: {hasil4}")
    
    print("\n✅ Demo selesai! Semua agent berfungsi dengan baik.")


def chat_agent_rule_based():
    print("\n🔧 MODE AGENT RULE-BASED (PRAKTIKUM 7)")
    print("-" * 60)
    print("🎯 CARA MENGGUNAKAN AGENT:")
    print("📋 Ketik perintah berikut untuk menggunakan tools:")
    print("   • 'hitung 2+3*4' - Menghitung ekspresi matematika")
    print("   • 'arti python' - Mencari arti kata di kamus")
    print("   • 'baca file materi.txt' - Membaca isi file")
    print("   • 'konversi 25' - Konversi 25°C ke Fahrenheit")
    print("   • 'bmi 70 1.75' - Hitung BMI (berat tinggi)")
    print("   • 'cari python di materi.txt' - Cari kata dalam file")
    print("   • 'ringkas file materi.txt' - Meringkas file")
    print("   • 'help' - Bantuan lengkap")
    print("   • 'exit' - Keluar dari chat")
    print("-" * 60)
    print("💡 Tips: Format perintah:")
    print("   'hitung', 'arti', 'baca file', 'konversi', 'bmi', 'cari [kata] di [file]', 'ringkas file'")
    print("-" * 60)
    
    while True:
        try:
            user_input = input("\n👤 Anda: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'keluar']:
                print("🤖 Agent: Sampai jumpa! 👋")
                break
            
            if user_input.lower() == 'help':
                print("\n🤖 Agent: 📚 PANDUAN LENGKAP PENGGUNAAN TOOLS")
                print("   " + "-" * 50)
                print("   🧮 KALKULATOR:")
                print("      • hitung 10+5*2")
                print("      • kalkulator (15-3)/4")
                print("      • perhitungan 2**3+1")
                print()
                print("   📖 KAMUS DIGITAL:")
                print("      • arti python")
                print("      • definisi agent")
                print("      • arti llm")
                print()
                print("   📄 BACA FILE:")
                print("      • baca file materi.txt")
                print("      • baca file data.txt")
                print()
                print("   🌡️ KONVERSI SUHU:")
                print("      • konversi 25 (Celsius ke Fahrenheit)")
                print("      • konversi 0")
                print()
                print("   ⚖️ HITUNG BMI:")
                print("      • bmi 70 1.75 (berat kg, tinggi m)")
                print("      • bmi 60 1.65")
                print()
                print("   🔍 CARI KATA:")
                print("      • cari python di materi.txt")
                print("      • cari AI di materi.txt")
                print()
                print("   📝 RINGKAS FILE:")
                print("      • ringkas file materi.txt")
                print("      • ringkasan dokumen.txt")
                print("   " + "-" * 50)
                continue
            
            if not user_input:
                print("🤖 Agent: Silakan masukkan pertanyaan atau perintah.")
                continue
            
            jawaban = agent_jawab(user_input)
            print(f"🤖 Agent: {jawaban}")
            log_interaksi(user_input, jawaban)
            
        except KeyboardInterrupt:
            print("\n🤖 Agent: Sampai jumpa! 👋")
            break
        except Exception as e:
            print(f"🤖 Agent: Terjadi error: {e}")

def lihat_log():
    print("\n📊 LOG INTERAKSI TERAKHIR")
    print("-" * 40)
    try:
        with open("log_agent.txt", "r", encoding="utf-8") as f:
            log_content = f.read()
        
        if log_content.strip():
            # Tampilkan 5 interaksi terakhir
            interaksi = log_content.strip().split("---\n")
            interaksi_terakhir = interaksi[-5:] if len(interaksi) > 5 else interaksi
            
            for i, interaksi_item in enumerate(interaksi_terakhir, 1):
                if interaksi_item.strip():
                    print(f"\n[{i}] {interaksi_item.strip()}")
            
            print(f"\n📝 Total: {len([i for i in interaksi if i.strip()])} interaksi tersimpan")
        else:
            print("📝 Belum ada log interaksi.")
            
    except FileNotFoundError:
        print("📝 File log belum ada. Mulai chat dulu untuk membuat log.")

def main():
    while True:
        tampilkan_menu()
        
        try:
            pilihan = input("🎮 Masukkan pilihan Anda (1-7): ").strip()
            
            if not pilihan:
                print("❌ Harap masukkan pilihan 1-7.")
                continue
            
            if pilihan == '1':
                chat_agent_rule_based()
            elif pilihan == '2':
                chat_agent_memory()
            elif pilihan == '3':
                chat_agent_multistep()
            elif pilihan == '4':
                chat_agent_tasks()
            elif pilihan == '5':
                demo_semua_agent()
            elif pilihan == '6':
                lihat_log()
            elif pilihan == '7':
                print("👋 Terima kasih telah menggunakan Agent Python!")
                break
            else:
                print("❌ Pilihan tidak valid. Pilih 1-7.")
                
        except KeyboardInterrupt:
            print("\n👋 Terima kasih telah menggunakan Agent Python!")
            break
        except Exception as e:
            print(f"❌ Terjadi error: {e}")

if __name__ == "__main__":
    main()