import requests

from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page.status_code)
print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
print('')

print(list(soup.children))
print('')
print([type(item) for item in list(soup.children)])
print('')

html = list(soup.children)[2]
print(list(html.children))
print('')

body = list(html.children)[3]
print(list(body.children))
print('')

p = list(body.children)[1]
print(p.get_text())
