# Prague Music Events - Backend

#### A REST API made with the Django REST Framework.

## Technologies Used

- Python 3
- Django

## Setup/Installation Requirements

From your command line:

```bash
# Clone this repository
$ git clone https://github.com/PaulRoss1/PME-Backend.git

# Go into the repository
$ cd PME-Backend

# Generate a Secret Key
generate a key https://miniwebtool.com/django-secret-key-generator/ 
and place it in settings.py

# Create and activate virtual environment
$ virtualenv env
$ source env/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Run database migrations
$ python manage.py migrate

# Run Django dev server
$ python manage.py runserver

```

## License

The MIT License. Please have a look at the LICENSE.md for more details.
