import requests
import json
from bs4 import BeautifulSoup

res = requests.get("https://panelaterapia.com/") #vai acessar o site usando python
res.encoding = "utf-8" # para ele conseguir identificar caracteres como acentuação e etc.

soup = BeautifulSoup (res.text, 'html.parser') # estanciando beatifulsoup e transformando objetos de texto em html

links = soup.find(class_="pagination").find_all('a')
all_pages = []
for link in links:
    page = res.request.get(link.get('href'))
    all_pages.append(BeautifulSoup(page.text, 'html.parser'))

print(len(all_pages))
#print(res) # mostra se o site ta respondendo ou n
#print(res.text) # mostra o código html do site

all_posts = []

# find mostra a primeira ocorrência que encontra
# find_all encontra varias ocorrências e retorna um array

for posts in all_pages: # percorrendo todas as páginas
    posts = soup.find_all(class_="post") # Pesquisa os elementos que tem a classe "post"
    for post in posts: # percorrendo os posts de cada página
        info = post.find(class_="post-content")
        title = info.h2.text
        preview = info.p.text
        author = info.find(class_="post-author")
        time = info.find(class_="post-date")['datetime']
        all_posts.append({
            'title':title, 
            'preview':preview, 
            'author':author,
            'time': time
        })
    
print(all_posts)
#salvar dentro de um arquivo JSON
# with open('nome do arquivo','escrever') referenciado aqui pela variável nome_variavel:
with open('posts.json','w') as json_file:
    json.dump(all_posts, json_file, indent=3, ensure_ascii=False)