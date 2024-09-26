import os


class SousCategorie:

    def __init__(self, nom, description, url, categorie):
        
        self.nom =  nom
        self.description = description
        self.url = url 
        self.categorie = categorie 

        def create_folder(self, pathname):
            path = self.nom
            if not(os.path.exists(path)):
                os.makedirs(path)

        def get_all_products(self):
            pass