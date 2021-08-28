# Alna Movies 

## FSND Capstone project 

This is the final project in FSND from Udacity.It is a movie website to view movies and actors

## Getting Started
### heroku url 
- `https://myproject511.herokuapp.com/`

#### Installing Dependencies
### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Endpoints


1. #### GET /
- *General*:
    - Request Arguments:None
    - Public endpoint
    - Returns message and success value 
- *sample*:`curl http://127.0.0.1:5000/api`
- Response body:
```
{
  "message": "Welcome to Alna Movies websit",
  "success": true
}
```
3. #### GET /movies
- *General*:
    - Display All movies 
    - Request Arguments: None
    - require get:movies permission
4. #### GET /api/movies
- *General*:
    - Returns a list of all movies and success value
    - Request Arguments: None
    - require get:movies permission
- *sample*:`curl http://127.0.0.1:5000/api`
- Response body:
```
{
  "Movies": [
    {
      "id": 1,
      "image_link": "https://horrornews.net/wp-content/uploads/2021/03/The-Scientist-2020-movie-9.jpg",
      "link": "https://horrornews.net/164691/film-review-the-scientist-2020/",
      "main_actor": [],
      "release_date": "August 17, 2020",
      "title": "The Scientist",
      "type": "{Action,Horror}"
    },
    {
      "id": 2,
      "image_link": "https://m.media-amazon.com/images/M/MV5BYWU1MTM4OTktZTU4OS00ZWNiLTk0ZTYtOGM4Y2M3NTVhOGJlXkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_.jpg",
      "link": "https://www.imdb.com/title/tt5715066/",
      "main_actor": [],
      "release_date": "August 17, 2021",
      "title": "Mortal",
      "type": "{Action}"
    }],
  "success": true
}
```
5. #### GET /index
- *General*:
    - Display flash messages
    - Request Arguments: None
    - require post:movies,post:actors permission
6. #### POST /api/m/create 
- *sample* `curl http://127.0.0.1:5000/api/movies/create -X POST -H "Content-Type: application/json" -d '{"title":"Test add movie", "release_date":"August 23, 2021", "type":"Action","image_link":"htt
ps://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg","link":"https://editorial.rottentomatoes.com/article/highest-grossing-movies-all-time/"}'`
- Response body:
```
{
  "created": "Test add movie",
  "success": true

}
```