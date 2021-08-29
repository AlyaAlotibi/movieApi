# Alna Movies 

## FSND Capstone project 

This is the final project in FSND from Udacity.It is a movie website to view movies and actors

## Getting Started
### heroku url 
- `https://myproject511.herokuapp.com/`
### Auth login
- 
`https://practic-misk.us.auth0.com/authorize?audience=alnamovies&response_type=token&client_id=Ol5KiSwXzzggvTnfWX4ygxPRtjAbUuMS&redirect_uri=https://127.0.0.1:5000/index `
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

## Error Handling
Errors are returned as JSON objects in the following format
- success: False.
- error: error code number.
- message: error message string giving description about the kind of error.
- *sample:*
```
{
    "error": 401,
    "message": "Unauthorized",
    "success": false
}
```
The API will return four error types when requests fail:
1. 404: resource not found
2. 422: unprocessable
3. 401: Unauthorized
#### example of error 
if the user inter `curl http://127.0.0.1:5000/movies/create -X POST` and he does not have post:movies
- Response body:
```
{
  "error": 401,
  "message": "Unauthorized",
  "success": false
}
```
## Test
the test done by
1. *postman*
To run the RBAC tests, just import the collection in Postman and run it. 
2. python unittest library 
To run test `python -m unittest`
## Roles and permessions 
  - There are 3 Roles:
  1. MOVIE_PRODUCER with 
    `
        "permissions": 
            "delete:actors",
            "delete:movies",
            "get:actors",
            "get:movies",
            "patch:actors",
            "patch:movies",
            "post:actors",
            "post:movies" 
        `
 `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZ4V2lPODRWcHBHN1llWEtSRnFuQyJ9.eyJpc3MiOiJodHRwczovL3ByYWN0aWMtbWlzay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBkZDI5Y2FhNzhiN2EwMDcwNmI4NGUzIiwiYXVkIjoiYWxuYW1vdmllcyIsImlhdCI6MTYzMDI2MTE0MiwiZXhwIjoxNjMwMzQ3NTQyLCJhenAiOiJPbDVLaVN3WHp6Z2d2VG5mV1g0eWd4UFJ0akFiVXVNUyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.JZ4Ih-Wd0uLnQC3RvvSYTkEUrm6PcS8QT6UqzVgrnVQsw9oGdWTNuT6yc7tJR0mdNCQ8I8Dtc2NxPDPjyy3qmklmJf-TjhJbcW1Ja_RUN4dy7IGgwwct2dQ1esexKNBfFo4Tzq5QzC1SmR-YJUfblC5jnp42avw6XffzvCgYfbupd4dkuomXak-AneekwtQ8zVrUOTLI3LvajGC5qw2-vtFsLo6N0EH6XTM0ui7VF133v-Qck6Uu2-zaQSy_xZ8g1FTHI1QpzZRwXCTV0Mn8Iix4BIqFGRJAz737HuQBJEyQsae9X-IPf7pa-gwkz7E4Dj1TYdt8mQuwTLzGC6rTgg`
  2. MOVIE_ASSISTANT with 
       
 
       ` "permissions": 
        "get:actors",
        "get:movies"
        `
`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZ4V2lPODRWcHBHN1llWEtSRnFuQyJ9.eyJpc3MiOiJodHRwczovL3ByYWN0aWMtbWlzay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBlNDQ1ZTQ2OGRhYmMwMDY5MGEzMjU3IiwiYXVkIjoiYWxuYW1vdmllcyIsImlhdCI6MTYzMDI2MTg3MSwiZXhwIjoxNjMwMzQ4MjcxLCJhenAiOiJPbDVLaVN3WHp6Z2d2VG5mV1g0eWd4UFJ0akFiVXVNUyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.VbQN2ml6jOH2IKbMbRNNkNT9Jk_2KGOrwjpw4JqSRizU7OFYV8EyFpcJmklo-gg1VWyi3DGC2EJCEIQ3FffrVYkdWy18KJ7-A16WPo0rcRvID8bUskXTwWAiALMgbdjCss336qF6nUhkgtqElr1O6P5U1BlGer4kGykNc-nSz-L76FfMrJwXkMkrpEzxcIr1X5PrLHMECuyDQNt_BvNBGdAGlqwaJl1Zr20mJ6quhcYgsd0PVDWri9t6Cd-LqGVdv4fzzciIJj-ZFZEtiPnaVDwh0qBAb5prh0cZHoHvv40lWrlLfZK2RerR4tr9OHYPENcZzuZMFJLVZFkEZ4lDzw`
  3. MOVIE_DIRECTOR with 
    `
      "permissions": [
        "delete:actors",
        "get:actors",
        "get:movies",
        "patch:actors",
        "patch:movies",
       "post:actors"
    `
 `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZ4V2lPODRWcHBHN1llWEtSRnFuQyJ9.eyJpc3MiOiJodHRwczovL3ByYWN0aWMtbWlzay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYmQzZGE3OTllNzAwMDcwODFhYWEwIiwiYXVkIjoiYWxuYW1vdmllcyIsImlhdCI6MTYzMDI2MjMwMywiZXhwIjoxNjMwMzQ4NzAzLCJhenAiOiJPbDVLaVN3WHp6Z2d2VG5mV1g0eWd4UFJ0akFiVXVNUyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.EkAiP2HOJb_wATLpO9lXJEny9fTPRypwbyAYWuHPRTVBWzY_pVZiO8QFzMbQrEuor2uymlqxrqDHeqYcWLY6ntJtpejMOnXi3qAuvHmxFDq6I7VNJtQR8gciLXvChJtn9CwuRUAO-vhtgxnAAoz6C50KrU-QoFGf-Q8Lv6BvDbpAdzG7XkM-hd0JvljI5rqbYpwiVWyyo9lGIrX3Lh72jxMy2YZC2UDB_sCHsHfUJAVDubQQN60m40iVfv8-tder08V8RbABRDYZ1RZhWLrPRLreI8Pmh-20Z3wQN-dxXosmMkoRZrgiYH5eEnmTxomZQooZk5EsJuxpEL0EK1rZeQ`


    
## Endpoints


1. #### GET /
- *General*:
    - Request Arguments:None
    - Public endpoint
    - Returns html page  

2. #### GET /movies
- *General*:
    - Returns a list of all movies and success value
    - Request Arguments: None
    - require get:movies permission 
- *sample*:In alnaMovies.postman_collection file
- Response body:
```
{
    "Movies": [
        {
            "id": 1,
            "image_link": "https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg",
            "link": "https://editorial.rottentomatoes.com/article/highest-grossing-movies-all-time/",
            "main_actor": [],
            "release_date": "August 23, 2021",
            "title": "Test new movie",
            "type": "Action"
        }
    ],
    "success": true
}
```
3. #### GET /actors 
- *General*:
    - Returns a list of all actors and success value
    - Request Arguments: None
    - require get:actors permission
- *sample*:In alnaMovies.postman_collection file
- Response body:
```
{
    "Actors": [
        {
            "gender": "Female",
            "id": 1,
            "image_link ": "https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg",
            "movie_id": 4,
            "name": "Test new actor"
        },
        {
            "gender": "Female",
            "id": 2,
            "image_link ": "https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg",
            "movie_id": 2,
            "name": "Test new actor1"
        }
    ],
    "success": true
}
```
4. #### POST /movies_create 
- *General*:
    - Returns title of movie created and success value 
    - require post:movies permission
    - Request Arguments: a key/value object whit the 
    following {
        - title: (type:string) containing the title of the movie .
        - type: (type:string) containing type of the movie e.g:Action.
        - release_date: (type:DateTime) date of release the movie.
        - image_link:(type:string) link of movie img.
        - link:(type:string) link of movie .
    }
- *sample* In alnaMovies.postman_collection file
- Response body:
```
{
  "created": "Test add movie",
  "success": true

}
```
5. #### POST /actors_create 
- *General*:
    - Returns name of the actor created and success value
    - require post:actors permission 
    - Request Arguments: a key/value object whit the following {
        - name: (type:string) containing the name of the actor .
        - gender: (type:string) containing gender .
        - image_link:(type:string) link of movie img.
        - movie_id:(type:integer) ForeignKey of movie id.
    }
- *sample* In alnaMovies.postman_collection file
- Response body:
```
{
    "created": "Test add actor3",
    "success": true
}
```
6. #### PATCH /movies/<int:movies_id>
- *General*:
    - Returns a list of movies and success value 
    - require patch:movies permission
    - Request Arguments: movies_id *required*in the url and in the body a key/value object whit the following {
        - title: (type:string) containing new value of the title  .
        - type: (type:string) containing type of the movie e.g:Action.
        - release_date: (type:DateTime) date of release the movie.
        - image_link:(type:string) link of movie img.
        - link:(type:string) link of movie .
    }
- *sample* In alnaMovies.postman_collection file
- Response body:
```
{
    "Movies": [
        {
            "id": 1,
            "image_link": "https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg",
            "link": "https://editorial.rottentomatoes.com/article/highest-grossing-movies-all-time/",
            "main_actor": [
                "Test add actor0",
                "Test add actor1"
            ],
            "release_date": "August 23, 2021",
            "title": "Test new movie",
            "type": "Action"
        },
        {
            "id": 2,
            "image_link": "https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg",
            "link": "https://editorial.rottentomatoes.com/article/highest-grossing-movies-all-time/",
            "main_actor": [
                "Test add actor2",
                "Test add actor3"
            ],
            "release_date": "August 23, 2021",
            "title": "Test new7 movie",
            "type": "Action"
        },
        {
            "id": 4,
            "image_link": "https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg",
            "link": "https://editorial.rottentomatoes.com/article/highest-grossing-movies-all-time/",
            "main_actor": [],
            "release_date": "August 23, 2021",
            "title": "Test new1 movie1",
            "type": "Action"
        },
        {
            "id": 3,
            "image_link": "https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg",
            "link": "https://editorial.rottentomatoes.com/article/highest-grossing-movies-all-time/",
            "main_actor": [],
            "release_date": "August 23, 2021",
            "title": "edit movie",
            "type": "Action,Drama"
        }
    ],
    "success": true
}
```
7. #### PATCH /actors/<int:actors_id>
- *General*:
    - Returns a list of Actors and success value 
    - require patch:actors permission
    - Request Arguments: actors_id *required* in the url and for body request  a key/value object whit the following {
        - name: (type:string) containing the name of the actor .
        - gender: (type:string) containing gender .
        - image_link:(type:string) link of movie img.
        - movie_id:(type:integer) ForeignKey of movie id.
    }

    - *sample* In alnaMovies.postman_collection file
    - Response body:
```
{
    "Actors": [
        {
            "gender": "Female",
            "id": 2,
            "image_link ": "https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg",
            "movie_id": 4,
            "name": "Test edit actor"
        },
        {
            "gender": "Female",
            "id": 1,
            "image_link ": "https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg",
            "movie_id": 2,
            "name": "Test edit actor1"
        }
    ],
    "success": true
}
```
8.  #### DELETE /actors/<int:actors_id>
- *General*:
    - Returns id of deleted actor and success value 
    - require delete:actors permission
    - Request Arguments: actors_id *required*
- *Sample*: In alnaMovies.postman_collection file
- Response body:
```
{
    "delete": 1,
    "success": true
}

```
9.  #### DELETE /movies/<int:movies_id>
- *General*:
    - Returns id of deleted movie and success value 
    - require delete:movies permission
    - Request Arguments: movies_id *required*
- *Sample*: In alnaMovies.postman_collection file
- Response body:
```
{
    "delete": 1,
    "success": true
}

```