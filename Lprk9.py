def buat_file(file_name):
    try:
        with open(file_name, 'w') as file:
            print(f"File '{file_name}' berhasil dibuat.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membuat file: {e}")

def baca_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print("Isi file:")
            print(file.read())
    except FileNotFoundError:
        print(f"File '{file_name}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")

def tambah_ke_file(file_name, text):
    try:
        with open(file_name, 'a') as file:
            file.write(text + '\n')
            print("Data berhasil ditambahkan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan data: {e}")

def main():
    print("\nPilih Menu:")
    print("1. Buat File")
    print("2. Baca File")
    print("3. Tambah Data ke File")
    print("4. Tutup Program")

    while True:
        pilihan = input("\nPilih menu (1/2/3/4): ")
        if pilihan == '1':
            file_name = input("Masukkan nama file (contoh: data.txt): ")
            buat_file(file_name)
        elif pilihan == '2':
            file_name = input("Masukkan nama file yang ingin dibaca: ")
            baca_file(file_name)
        elif pilihan == '3':
            file_name = input("Masukkan nama file untuk menambah data: ")
            text = input("Masukkan data yang ingin ditambahkan: ").capitalize()
            tambah_ke_file(file_name, text)
        elif pilihan == '4':
            print("Terima kasih program ditutup. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

main()