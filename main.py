from bs4 import BeautifulSoup
import lxml
import requests


with open("website.html", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

print (soup.title.string)
print (soup.p)


all_anchor_tags =  soup.findAll(name="a")
print (all_anchor_tags)

for tag in all_anchor_tags:
    print (tag.get("href"))

heading = soup.find(name="h1", id="name")
print (heading)

section_heading = soup.find(name="h3", class_="heading")
print (section_heading.text)

company_url = soup.select_one(selector="p a")
print (company_url)

# selecting all class="heading" - results in a list of elements
headings = soup.select(".heading")
print (headings)

# new exercise getting a hold of live website - https://news.ycombinator.com/

response = requests.get("https://news.ycombinator.com/news")

news_html = response.text
soup_news = BeautifulSoup(news_html, "html.parser")

headlines = soup_news.find_all(class_="titleline")
upvotes = soup_news.find_all(class_="score")
upvotesint = []
for i in range(len(upvotes)):
    upvotesint.append(int(upvotes[i].get_text().split()[0]))
print(len(headlines))
print(len(upvotes))
for i in range(min(len(headlines), len(upvotes))):
    print(headlines[i].a.get_text())
    print(headlines[i].a.get("href"))
    print(upvotes[i].get_text())

max_index = upvotesint.index(max(upvotesint))
print(headlines[max_index].a.get_text())
print(headlines[max_index].a.get("href"))
print(upvotes[max_index].get_text())


# project - create a list of 100 top movies from https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/

response2 = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movies_html = response2.text
movies_data = BeautifulSoup(movies_html, "html.parser")

movie_titles = movies_data.find_all(name="h3", class_="title")
print(movie_titles)
title_list = []
for title in movie_titles:
    title_list.append(title.get_text())
    print(title.get_text())

# now , write the list to a file - movies.txt
with open("movies.txt", "w",encoding="utf-8") as file:
    for title in reversed(title_list):
        file.write(title + "\n")