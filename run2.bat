clear
cd microfe
## initiate the database
python manage.py migrate
## check it works
python manage.py runserver 8000  --settings=microfe_main
