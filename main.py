from bs4 import BeautifulSoup
import requests
results=requests.get("https://subslikescript.com/movie/Titanic-120338")
content=results.text
soup=BeautifulSoup(content,'lxml')

box=soup.find('article',class_='main-article')
title=box.find('h1').get_text()
transcript=box.find('div',class_='full-script').get_text()
with open(f'{title}.txt','w', encoding="utf-8") as file:
    file.write(transcript)
