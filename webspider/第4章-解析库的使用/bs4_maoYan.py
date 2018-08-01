from bs4 import BeautifulSoup
with open("test.html", "r", encoding = "utf-8") as file:
    html = ""
    for line in file:
        html += line

soup = BeautifulSoup(html, "lxml")
print(soup.p.string)