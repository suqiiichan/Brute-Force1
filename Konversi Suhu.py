class suhu():
	def celcius(C):
		if pilihan == 1:
			print("Hasil Celcius adalah ", 9 / 5 * Cel + 32, "F")
		elif pilihan == 2:
			print("Hasil Celcius adalah ", Cel + 273.15, "K")
		elif pilihan == 3:
			print("Hasil Celcius adalah ", (4 / 5) * Cel, "R")
		else:
			print("tidak ada")
	def fahrenheit(F):
		if pilihan1 == 1:
			print("Hasil Fahrenheit adalah ", (Fah-32)*(5/9), "C")
		elif pilihan1 == 2:
			print("Hasil Fahrenheit adalah ", (Fah + 273.15 )* 5/9, "K")
		elif pilihan1 == 3:
			print("Hasil Fahrenheit adalah ",( 4/9 )*(Fah-32), "R")
		else:
			print("tidak ada")
	def kelvin(K):
		if pilihan2 == 1:
			print("Hasil Kelvin adalah ", Kel - 273.15, "C")
		elif pilihan2 == 2:
			print("Hasil Kelvin adalah ", Kel *( 9/5) - 459.67, "F")
		elif pilihan2 == 3:
			print("Hasil Kelvin adalah ",(4/5) * Kel -273, "R")
		else:
			print("tidak ada")
	def reamur(R):
		if pilihan3 == 1:
			print("Hasil Reamur adalah ", Re /0.8, "C")
		elif pilihan3 == 2:
			print("Hasil Reamur adalah ", (Re * 2.25) + 32, "F")
		elif pilihan3 == 3:
			print("Hasil Reamur adalah ",(Re / 0.8) + 273.15, "K")
		else:
			print("tidak ada")

derajat = suhu()
kondisi = True
while(kondisi):
	print("Pilihlah satuan yang akan anda konversikan\n 1. Celcius\n 2. Fahrenheit\n 3. Kelvin\n 4. Reamur")
	pilih = int(input("pilih : "))
	if pilih == 1:
		kondisi1 = True
		while(kondisi1):
			pilihan = int(input("Pilih satuan celcius yang akan anda konversikan\n 1. Celcius ke Fahrenheit\n 2. Celcius ke Kelvin\n 3. Celcius ke Reamur\n Pilih: "))
			Cel = float(input("Masukan Suhu dalam satuan Celcius: "))
			suhu.celcius(Cel)
			kondisi5 = True
			while(kondisi5):
				pilihan4 = str(input("Apakah Anda ingin mengulang? tulis Y jika ingin mengulang, tulis N jika ingin berhenti, B jika ingin kembali ke menu\n Pilih: "))
				if pilihan4 == "b" or pilihan4 == "B":
					kondisi = True
					kondisi1 = False
					kondisi5 = False
				elif pilihan4 == "n" or pilihan4 == "N":
					kondisi = False
					kondisi1 = False
					kondisi5 = False
				elif pilihan4 == "y" or pilihan4 == "Y":
					kondisi = False
					kondisi1 = True
					kondisi5 = False
				else:
					print("Yang anda tulis tidak ada dalam pilihan")
					kondisi = False
					kondisi1 = False
					kondisi5 = True
	elif pilih == 2:
		kondisi2 = True
		while(kondisi2):
			pilihan1 = int(input("Pilih satuan Fahrenheit yang akan anda konversikan\n 1. Fahrenheit ke Celcius\n 2. Fahrenheit ke Kelvin\n 3. Fahrenheit ke Reamur\n Pilih: "))
			Fah = float(input("Masukan Suhu dalam satuan Fahrenheit: "))
			suhu.fahrenheit(Fah)
			kondisi6 = True
			while(kondisi6):
				pilihan5 = str(input("Apakah Anda ingin mengulang? tulis Y jika ingin mengulang, tulis N jika ingin berhenti, tulis B jika ingin kembali kemenu\n Pilih: "))
				if pilihan5 == "b" or pilihan5 == "B":
					kondisi = True
					kondisi2 = False
					kondisi6 = False
				elif pilihan5 == "n" or pilihan5 == "N":
					kondisi = False
					kondisi2 = False
					kondisi6= False
				elif pilihan5 == "y" or pilihan5 == "Y":
					kondisi = False
					kondisi2 = True
					kondisi6 = False
				else:
					print("Yang anda tulis tidak ada dalam pilihan")
					kondisi = False
					kondisi2 = False
					kondisi6 = True
	elif pilih == 3:
		kondisi3 = True
		while(kondisi3):
			pilihan2 = int(input("Pilih satuan Kelvin yang akan anda konversikan\n 1. Kelvin ke Celcius\n 2. Kelvin ke Fahrenheit\n 3. Kelvin ke Reamur\n Pilih: "))
			Kel = float(input("Masukan Suhu dalam Kelvin: "))
			suhu.kelvin(Kel)
			kondisi7 = True
			while(kondisi7):
				pilihan6 = str(input("Apakah Anda ingin mengulang? tulis Y jika ingin mengulang, tulis N jika ingin berhenti, tulis B jika anda ingin kembali ke menu\n Pilih: "))
				if pilihan6 == "b" or pilihan6 == "B":
					kondisi = True
					kondisi3 = False
					kondisi7 = False
				elif pilihan6 == "n" or pilihan6 == "N":
					kondisi = False
					kondisi3 = False
					kondisi7 = False
				elif pilihan6 == "y" or pilihan6 == "Y":
					kondisi = False
					kondisi3 = True
					kondisi7 = False
				else:
					print("Yang anda tulis tidak ada dalam pilihan")
					kondisi = False
					kondisi3 = False
					kondisi7 = True
	elif pilih == 4:
		kondisi4 = True
		while(kondisi4):
			pilihan3 = int(input("Pilih satuan Reamur yang akan anda konversikan\n 1. Reamur ke Celcius\n 2. Reamur ke Fahrenheit\n 3. Fahrenheit ke Reamur\n Pilih: "))
			Re = float(input("Masukan Suhu dalam satuan Reamur: "))
			suhu.reamur(Re)
			kondisi8 = True
			while(kondisi8):
				pilihan7 = str(input("Apakah Anda ingin mengulang? tulis Y jika ingin mengulang, tulis N jika ingin berhenti, ketik B jika anda ingin kembali ke menu\n Pilih: "))
				if pilihan7 == "b" or pilihan7 == "B":
					kondisi = True
					kondisi4 = False
					kondisi8 = False
				elif pilihan7 == "n" or pilihan7 == "N":
					kondisi = False
					kondisi4 = False
					kondisi8 = False
				elif pilihan7 == "y" or pilihan7 == "Y":
					kondisi = False
					kondisi4 = True
					kondisi8 = False
				else:
					print("Yang anda tulis tidak ada dalam pilihan")
					kondisi = False
					kondisi4 = False
					kondisi8 = True
	else:
		print("pilihan anda salah")
		kondisi = True
