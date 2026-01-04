import requests
from bs4 import BeautifulSoup

url = "https://simplylearn.com"

r=requests.get(url)
htmlContent=r.content
print(htmlContent)

soup=BeautifulSoup(r.content, 'html.parser')
for i in soup.find_all('code'):
    print(i.text)

titles=soup.title
print(titles.string)  

print(soup.find('p'))

print(soup.find_all('p'))

a=soup.find_all('a')
for i in a:
    print(i)

print(soup.find('p')['class'])
print(soup.find('p')['id'])

print(soup.find('p').get_text())

print(soup.get_text())

anchor=soup.find_all('a')
print(anchor)

for i in anchor:
    print(i['href'])

all=set()
for i in anchor:
    Text="https://simplylearn.com/"+i.get('href')
    all.add(i)
    print(Text)

root=soup.find(id='root')
print(root)
