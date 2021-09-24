release: python RoyalSite/manage.py migrate
web: gunicorn RoyalSite.wsgi.application --log-file=-