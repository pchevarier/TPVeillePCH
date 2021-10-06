import requests
import json

r=requests.get("https://jsonplaceholder.typicode.com/todos")
#print(r)
#print(r.text)
#print(r.json())
#print(r.data())
resu = dict()
iresu = 0
arr= r.json()
print ("Nombre de lignes a analyser:"+str(len(arr)))
with open("users.txt", "w") as fuser:
  with open("usersfiltred.json", "w") as ffiltred:
    for lig in arr:
      fuser.write(str(lig["userId"])+"\n")
      if (lig["completed"]):
        print (str(lig["userId"])+" "+str(lig["id"])+" "+lig["title"])
        resu[lig["id"]] = lig.copy()
        ffiltred.write(json.dumps(lig))

print("Nombre de lignes sélectionnées: "+str(len(resu)))
