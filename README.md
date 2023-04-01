# BookList API

## BookList API project made with Django Rest Framework

### To run the project:

1. Clone the repository
2. Create a virtual environment and install the requirements
    - if you use pipenv: `pipenv shell` then `pipenv install`
    - if you use pip: `pip install -r requirements.txt`
4. Make the migrations: `python manage.py makemigrations`
3. Run the migrations: `python manage.py migrate`
5. Run the server: `python manage.py runserver`
6. Go to any of the 2 API endpoints (use a browser or any tool like Insomnia or Postman):
    - Get all books: `http://localhost:8000/api/books/`
    - Get a single book: `http://localhost:8000/api/books/<id>/`

## Credits

This project was made following the course from [APIs](https://www.coursera.org/learn/apis) on [Coursera](https://www.coursera.org/) by [Meta](https://www.coursera.org/meta)
