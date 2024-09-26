from models.categorie import Categorie


class DefaultScraper:

    def __init__(self, url):

        self.url = url

    # ttfyffyffyfyfyfyfyfyfyff
    def get_categories(self):
        """
        dfghdfghdfghj
        dfghjfghjfghjfghhgjjhjhghghgg
        """
        categories = [("Apparel & Accessories", "url"), ()]
        for categorie in categories:
            categorie = Categorie(categorie[0], categorie[1])
            categorie.create_folder()
            categorie.get_all_sub_categorie()

    