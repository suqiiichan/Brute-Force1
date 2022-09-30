from datetime import datetime

hari = {"Sunday":"Mingggu",
        "Monday":"Senin",
        "Tuesday":"Selasa",
        "Wednesday":"Rabu",
        "Thursday":"Kamis",
        "Friday":"Jumat",
        "Saturday":"Sabtu"}
tgl = str(input("masukan tanggal: "))
x = datetime.strptime(tgl, "%Y-%m-%d")
print("Halo, tanggal ",x.strftime("%d/%m/%Y"), "adalah hari ",hari[x.strftime("%A")])
