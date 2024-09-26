from controlers.scrape_defaut_controler import DefaultScraper
from controlers.scrape_categorie_controler import CategorieScraper
class MainNav:

    def __init__(self, url_principale):

        self.url = url_principale

    def show_nav(self):
        while True:
            print("--------------------------------------------------------")
            print("--------------------------------------------------------")
            print("----------------WEB SCRAPER : WELCOME-------------------")
            print("--------------------------------------------------------")
            print("--------------------------------------------------------")
            print('\n')
            print("--------------------------------------------------------")
            print("-------------------------MENU---------------------------\n 1 => Scraper une catégorie \n 2 => Programme par défaut \n 0 => Quitter \n")
            choix = input("Votre choix : ")

            while not choix.isnumeric():
                print("Choix incorrect \n")
                choix = input("Votre choix : \n 1 => Scraper une catégorie \n 2 => Programme par défaut \n")
            
            choix = int(choix)
            if choix ==  0:
                break

            elif choix == 1:
                url = input("Veuillez entrer l'url : ")
                CategorieScraper(url)
                
            elif choix == 2:
                DefaultScraper(self.url)


