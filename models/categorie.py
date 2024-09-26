import os


class Categorie:

    def __init__(self, nom, url):
        
        self.nom =  nom
        self.url = url 

        def create_folder(self, pathname):
            path = os.path.join(pathname, self.nom)
            if not(os.path.exists(path)):
                os.makedirs(path)

        def get_all_sub_categorie(self):
            pass



