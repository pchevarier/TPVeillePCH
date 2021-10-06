import requests
r=requests.get("https://jsonplaceholder.typicode.com/todos")
#print(r)
#print(r.text)
#print(r.json())
#print(r.data())
arr = r.json()
for lig in arr:
  if (lig["completed"]==1):
    print (str(lig["userId"])+" "+str(lig["id"])+" "+lig["title"])