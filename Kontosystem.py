ask_user_acc = input("\n" "Haben Sie schon ein Account? (ja oder nein) ")

#------------------------------------------------------------------------------------------------------

def add_acc():
    user_name_add = input("\n""Benutzername wählen: ")   #Daten input
    user_pwd_add = input("Passwort wählen: ")
    
    with open('benutzer-daten.txt', 'a') as f:
           with open('benutzer-daten.txt', 'a') as f:
               f.write(user_name_add + "|" + user_pwd_add + "\n") #Daten im Txt speichern
               print("Daten wurden gespeichert")

#------------------------------------------------------------------------------------------------------

def log_acc():
     user_name_log = input("Benutzernme: ")             #Daten input
     user_pwd_log = input ("Passwort: ")

     with open('benutzer-daten.txt', 'r') as f:
        for line in f.readlines():
           data = line.strip()
           user, passw = data.split("|")
           print(user)
           print(passw)


           if user == user_name_log and passw == user_pwd_log:
            print("Du bist jetzt eingelogt, " + user)
           else:
              print("Falsches Passwort")
               
#------------------------------------------------------------------------------------------------------         

if ask_user_acc == "nein":          #Wecher Fall liegt vor
   print("Account erstellen...")
                                          
   add_acc()

elif ask_user_acc == "ja":
   log_acc()

else:
    print("Falsche Eingabe")