from Mailbox import *
import sys
import traceback

if __name__=='__main__':
   print('Exercice 1+2'); print('------------')
   try:
      msg=Message('Messages/msg.eml')
   except:
      print('Erreur exercice 1+2: constructeur')
      print(sys.exc_info()[0])
      #traceback.print_exc(file=sys.stdout)
   try:
      print(str(msg)[:100])
   except:
      print('Erreur exercice 1+2:str')
      print(sys.exc_info()[0])
      #traceback.print_exc(file=sys.stdout)

   print('\nExercice 3'); print('------------')
   try:
      MB=Mailbox('Messages')
   except:
      print('Erreur exercice 3: constructeur')
      print(sys.exc_info()[0])
      #traceback.print_exc(file=sys.stdout)
   try:
      print(len(MB))
   except:
      print('Erreur: Classe Mailbox: longueur')
      print(sys.exc_info()[0])
      #traceback.print_exc(file=sys.stdout)
   try:
      for i,m in enumerate(MB): 
         if i<5: print(str(m)[:50]+'...')
   except:
      print('Erreur: Classe Mailbox: iterateur')
      print(sys.exc_info()[0])
      #traceback.print_exc(file=sys.stdout)

   print('\nExercice 4'); print('------------')
   try:
      os.system("./pays_plus_frequents Messages 3")
   except: 
      print('Erreur: pays_plus_frequents')
      print(sys.exc_info()[0])

   print('\nExercice 5'); print('------------')
   for root, dir, files in os.walk("Messages/PetiteBoite"):
       for msg in files:
        try:
          os.system("./duree_acheminement Messages/PetiteBoite/" + msg)
        except: 
          print('Erreur: duree_acheminement '+ msg)
          print(sys.exc_info()[0])

   print('\nExercice 6'); print('------------')
   try:
      os.system("./max_acheminement Messages")
   except: 
      print('Erreur: max_acheminement')
      print(sys.exc_info()[0])

   print('\nExercice 7'); print('------------')
   try:
      os.system("./cote_moy_spam Messages")
   except: 
      print('Erreur: cote_moy_spam')
      print(sys.exc_info()[0])
  
   print('\nExercice 8'); print('------------')
   try:
      os.system("./msg_par_jour Messages")
   except: 
      print('Erreur: msg_par_jour')
      print(sys.exc_info()[0])

   print('\nExercice 9'); print('------------')
   try:
      os.system("./archivage Messages Archive")
   except: 
      print('Erreur: archivage')
      print(sys.exc_info()[0])

   print('\nExercice 10'); print('------------')
   try:
      os.system("./spams_proches Messages/PetiteBoite gzip gunzip gz")
   except: 
      print('Erreur: comparaison de mails')
      print(sys.exc_info()[0])
      
