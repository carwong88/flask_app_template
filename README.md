# Flask Application Template

This is a template for building a flash application. 

## Steps to set up the environment
1. Download the zip file and extract it

2. Rename the flask_app_template to your project name

3. Setup a virtual environment under your project<br>
  `python -m venv venv`

4. Install required packages<br>
  `Remove the last line "uwsgi" from the requirements.txt file (That's for deploying on Heroku)`<br>
  `pip install -r .\requirements.txt`

5. Set up environment variables on your machine (See Environmnet Variables)

6. Start the development server and run the app<br>
  `./app.py`

## Environmnet Variables
There are a few environment variables need to be set on your machine.
- FLASK_APP   (set to /your/path/to/app.py)
- DB_USERNAME   (Database username)
- DB_PASSWORD   (Database password)
- DB_HOST       (Database host)
- DB_DATABASE   (Database)
- FLASK_SECRET_KEY   (Secret key)

## Steps to create a new view (Example here is 'projects')

#### 1. Create a blueprint file under views
>`File: views\projects.py`

```
from flask import Blueprint, render_template

projects = Blueprint('projects', __name__)

@projects.route('/')
def home():
  return render_template('projects.html', title='Projects')
```

#### 2. Create a template file under templates

>`File: templates\projects.html`

```
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h1>
  This is my {{ title }} page.
</h1>
{% endblock %}
```

#### 3. Register the blueprint in init file

>`File: __init__.py`

```
from src.views.projects import projects
  app.register_blueprint(projects, url_prefix='/projects')
```

#### 4. Check your new view render successfully

>`http://127.0.0.1:5000/projects/`
