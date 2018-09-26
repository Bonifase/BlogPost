# Project Title
BlogPost Application.

# Project Description
BlogPost provides a platform that brings individuals together.
This platform creates awareness for varius expriences and gives the users the ability to write comments about the daily experiences they have interacted with. 


## Getting Started

1. Clone and download the project from the github.
2. To get started, Create a virtual environment for your project.

### Prerequisites

1. Create a requirements.txt file to store your dependencies.
2. Setup Flask.
3. Setup Pylint 
4. Setup unit testing libraries and ensure minimal tests 
5. Setup PostgreSQL
6. Setup SQLAlchemy

8. freeze the installed packages and store this setup in a requirements.txt file: use pip freeze > requirements.txt

## Installing

1. Install the latest version of Python 3
2. Use a virtual environment to manage the dependencies for your project, both in development and in production.
3. Install virtualenv use: virtualenv venv. On Windows: \Python36\Scripts\virtualenv.exe venv
4. Activate the environment: .venv/bin/activate. On Windows: venv\Scripts\activate
5. Install Flask: Within the activated environment, use the following command to install Flask: pip install Flask
6. copy the folder containing the files of the application into the virtual environment folder.
7. Run the application using the command: python app.py
8. To stop the server process, press control+C.

## Running the tests
1. Use nosetests to manually test the application
2. Navigate to the directory where the api folder is located using the terminal
3. Run the nosetests command in the terminal

## Deployment

1. Use Heroku for deployment. 
2. Sign up, Download and install the Heroku CLI and then upload our app to the platform effortlessly.
3. Login into the Heroku Cli by running this command in the terminal: heroku login
4. Add a Procfile to that application.
5. Update the requirements file by running: pip freeze > requirements.txt
6. Add this line of code: web: gunicorn app:app
7. In the application folder run this command: heroku create WeConnect-api-heroku.
8. WeConnect is the name of the application, this has to be unique across Heroku. 

## Built With

 * [Flask](http://flask.pocoo.org/)- The web framework used

 * [Bootstrap](https://getbootstrap.com/)- An open source toolkit for developing with HTML, CSS, and JS.


## Versioning

This is the first v1 

## Authors

* **Bonifase Orwa** - *Initial work* - [BlogPost](https://github.com/Bonifase/BlogPost)

## License

This is a free open source application with no license

## Acknowledgments
* Bootstrap CDN
* LFAs
* Team members
