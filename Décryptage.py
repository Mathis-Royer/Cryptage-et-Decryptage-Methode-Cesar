import os
import matplotlib.pyplot as plt

#déclaration du répertoire courant à compléter en remplaçant \ par /
os.chdir("C:/Users/royer/Dropbox/INFO/TP/TP8 - Lecture-Ecriture de fichiers/8_TP_fichiers")

#définition de [alphabet]
alphabet="abcdefghijklmnopqrstuvwxyz"

def decal(lettre,dec):
    if lettre in alphabet:           #si lettre est un caractère normal on applique le décalage
        ind=alphabet.index(lettre)   #position du caractère lettre dans l'alphabet
        newind=(ind+dec)%26          #position du caractère de remplacement
        lettre_dec=alphabet[newind]
    else:                            #sinon on recopie le caractère
        lettre_dec=lettre
    return lettre_dec

def decrypt_cesar(code,dec):
    mess=""
    for i in range(len(code)):       #procédure de décryptage
        mess=mess+decal(code[i],dec) #ajout du caractère décodé
    return mess


message = open("message_crypte.txt", "r")   #Ouverture du texte crypté par la méthode Cesar
MESSAGE = message.read()


def Cesar(code,j):  #Fonction de cryptage d'un message par la fonction césar
    mess=""
    for i in range(len(code)):
        mess=mess+decal(code[i],j)
    print (mess)

for K in range(1,27):   #Affichage des différents résultats de décryptage
    print(decrypt_cesar(MESSAGE,K),K)