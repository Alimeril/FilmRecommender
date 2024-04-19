Welcome to one of my favorite personal projects.
"FilmRecommender" is a "html parser" project, where takes the name of your favorite film, and recommend films based on that, using "requests" and "BeautifulSoup" python libraries.

First, after recieving the name of the film, the function below parse it's google search page for the film's imdb link:

![find_imdb_link](https://github.com/Alimeril/FilmRecommender/assets/165685373/1b698a93-2eb3-42a5-b642-1c4f587ff00c)

Then, we wanted to parse the film's imdb page, however, imdb blocks bots to get page source. In this regard, we define a header for the request library to get imdb source:

![Headers](https://github.com/Alimeril/FilmRecommender/assets/165685373/e6d30716-be41-410d-9f37-eabb9d992871)

Now with this header we parse imdb page (with BeautifulSoup) for similar films to recommend:

![recommend_film](https://github.com/Alimeril/FilmRecommender/assets/165685373/c6ded5de-74a6-47c2-a9e0-22cbf261da9a)

After that we can recommend even more films using the list we achived with the imdb page.
