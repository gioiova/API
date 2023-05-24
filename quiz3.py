import requests
import json
import sqlite3
conn = sqlite3.connect("apidb.sqlite")
cur = conn.cursor()
base_url = "http://api.football-data.org/v4/matches"
api_key = "058b865ff89441168c3594ef554c275a"


url = f"{base_url}"
headers = {
    "X-Auth-Token": api_key,
}
payload = {"dateFrom":"2023-05-22",
           "dateTo":"2023-05-25"}
response = requests.get(url,headers=headers,params=payload)
# print(response)
# print(response.status_code)
# print(response.headers)
result = response.json()
print(type(response.text))
print(json.dumps(result,indent=4))
coun = result["matches"][2]["area"]["name"]
print(coun)
# with open('matches.json','w') as f:
#     json.dump(result,f,indent=4)

#მოცემულ თარიღში,თუ რომელ ქვეყნებში ჩატარდა მატჩები
cur.execute('''CREATE TABLE area
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            country VARCHAR(50))''')
cur.execute("INSERT INTO area (country) values (?)",(coun,))
conn.commit()