# Flask Application Template

This is a template for building a flash application. 

## Requirements
There are a few environment variables need to be set on your machine.
- FLASK_APP   (set to /your/path/to/app.py)
- DB_USERNAME   (Database username)
- DB_PASSWORD   (Database password)
- DB_HOST       (Database host)
- DB_DATABASE   (Database)
- FLASK_SECRET_KEY   (Secret key)

## To set up an virtual environment
python -m venv venv

## Install required packages
pip install -r requirements.txt

## To start the development server and run the app
./app.py