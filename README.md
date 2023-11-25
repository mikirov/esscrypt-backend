# Installation:
```
git clone https://github.com/mikirov/esscrypt.git
cd esscrypt
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
# Running server locally:
```
python manage.py runserver
```

# Make migrations:
```
python manage.py makemigrations app
python manage.py migrate
```
# Freeze requirements:
```
pip freeze > requirements.txt
```

# Deactivate virtual environment:
```
deactivate
```