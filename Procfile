release: python RoyalSite/manage.py migrate
web: gunicorn 'RoyalSite/RoyalSite/RoyalSite.wsgi' --log-file=-