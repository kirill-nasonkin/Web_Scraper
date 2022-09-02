import string
import os

import requests
from bs4 import BeautifulSoup


def heading_formatter(sentence: str):
    heading_copy = sentence[:]
    for char in (string.punctuation + '’' + '—'):
        if char in heading_copy:
            heading_copy = heading_copy.replace(char, '')
    heading_copy = heading_copy.replace(' ', '_')
    return heading_copy


def file_creator(page_n: int, heading_and_body: dict):
    project_wd = os.getcwd()
    os.chdir(f".\\Page_{page_n}")
    for heading in heading_and_body:
        with open(f'{heading}.txt', 'wb') as file:
            file.write(heading_and_body[heading])

    print(f"Saved articles: {len(heading_and_body)} ")
    os.chdir(project_wd)


def scrapper(page_n: int, article_type: str):
    list_of_news = []
    list_of_links = []
    heading_and_body = {}

    url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={page_n}"
    url_domen = "https://www.nature.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    span = soup.find_all("span", {'class': 'c-meta__type'})

    for s in span:
        if s.text == f"{article_type}":
            list_of_news.append(s.parent.parent.parent)
    if len(list_of_news) > 0:
        for el in list_of_news:
            list_of_links.append(url_domen + el.a.get("href"))

        for link in list_of_links:
            link_content = requests.get(link).content
            b_soup = BeautifulSoup(link_content, 'html.parser')
            heading_no_format = b_soup.find('h1').get_text().strip()
            heading = heading_formatter(heading_no_format)

            body = b_soup.find("div", {"class": "c-article-body u-clearfix"}).text.strip()
            body = body.encode(encoding='utf-8')
            heading_and_body[heading] = body
        return heading_and_body
    else:
        return None


def main():
    num_of_pages = int(input())
    type_of_articles = input()

    for num in range(1, num_of_pages + 1):
        os.mkdir(f".\\Page_{num}")
        articles = scrapper(num, type_of_articles)
        if articles:
            file_creator(num, articles)
        else:
            continue
    print("Saved all articles.")


if __name__ == "__main__":
    main()
