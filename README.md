Mon Projet Netmiko
Examen Pratique

I. Initialiser un dépôt Git local
1. Créez un nouveau répertoire prenom-nom-netmiko pour votre projet.
$ mkdir miadi-maram-netmiko
$ cd miadi-maram-netmiko
2. Initialisez un dépôt Git dans ce répertoire.
$ git init
II. Ajouter et commiter des fichiers
1. Créez un fichier README.md et ajoutez-y le titre : Mon Projet Netmiko
$ echo "Mon Projet Netmiko" > README.md
2. Ajoutez ce fichier à l'index et commitez-le en utilisant le message "Ajout du fichier
README".
$ git add README.md
$ git commit -m "Ajout du fichier README"
3. Créez un fichier main.py et ajoutez-y un simple script Python : print("Hello, Git!")
$ echo "print'("Hello , Git")" > main.py
4. Ajoutez et commitez ce fichier en utilisant le message "Ajout du script Python principal".
$ git add .
$ git commit -m "Ajout du script Python principal"
5. Affichez tous les commits effectués.
$ git log
III. Créer et fusionner des branches
1. Créez une nouvelle branche feature/netmiko pour ajouter une fonctionnalité.
$ git branch feature/netmiko
2. Modifiez main.py pour inclure une fonction acces_netmiko qui utilise la bibliothèque netmiko pour effectuer les opérations suivantes sur un routeur Cisco C8000V :
$ git switch feature/netmiko

$ vim main.py
Dans le fichier main.py
from netmiko import ConnectHandler
import datetime

def acces_netmiko():
    Cisco_device = {
            "Login": "admin",
            "Pass": "C1sco12345",
            "ssh port": "22",
            "host": "sandbox-iosxr-1.cisco.com",
                   }
ssh = ConnectHandler(**cisco_device)
affiche_interfaces = ssh.send_command("show ip interfaces brief")
print(affiche_interfaces)
x = datetime.datetime.now()
print(x)

print("Hello , Git!")
3. Ajoutez et commitez ces modifications avec le message "Ajout de la fonction
acces_netmiko".
$ git add .
$ git commit -m "Ajout de la fonction acces_netmiko"
4. Revenez à la branche principale (main).
$ git switch master
5. Fusionnez les modifications de la branche feature/netmiko dans main.
$ git merge feature/netmiko




IV. Travailler avec un dépôt distant sur GitHub
2. Ajoutez ce dépôt GitHub comme dépôt distant.
$ git clone https://github.com/MaramMiadi/maram-miadi-netmiko.git
3. Poussez vos commits locaux vers GitHub.
$ git push
3. Poussez vos commits locaux vers GitHub.


