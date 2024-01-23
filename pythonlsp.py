def tampilkan_menu():
    print("========== Menu ==========")
    print("1. Pilihan 1")
    print("2. Pilihan 2")
    print("3. Pilihan 3")
    print("0. Keluar")
    print("==========================")

# Contoh pemanggilan
tampilkan_menu()
def layar_input():
    input_user = input("Masukkan sesuatu: ")
    return input_user

# Contoh pemanggilan
data_input = layar_input()
print("Anda memasukkan:", data_input)
def layar_output(data):
    print("========== Output ==========")
    print(data)
    print("=============================")

# Contoh pemanggilan
data_output = "Ini adalah contoh output"
layar_output(data_output)
while True:
    tampilkan_menu()

    pilihan = input("Pilih menu (0-3): ")

    if pilihan == '1':
        data_input = layar_input()
        hasil_proses = "Anda memasukkan: " + data_input
        layar_output(hasil_proses)
    elif pilihan == '2':
        # Tambahkan logika pilihan 2
        pass
    elif pilihan == '3':
        # Tambahkan logika pilihan 3
        pass
    elif pilihan == '0':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
