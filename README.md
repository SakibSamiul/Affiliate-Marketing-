
# Baby Affiliate - Amazon Baby Products

This project is a Django-based affiliate marketing website for promoting Amazon baby products. It dynamically displays product details, uses reusable templates, and adheres to a modular code structure.
## Features

- Display a list of baby products with images, names, prices, and details.
- Detailed view of individual products, including a description and affiliate link.
- Admin panel for managing product data.
- Efficient use of Django Template Language (DTL) for dynamic content rendering.
- Modular and reusable code with proper use of templates, views, and models.

## Prerequisites

Before running the project, ensure the following are installed on your system:

- **Python 3.8+**
- **Django 5.1.3**
- **pip** (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/baby-affiliate.git
   cd baby-affiliate
   ```

2. Create a Virtual Environment
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a Superuser
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
baby_affiliate/
├── baby_affiliate/       # Django project settings
├── products/             # App for managing baby products
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates
│   ├── models.py         # Product model
│   ├── views.py          # Views for product list and details
│   ├── urls.py           # URLs for the app
├── static/               # Static files (CSS, images, etc.)
├── manage.py             # Django management script
└── README.md             # Project documentation
```

## Contact

For queries or issues, please contact:
- **Email:** sb.sakib77@gmail.com
- **GitHub:** [my-profile](https://github.com/SakibSamiul)
