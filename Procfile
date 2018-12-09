release: python manage.py migrate --no-input
web: gunicorn apiconfig.wsgi.application --log-file -
