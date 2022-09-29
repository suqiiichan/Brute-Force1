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

            nama = str(input("Nama: "))
            lenght = 13
            kode = ''.join(random.choices(string.digits, k= lenght))
            tabung = int(input("Tabungan Pertama : Rp "))
            daftar_nasabah[kode.title()] = {nama: tabung}
            nasabah[kode.title()] = nama
            tabungan[kode.title()] = tabung
            print(daftar_nasabah)
            print(tabungan)
            kondisi1 = True
            while kondisi1:
                a = str(input("Apakah anda ingin kembali? \n1. B = kembali ke menu \n2. Y = Mengulang \n3. T = Tidak \nPilih:  "))
                if a == "b" or a == "B":
                    kondisi = True
                    kondisi1 = False
                    kondisi2 = False
                elif a == "n" or a == "N":
                    kondisi = False
                    kondisi1 = False
                    kondisi2 = False
                elif a == "y" or a == "Y":
                    kondisi = False
                    kondisi1 = False
                    kondisi2 = True
                else:
                    kondisi = False
                    kondisi1 = True
                    kondisi2 = False
    elif pilih == "2":
        kondisi3 = True
        while kondisi3:
            kode_nasabah = str(input("Masukkan Nomer Rekening Anda: "))
            uang = int(input("Jumlah uang yang akan ditabung: Rp "))
            jumlah = tabungan[kode_nasabah] + uang
            tabungan[kode_nasabah] = jumlah
            print(tabungan)
            kondisi4 = True
            while kondisi4:
                b = str(input("Apakah anda ingin kembali? \n1. B = kembali ke menu \n2. Y = Mengulang \n3. T = Tidak \nPilih:  "))
                if b == "b" or b == "B":
                    kondisi = True
                    kondisi3 = False
                    kondisi4 = False
                elif b == "y" or b == "Y":
                    kondisi = False
                    kondisi4 = False
                    kondisi3 = True
                elif b == "n" or b == "N":
                    kondisi = False
                    kondisi3 = False
                    kondisi4 = False
                else:
                    kondisi = False
                    kondisi3 = False
                    kondisi4 = True
    elif pilih == "3":
        kondisi5 = True
        while kondisi5:
            kode_pemilik = str(input("Masukan Nomer Rekening Anda: "))
            okane = int(input("jumlah uang yang akan di ambil: "))
            ambil = tabungan[kode_pemilik] - okane
            tabungan[kode_pemilik.title()] = ambil
            print(tabungan)
            kondisi6 = True
            while kondisi6:
                c = str(input("Apakah anda ingin kembali? \n1. B = kembali ke menu \n2. Y = Mengulang \n3. T = Tidak \nPilih:  "))
                if c == "b" or c == "B":
                    kondisi = True
                    kondisi5 = False
                    kondisi6 = False
                elif c == "y" or c == "Y":
                    kondisi = True
                    kondisi5 = False
                    kondisi6 = False
                elif c == "n" or c == "N":
                    kondisi = False
                    kondisi5 = False
                    kondisi6 = False
                else:
                    kondisi = False
                    kondisi5 = False
                    kondisi6 = True
    elif pilih == "4":
        kondisi7 = True
        while kondisi7:
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
                if d == "B" or d == "b":
                    kondisi = True
                    kondisi7 = False
                    kondisi8 = False
                elif d == "y" or d == "Y":
                    kondisi = False
                    kondisi7 = True
                    kondisi8 = False
                elif d == "n" or d == "N":
                    kondisi = False
                    kondisi7 = False
                    kondisi8 = False
                else:
                    kondisi = False
                    kondisi7 = False
                    kondisi8 = True
    elif pilih == "5":
        kondisi9 = True
        while kondisi9:
            cari = input("masukkan nomer rekening anda: ")
            print(daftar_nasabah[cari])
            kondisi10 = True
            while kondisi10:
                e = str(input("Apakah anda ingin kembali? \n1. B = kembali ke menu \n2. Y = Mengulang \n3. T = Tidak \nPilih:  "))
                if e == "B" or e == "b":
                    kondisi = True
                    kondisi9 = False
                    kondisi10 = False
                elif e == "y" or e == "Y":
                    kondisi = False
                    kondisi9 = True
                    kondisi10 = False
                elif e == "n" or e == "N":
                    kondisi = False
                    kondisi9 = False
                    kondisi10 = False
                else:
                    kondisi = False
                    kondisi9 = False
                    kondisi10 = True
    else:
        print("Mohon maaf tolong ulangi sekali lagi!!!")
        kondisi = True
