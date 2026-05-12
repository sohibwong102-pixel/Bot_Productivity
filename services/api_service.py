import requests

def get_advice():
                # API Key pihak ketiga
                url = "https://api.adviceslip.com/advice"

                # python mengirim request GET ke api
                response = requests.get(url)

                print(response)
                print(response.text)
                
                # menampilkan data dari json (hanya mengincar advice karna advice didalam kurung slip)
                data = response.json()
                print(data["slip"]["advice"])