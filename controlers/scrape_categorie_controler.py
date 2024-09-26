from models.categorie import Categorie


class CategorieScraper:

    def __init__(self, url):

        self.url = url

    def create_categorie(self):
        nom = "Apparel & Accessories"
        categorie = Categorie(nom, self.url)
        categorie.create_folder()
        categorie.get_all_sub_categorie()

    