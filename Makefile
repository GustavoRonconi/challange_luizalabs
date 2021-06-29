install:
	sudo -u postgres psql -c "CREATE USER gustavoronconi WITH PASSWORD 'gustavo_luizalabs'"
	sudo -u postgres psql -c "CREATE DATABASE challenge_luizalabs"
	sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE "challenge_luizalabs" to gustavoronconi"
	sudo -u postgres psql -c "ALTER USER gustavoronconi CREATEDB"
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('gustavoronconi', 'gustavo.ronconi@simplecapp.com.br', 'gustavo_luizalabs')" | python manage.py shell