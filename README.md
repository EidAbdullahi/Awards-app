# Title
Awards
# Description
Awward is a website that allows people to present their websites to be critiqued by other developers and users.Here is the live link: https://eid-awards.herokuapp.com/

# Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- Heroku
- Postgresql
- Django

# Setup and installations
Prerequisites
Python3.6
virtualenv
Pip
Clone the Repo and rename it to suit your needs.
git clone https://github.com/EidAbdullahi/Awards-app
Initialize git and add the remote repository
```
git init
git remote add origin <your-repository-url>
Create and activate the virtual environment
python3.8 -m virtualenv virtual
source virtual/bin/activate
```
Setting up environment variables
# Create a .env file and paste paste the following filling where appropriate:
```
SECRET_KEY='<YOUR_SECRET_KEY_HERE>
DEBUG=True #set to false in production
DB_NAME=<YOUR_DATA_BASE_NAME>
DB_USER=<YOUR_DATA_BASE_USER>
DB_PASSWORD=<YOUR_DATA_BASE_PASSWORD>
DB_HOST='127.0.0.1'
MODE='dev' #set to 'prod' in production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

Install dependancies
Install dependancies that will create an environment for the app to run
```
pip install -r requirements.txt
Run migrations
python manage.py migrate
Run the app
python manage.py runserver
Access the application through localhost:8000
Open localhost:8000
```
# Contributing
Please read this comprehensive guide on how to contribute. Pull requests are welcome :-)

# Bugs
Create an issue mentioning the bug you have found


# Support and contact details
Contact Eid Abdullahi for further help/support

License
MIT

Copyright (c)2020 Eid Abdullahi

# About
Awward is a website that allows people to present their websites to be critiqued by other developers.

https://eid-awards.herokuapp.com/

# Resources
 Readme
# License
 MIT License
# Releases
No releases published
# Packages
No packages published
# Languages
HTML
72.5%
 
Python
27.5%
