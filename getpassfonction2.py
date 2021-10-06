#LAB : Interface d'authentification avec Python 
# 1) Premieremenet inserer l'username et le mot de passe 
# 2) On doit verifier l'username est admin et verifier le mot de passe # si c'est admin123
# 3) Si la condition est verifie on va afficher le message Bonjour ADMIN, si c'est pas le cas on va afficher "Mot de passe incorrect
from getpass import getpass
import csv
#Fonction litcsv
#Lit le csv dans lesquels sont les users et le met dans un tableau associatif
#renvoie le tableau associatif
def litcsv(file):
  with open(file, mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}
    return dict_from_csv

#Fonction cnx
#Demande username, passord, les vérifie
#retourne résultat de connexion ET message a afficher
def cnx(users):
  #users={'admin': 'admin123', 'toto': 'titi'}
  usr = input("Username: ")
  psw = getpass(prompt='Password: ')
  ret = 0
  msg ="Username ou mot de passe incorrect"
  if (usr in users):
    if(psw==users[usr]):
      ret = 1
      msg = "Bienvenue "+usr
  
  return ret,msg

#MAIN

pswok=0
#charge le fichier des users
users = litcsv("users.txt")
tentatives = 0
while (pswok==0) and (tentatives<3):
  ret = cnx(users)
  tentatives +=1
  pswok = ret[0]
  print(ret[1])
if (tentatives>2):
  print('Compte bloqué')