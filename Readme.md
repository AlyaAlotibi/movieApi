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
the test done by *postman*

## Endpoints


1. #### GET /
- *General*:
    - Request Arguments:None
    - Public endpoint
    - Returns message and success value 
- *sample*:`curl http://127.0.0.1:5000/`
- Response body:
```
{
  "message": "Welcome to Alna Movies websit",
  "success": true
}
```

2. #### GET /movies
- *General*:
    - Returns a list of all movies and success value
    - Request Arguments: None
    - require get:movies permission
- *sample*:`curl http://127.0.0.1:5000/movies`
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

3. #### POST /movies/create 
- *sample* `curl http://127.0.0.1:5000/movies/create -X POST -H "Content-Type: application/json" -d '{"title":"Test add movie", "release_date":"August 23, 2021", "type":"Action","image_link":"htt
ps://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg","link":"https://editorial.rottentomatoes.com/article/highest-grossing-movies-all-time/"}'`
- Response body:
```
{
  "created": "Test add movie",
  "success": true

}
```

