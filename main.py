import requests
from views.main_nav import MainNav

url = "www.alibaba.com"

def main():
    nav = MainNav(url)
    nav.show_nav()

if __name__ == "__main__":
    main()

