 # Property Management Application

## Overview
This is a Django-based API for a property management application. It allows property managers to add properties, manage tenants, and monitor rent payments.

## Features
- Property management (add, edit, delete properties)
- Tenant management
- Rental payment tracking
- JWT Authentication
- Filtering and sorting for properties
- Automated email notifications for due payments 
- Unit tests

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/Egaokira/property_management.git
   cd property_management
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Running Tests
To run the tests, use the following command:
```
python manage.py test
```

## API Documentation
API documentation is available via Swagger UI. After running the server, visit:
- http://localhost:8000/swagger/ for Swagger UI
- http://localhost:8000/redoc/ for ReDoc UI

## Project Structure
- `authentication/`: Custom user model and authentication views
- `properties/`: Property, Tenant, and RentalPayment models and views
- `property_management/`: Main project settings and configuration
