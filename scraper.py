import requests
from bs4 import BeautifulSoup

url1 = "https://fr.wikipedia.org/wiki/S%C3%A9n%C3%A9gal"
def RecupereHTML():
    recupere = requests.get(url1)
    soup = BeautifulSoup(recupere.content, "html.parser")

    print(soup.prettify())


def ExtraireTitre():
    titre = requests.get(url1)
    soup = BeautifulSoup(titre.content, "html.parser")
    title = soup.find('h1').text


    print(title)


print("1\n-----Écrire une fonction pour obtenir et analyser le contenu HTML d'une page Wikipédia-----")
RecupereHTML()

print("2\n-----Écrire une fonction pour extraire le titre de l'article-----")
ExtraireTitre()

print("3\n-----Écrire une fonction pour extraire le texte de l'article pour chaque paragraphe avec leurs titres respectifs.-----")
print("-----Mapper ces titres à leurs paragraphes respectifs dans un dictionnaire.-----")
def Paragraphes():
    titreparagraphe = requests.get(url1)
    soup = BeautifulSoup(titreparagraphe.content, "html.parser")
    paragraphes = soup.find_all('p')
    titres = soup.find_all('div' , class_ = 'mw-heading mw-heading2')
    print(paragraphes)


    for titre in titres:

        titre1 = titre.find('h2').text
        print(titre1)



Paragraphes()
print("4\n-----Écrire une fonction pour collecter chaque lien qui redirige vers une autre page Wikipédia-----")

def LienWikipedia():
    lienpage = requests.get(url1)
    soup = BeautifulSoup(lienpage.content, "html.parser")

    liens = []
    for lien in soup.find_all('a', href=True):
        liens.append(lien['href'])

    for lien in liens:
        print(lien)


LienWikipedia()
print("5\n-----Regrouper toutes les fonctions précédentes en une seule fonction qui prend comme paramètre un lien Wikipédia-----")

def FonctionsMultiples():
    url = "https://fr.wikipedia.org/wiki/France"
    def RecupereHTML():
        recupere = requests.get(url)
        soup = BeautifulSoup(recupere.content, "html.parser")

        print(soup.prettify())

    RecupereHTML()

    def ExtraireTitre():
        titre = requests.get(url)
        soup = BeautifulSoup(titre.content, "html.parser")
        title = soup.find('h1').text

        print(title)

    ExtraireTitre()

    def LienWikipedia():
        lienpage = requests.get(url)
        soup = BeautifulSoup(lienpage.content, "html.parser")

        liens = []
        for lien in soup.find_all('a', href=True):
            liens.append(lien['href'])

        for lien in liens:
            print(lien)

    LienWikipedia()



print("6\n-----Tester la dernière fonction sur une page Wikipédia de votre choix-----")
FonctionsMultiples()