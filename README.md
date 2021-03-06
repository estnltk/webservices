# Estnltk webservices
## Weblicht
Estnltk webserver for weblicht.

## Usage

### Run development server

```
python manage.py runserver --settings mysite.settings_dev 0.0.0.0:8000
```

Check http://localhost:8000/analyse/

### Run in production environment with uWsgi server

Run as root user:

```
cd webservices/weblicht
python manage.py collectstatic
cd config
uwsgi --ini weblicht_uwsgi.ini \
      --touch-reload=weblicht_uwsgi.ini \
      --pidfile=/tmp/webservices.pid \
      --check-static /home/sass/webservices/weblicht/
```

Stop server:

```
uwsgi --stop /tmp/webservices.pid
```

## Reqiurements

* Conda https://www.anaconda.com/download/

## Installation

Create virtual environment:
```
conda create -n estnltk_webservices python=3.5
source activate estnltk_webservices
```

Install estnltk:
```
git clone https://github.com/estnltk/estnltk.git
cd estnltk
git checkout devel_1.6
python setup.py build
python setup.py install
```

Install webservices:
```
git clone https://github.com:estnltk/webservices.git
cd webservices
pip install -r requirements.txt
```
