class Produit :
    def __init__(self, code, nom, prix_unitaire, tva, quantite):
        self.code = code
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.tva = tva
        self.quantite = quantite

    def incrementer_quantite(self, q):
        self.quantite += q

    def decrementer_quantite(self, q):
        self.quantite -= q

    def afficher(self):
        print('| %-8s | %-8s | %-8.3f | %-8.3f | %-8d |'% (str(self.code), self.nom, self.prix_unitaire, self.tva, self.quantite))

class Stock():
    def __init__(self, nom_f):
        self.produits = []
        self.nom_f = nom_f

    def rechercher(self,code):
        return (True, self.produits.index(code)) if code in self.produits else (False, 'h')

    def supprimer(self,code):
        self.produits.remove(code)
        return not code in self.produits

    def ajouter(self,code):
            self.produits.append(code)

    def vendre(self, code, q):
        if self.rechercher(code)[0] and not self.produits[self.rechercher(code)[1]].quantite < 0:
            self.produits[self.rechercher(code)[1]].decrementer_quantite(q)
            return True
        else:
            return False

    def acheter(self, code, q):
        if self.rechercher(code):
            self.produits[self.rechercher(code)[1]].incrementer_quantite(q)
            if self.quantite > 100:
                self.produits[self.rechercher(code)[1]].decrementer_quantite(q)
                return False
            return True
        else:
            return False

    def nouveau(self,prod):
        if not self.rechercher(prod.code)[0]:
            self.ajouter(prod)
            return True
        else:
            return False


    def afficher(self):
        if len(self.produits)>0:
            for p in self.produits:
                p.afficher()
            print('La liste est terminé!')
        else:
            print('Pas de produits a affichier')

    def enregistrer(self):
        file = open(self.nom_f,'w')
        for p in self.produits:
            file.write(p.code + ";" + p.nom + ";" + str(p.prix_unitaire) +";" + str(p.tva) + ";" + str(p.quantite) + "\n")
        file.close()
        print("Les donnes sont enregistres !!")

    def charger(self):
        try:
            file = open(self.nom_f, 'r')
            EOF = False
            while not EOF:
                line = file.readline()
                if line != '':
                    liste = line.split(';')
                    code = liste[0]
                    nom = liste[1]
                    prix_unitaire = float(liste[2])
                    tva = float(liste[3])
                    quantite = int(liste[4])
                    p = Produit(code, nom, prix_unitaire, tva, quantite)
                    self.produits.append(p)
                else:
                    EOF = True
            file.close()
            print('Les données sont chargés')
        except :
            print("Pas de données a charger")

    def tri(self):
        if len(self.produits)>=2:
            for i in range(len(self.produits)-2):
                for j in range(len(self.produits)-1):
                    if self.produits[i].prix_unitaire < self.produits[j].prix_unitaire:
                        temp = self.produits[i]
                        self.produits[i] = self.produits[j]
                        self.produits[j] = temp

