# Programme utilisant la méthode REST API pour obtenir le nom des questions de la première page StackOverFlow ainsi que leur sondage respectif sur la première page, à l'aide de l'outil Developpeur du navigateur.
# Pour obtenir le même résultat sur les autres pages, il faudrait faire une itération en utilisant le numéro de la dernière page.

import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
for question in questions:
    print((questions[0]).select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
