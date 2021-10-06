#LAB : Interface d'authentification avec Python 
# 1) Premieremenet inserer l'username et le mot de passe 
# 2) On doit verifier l'username est admin et verifier le mot de passe # si c'est admin123
# 3) Si la condition est verifie on va afficher le message Bonjour ADMIN, si c'est pas le cas on va afficher "Mot de passe incorrect
from getpass import getpass
#Fonction cnx
#Demande username, passord, les vérifie
#retourne résultat de connexion ET message a afficher
def cnx():
  usr = input("Username: ")
  psw = getpass(prompt='Password: ')
  if((usr=="admin") and (psw=="admin123")):
    ret = 1
    msg = "Bienvenue "+usr
  else:
    ret = 0
    msg ="Username ou mot de passe incorrect"
  return ret,msg

#MAIN
pswok=0
while pswok==0:
  ret = cnx()
  pswok = ret[0]

print(ret[1])