web: python scripts/init_db.py && gunicorn -w 2 -k gthread --threads 4 --timeout 120 --bind 0.0.0.0:$PORT wsgi:app
