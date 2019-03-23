# Sample project using MongoDB

---

## Overview
MongoDB is a cross-platform document-oriented database program. The main feature is it being a NoSQL database that uses JSON-like documents for storing data.
This project represents basic web-application with social-network features such as feed, subscribers and upvotes.

## How to run on your local machine
- Make sure you have all [dependencies](./dependencies.md) installed.
- Run your mongodb instance (e.g.: `# mongod --dbpath /var/lib/mongodb/ --journal`)
- `$ cd socialpic`
- `$ python manage.py makemigrations`
- `$ python manage.py migrate`
- `$ python manage.py runserver`
- Open URL `127.0.0.1:8000`
