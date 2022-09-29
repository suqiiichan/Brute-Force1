dict_barang = {}
list_barang = {}
kondisi1 = True
while kondisi1:
    print("===============")
    print("KASIR INDOAPRIL")
    print("===============")
    print("1. INPUT DATA BARANG \n2. CARI DATA \n3. TOTAL DATA")
    pilih = str(input("Pilih : "))
    if pilih == "1":
        jumlah_barang = int(input("Berapa jumlah barang yang ingin anda masukkan? "))
        for i in range(jumlah_barang):
            kode_barang = str(hash(input("masukan nama barang: ")))
            nama_barang = str(input("masukan nama barang: "))
            harga = int(input("masukan harga barang: "))
            dict_barang[kode_barang.title()] = {nama_barang : harga}
            list_barang[nama_barang.title()] = harga
            print(dict_barang)
    elif pilih == "2":
        cari_data = input("Masukan koba barang: ")
        print(dict_barang[cari_data])
    elif pilih == "3":
        def getPrice(name, jumlah):
            hasil = list_barang[name]*jumlah
            print(name+":Rp "+str(list_barang[name])+"x "+str(jumlah)+"=Rp "+str(hasil))
            return hasil
        user = {}
        total = 0
        kondisi = True
        while kondisi:
            barang_key = input("Nama Barang: ")
            jumlah_value = int(input("Jumlah Barang: "))
            user[barang_key.title()]= jumlah_value

            for k,v in user.items():
                total += getPrice(k,v)
            kondisi3 = True
            while kondisi3:
                tanya = str(input("apa masih ada barang yang akan ditambah? \nklilk y atau n: "))
                if tanya == "n" or tanya == "N":
                    kondisi3 = False
                    kondisi = False
                elif tanya == "y" or tanya == "Y":
                    kondisi = True
                    kondisi3 =False
                else:
                    print("GAGAL")
                    kondisi3 = True
                    kondisi = False
        print("jumlah yang harus dibayar: Rp ", total)
    else:
        print("Pilihan anda tidak ada")
        kondisi1 = True
    kondisi2 = True
    while kondisi2:
        pertanyaan = str(input("Apakah Anda Ingin Mengulanginya? \nN atau Y"))
        if pertanyaan == "n" or pertanyaan == "N":
            kondisi1 = False
            kondisi2 = False
        elif pertanyaan == "y" or pertanyaan == "Y":
            kondisi1 = True
            kondisi2 = False
        else:
            print("Ulangi")
            kondisi1 = False
            kondisi2 = True
