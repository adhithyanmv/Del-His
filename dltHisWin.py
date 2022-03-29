import sqlite3
import getpass
import src.windows.getIds as getids
import sys
import os

arr = ["C:", "Users", getpass.getuser(), "AppData", "Local", "Google", "Chrome", "User Data", "Default", "History"]
path = "\\\\".join(arr)

if os.stat('domains.txt').st_size == 0 and len(sys.argv) == 1:
    ss = input("Urls or domains are empty (Note: seperate with a space if you have multiple domains EG: 'Domain1 Domain2') : ").strip().split(" ")

    f = open("domains.txt", "a")
    for i in range(len(ss)):
        f.write(ss[i])
        f.write("\n")
    f.close()
    print("Domains Added!")

if len(sys.argv) > 1:
    if sys.argv[1] == "-add":
        ss = input("Enter the domains to be added (Note: seperate with a space if you have multiple domains EG: 'Domain1 Domain2') : ").strip().split(" ")

        f = open("domains.txt", "a")
        for i in range(len(ss)):
            f.write(ss[i])
            f.write("\n")
        f.close()
        print("Domains Added!")


conn = sqlite3.connect(path)

datas = []
cursor = conn.cursor()
cursor.execute("SELECT id,url FROM urls")
urls = cursor.fetchall()

with open("histories.txt", "w") as f:
    f.write("")
f.close()

f = open("histories.txt", "a")

for r in urls:
    f.writelines(str(r))
    f.writelines("\n")
f.close

print("Clearing histories")
cursor.executemany('DELETE from urls WHERE id = ?',getids.datas[0])
conn.commit()
conn.close()
print("CLEARED!")