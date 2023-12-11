daftar_nasabah = {}
nasabah = {}
tabungan = {}
kondisi = True

while kondisi:
    print("PROGAM MESIN ATM")
    print("================")

    pilih = str(input("1. Daftar \n2. Tabung \n3. Ambil Okane \n4. Transfer \n5. Cek saldo \nPilih: "))

    if pilih == "1":
        kondisi2 = True
        while kondisi2:
            import random
            import string

            try:
                nama = str(input("Nama: "))
                lenght = 13
                kode = ''.join(random.choices(string.digits, k=lenght))
                tabung = int(input("Tabungan Pertama : Rp "))
                daftar_nasabah[kode.title()] = {nama: tabung}
                nasabah[kode.title()] = nama
                tabungan[kode.title()] = tabung
                print(daftar_nasabah)
                print(tabungan)
                kondisi1 = True
                while kondisi1:
                    a = str(input("Apakah anda ingin kembali? \n1. B = kembali ke menu \n2. Y = Mengulang \n3. T = Tidak \nPilih:  "))
                    if a.lower() == "b":
                        kondisi1 = False
                        kondisi2 = False
                    elif a.lower() == "t":
                        kondisi1 = False
                        kondisi = False
                        kondisi2 = False
                    elif a.lower() == "y":
                        kondisi1 = False
                    else:
                        print("Input tidak valid, silakan masukkan pilihan yang benar.")
            except ValueError:
                print("Terjadi kesalahan input. Pastikan Anda memasukkan nilai yang benar.")
    elif pilih == "2":
        kondisi3 = True
        while kondisi3:
            
            try:
                kode_nasabah = str(input("Masukkan Nomer Rekening Anda: "))
                uang = int(input("Jumlah uang yang akan ditabung: Rp "))
                jumlah = tabungan[kode_nasabah] + uang
                tabungan[kode_nasabah] = jumlah
                print(tabungan)
                kondisi4 = True
                while kondisi4:
                    b = str(input("Apakah anda ingin kembali? \n1. B = kembali ke menu \n2. Y = Mengulang \n3. T = Tidak \nPilih:  "))
                    if b.lower() == "b":
                        kondisi = True
                        kondisi3 = False
                        kondisi4 = False
                    elif b.lower() == "y":
                        kondisi4 = False
                    elif b.lower() == "t":
                        kondisi = False
                        kondisi3 = False
                        kondisi4 = False
                    else:
                        print("Input tidak valid, silakan masukkan pilihan yang benar.")
            except ValueError:
                print("Terjadi kesalahan input. Pastikan Anda memasukkan nilai yang benar.")

    elif pilih == "3":
        kondisi5 = True
        while kondisi5:
            try:
                kode_pemilik = str(input("Masukan Nomer Rekening Anda: "))
                okane = int(input("jumlah uang yang akan di ambil: "))
                ambil = tabungan[kode_pemilik] - okane
                tabungan[kode_pemilik.title()] = ambil
                print(tabungan)
                kondisi6 = True
                while kondisi6:
                    c = str(input("Apakah anda ingin kembali? \n1. B = kembali ke menu \n2. Y = Mengulang \n3. T = Tidak \nPilih:  "))
                    if c.lower() == "b":
                        kondisi = True
                        kondisi5 = False
                        kondisi6 = False
                    elif c.lower() == "y":
                        kondisi6 = False
                    elif c.lower() == "n":
                        kondisi = False
                        kondisi5 = False
                        kondisi6 = False
                    else:
                        print("Input tidak valid, silakan masukkan pilihan yang benar.")
            except ValueError:
                print("Terjadi kesalahan input. Pastikan Anda memasukkan nilai yang benar.")

    elif pilih == "4":
        kondisi7 = True
        while kondisi7:
            try:
                milih = str(input("1. Transfer ke Bank Lain \n2. Transfer ke Sesama Bank \nPilih: "))
                if milih == "1":
                    no_rekening = str(input("Masukkan Nomer Rekening yang anda: "))
                    no_tujuan = int(input("Masukkan Nomer Rekening yang anda tujuh: "))
                    tf = int(input("Jumlah uang yang ingin anda trasnferkan: Rp "))
                    jumlah_tf = tabungan[no_rekening] - tf
                    tabungan[no_rekening] = jumlah_tf
                    print(tabungan)
                elif milih == "2":
                    kode_pengirim = str(input("Masukan Nomer Rekening Anda: "))
                    kode_penerima = str(input("Masukkan Nomer Rekening yang anda tujuh: "))
                    jumlah_uang = int(input("Jumlah yang ingin anda transferkan: "))
                    tf2 = tabungan[kode_pengirim] - jumlah_uang
                    jumlahtf = tabungan[kode_penerima] + jumlah_uang
                    tabungan[kode_penerima] = tf2
                    tabungan[kode_pengirim] = jumlahtf
                    print(tabungan)
                kondisi8 = True
                while kondisi8:
                    d = str(input("Apakah anda ingin kembali? \n1. B = kembali ke menu \n2. Y = Mengulang \n3. T = Tidak \nPilih:  "))
                    if d.lower() == "b":
                        kondisi = True
                        kondisi7 = False
                        kondisi8 = False
                    elif d.lower() == "y":
                        kondisi8 = False
                    elif d.lower() == "n":
                        kondisi = False
                        kondisi7 = False
                        kondisi8 = False
                    else:
                        print("Input tidak valid, silakan masukkan pilihan yang benar.")
            except ValueError:
                print("Terjadi kesalahan input. Pastikan Anda memasukkan nilai yang benar.")

    elif pilih == "5":
        kondisi9 = True
        while kondisi9:
            try:
                cari = input("masukkan nomer rekening anda: ")
                print(daftar_nasabah[cari])
                kondisi10 = True
                while kondisi10:
                    e = str(input("Apakah anda ingin kembali? \n1. B = kembali ke menu \n2. Y = Mengulang \n3. T = Tidak \nPilih:  "))
                    if e.lower() == "b":
                        kondisi = True
                        kondisi9 = False
                        kondisi10 = False
                    elif e.lower() == "y":
                        kondisi10 = False
                    elif e.lower() == "n":
                        kondisi = False
                        kondisi9 = False
                        kondisi10 = False
                    else:
                        print("Input tidak valid, silakan masukkan pilihan yang benar.")
            except ValueError:
                print("Terjadi kesalahan input. Pastikan Anda memasukkan nilai yang benar.")
    else:
        print("Mohon maaf tolong ulangi sekali lagi!!!")
        kondisi = True
