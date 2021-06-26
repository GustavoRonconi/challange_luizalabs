install:
	sudo -u postgres psql -c "CREATE USER gustavoronconi WITH PASSWORD 'gustavo_luizalabs'"
	sudo -u postgres psql -c "CREATE DATABASE challange_luizalabs"
	sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE "challange_luizalabs" to gustavoronconi"
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('gustavoronconi', 'gustavo.ronconi@simplecapp.com.br', 'gustavo_luizalabs')" | python manage.py shell