# Online Store API using DRF

- This is an online store API built with Django Rest Framework to manage product categories and orders.

## Features
- CRUD operations for Categories and Products
- Order creation with validation on stock availability

## Project Setup

1. Clone the repository:
    ```bash
    git clone <repo_url>
    cd online_store
    ```
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

7. Running Tests- To run the tests, use PyTest:
    ```bash
    pytest
    ```

## API Endpoints
- GET /v1/api/categories/ - List all categories
- POST /v1/api/categories/ - Create a new category
- GET /v1/api/products/ - List all products
- POST /v1/api/products/ - Create a new product
- POST /v1/api/orders/ - Create a new order (with stock validation)
