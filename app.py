import gestion_stock as gs
import os


class App:
        def __init__(self):
            self.s = gs.Stock('data.txt')
            self.menu_charger()

        def run(self):
            stop = False
            while not stop:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('=====================================')
                print('Nouveau produit :(n)')
                print('Supprimer produit :(s)')
                print('Vendre produit :(v)')
                print('Acheter produit :(a)')
                print('Afficher les produits(d)')
                print('Pour trier (t)')
                print("N’importe autre touche pour quitter")
                print('=====================================')
                choix = input('Choisir une operation: ')
                if choix == 'n':
                    self.menu_nouveau()
                elif choix == 's':
                    self.menu_supprimer()
                elif choix == 'v':
                    self.menu_vendre()
                elif choix == 'a':
                    self.menu_acheter()
                elif choix == 'd':
                    self.menu_afficher()
                elif choix == 't':
                    self.menu_tri()
                else:
                    stop = True
                    self.menu_quitter()
                os.system('cls' if os.name == 'nt' else 'clear')

        def menu_nouveau(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            code = input('Entrer le code:')
            nom = str(input('Entrer le nom'))
            prix_unitaire = float(input('Entrer le prix unitaire'))
            tva = float(input('Entrer la TVA'))
            quantite = int(input('Entrer la quantite'))
            prod = gs.Produit(code, nom, prix_unitaire, tva, quantite)
            resultat = self.s.nouveau(prod)
            if resultat == True:
                print('Un nouveau produit a été crée!')
            else:
                print('Impossible de créé un produit existant!!')
            input('Taper pour continuer ..........')
            os.system('cls' if os.name == 'nt' else 'clear')

        def menu_supprimer(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            code = input('Entrer le code du produit a supprimer:')
            resultat = self.s.supprimer(code)
            if resultat:
                print('Suppression avec succées')
            else:
                print('Suppresion a échoué')
            input('Taper pour continuer ..........')
            os.system('cls' if os.name == 'nt' else 'clear')

        def menu_vendre(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            code = input('Entrer le code du produit a vendre:')
            q = input('Entrer la quantite a vendre:')
            resultat = self.s.vendre(code, q)
            if resultat:
                print('Produit vendu avec succes')
            else:
                print('vente echoué')
            input('Taper pour continuer ..........')
            os.system('cls' if os.name == 'nt' else 'clear')

        def menu_acheter(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            code = input('Entrer le code du pproduit a acheter:')
            q = input('Entrer quantite :')
            resultat = self.s.acheter(code, q)
            if resultat:
                print('Achat avec succes')
            else:
                print('Achat echoue')
            input('Taper pour continuer ..........')
            os.system('cls' if os.name == 'nt' else 'clear')

        def menu_afficher(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            self.s.afficher()
            input('Taper pour continuer ..........')
            os.system('cls' if os.name == 'nt' else 'clear')

        def menu_quitter(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            self.s.enregistrer()
            input('Taper pour continuer ..........')
            os.system('cls' if os.name == 'nt' else 'clear')

        def menu_charger(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print('wtf')
            self.s.charger()
            input('Taper pour continuer ..........')
            os.system('cls' if os.name == 'nt' else 'clear')

        def menu_ajouter(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            code = input('Entrer le code du produit a ajouter')
            self.s.ajouter(code)
            input('Taper pour continuer ..........')
            os.system('cls' if os.name == 'nt' else 'clear')

        def menu_tri(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            self.s.tri()
            self.s.afficher()
            os.system('cls' if os.name == 'nt' else 'clear')


a = App()
a.run()
