import re
import requests
from bs4 import BeautifulSoup
import random

HEADERS1 = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure_Requests": "1"
}

def find_imdb_link(film:str):
    search_words = film.split(' ')
    url = 'https://www.google.com/search?client=firefox-b-d&q='
    for w in search_words:
        url = url + w + '+'
    url += 'film'
    # TODO: use try and except for cases that cannot find the link
    req = requests.get(url)
    soup = BeautifulSoup(req.text,'html.parser')
    imdb_tag = soup.find(href = re.compile("imdb"))
    imdb_tag = str(imdb_tag)
    pattern = r'https.+?imdb[\d\w\./]+'
    match = re.search(pattern,imdb_tag)
    link = match.group()
    return link

# def full_title(imdb_link):
#     req = requests.get(imdb_link,headers=HEADERS1)
#     soup = BeautifulSoup(req.text,'html.parser')
#     title = str(soup.find("title"))
#     pattern = r"<title>(.+) - IMDb</title>"
#     match = re.search(pattern,title)
#     return match.group(1)

def recommend_films(imdb_link):
    req = requests.get(imdb_link,headers=HEADERS1)
    soup = BeautifulSoup(req.text,'html.parser')
    class_links = soup.find_all("a", class_="ipc-lockup-overlay ipc-focusable")
    films = []
    for link in class_links:
        match = re.search(r"View title page for (.+?)\"",str(link))
        if match:
            films.append(match.group(1))
            #films.append(full_title(find_imdb_link(match.group(1))))
    return films

def main():
    print("* Welcome to FILM RECOMMENDER *")
    input_film = input("Enter your favorite film (or just a film) to recommend similar films: ")
    imdb_link = find_imdb_link(input_film)
    #print(full_title(imdb_link)+":")
    films = recommend_films(imdb_link)
    for film in films:
        print(film)
    print("**********")
    more = input("More films (y/n): ")
    if more == 'y' or more == 'Y':
        more_films = recommend_films(find_imdb_link(films[random.randrange(len(films)-1)]))
        for film in more_films:
            print(film)
        print("**********")
        more = input("More films (y/n): ")
        if more == 'y' or more == 'Y':
            more_films2 = recommend_films(find_imdb_link(more_films[random.randrange(len(more_films)-1)]))
            for film in more_films2:
                print(film)
            print("**********")
    print("* Enjoy Watching Films *")

if __name__ == "__main__":
    main()