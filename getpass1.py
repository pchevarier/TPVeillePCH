#LAB : Interface d'authentification avec Python 
# 1) Premieremenet inserer l'username et le mot de passe 
# 2) On doit verifier l'username est admin et verifier le mot de passe # si c'est admin123
# 3) Si la condition est verifie on va afficher le message Bonjour ADMIN, si c'est pas le cas on va afficher "Mot de passe incorrect
from getpass import getpass
usr = input("Username: ")
psw = getpass(prompt='Password: ')

if((usr=="admin") and (psw=="admin123")):
  print("Bonjour "+usr)
else:
  print("Username ou mot de passe incorrect")
print("fin")