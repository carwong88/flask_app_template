# Flask Application Template

This is a template for building a flash application. 

## Steps to set up the environment
1. Download the zip file and extract it
2. Rename the flask_app_template to your project name
3. Setup a virtual environment under your project
`python -m venv venv`
4. Install required packages
`pip install -r .\requirements.txt`
5. Set up environment variables on your machine (See Environmnet Variables)
6. Start the development server and run the app
`./app.py`

## Environmnet Variables
There are a few environment variables need to be set on your machine.
- FLASK_APP   (set to /your/path/to/app.py)
- DB_USERNAME   (Database username)
- DB_PASSWORD   (Database password)
- DB_HOST       (Database host)
- DB_DATABASE   (Database)
- FLASK_SECRET_KEY   (Secret key)
