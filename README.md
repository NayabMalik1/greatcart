

#  GreatKart – E-Commerce Website

GreatKart is a fully functional **E-Commerce web application** built with **Django**. It supports user authentication, product management, cart/checkout flow, order management, and more.

This project is designed for learning as well as production-level e-commerce development.

---

##  Features

* 🔑 **User Authentication** (Register, Login, Logout, Password Reset, Email Activation)
* 🛍️ **Product Catalog** with Categories & Variations
* 🛒 **Shopping Cart** (Add, Remove, Update Items, Grouped Cart Items)
* 💳 **Checkout & Payment Flow**
* 📦 **Order Management**
* 🔎 **Search & Pagination** for products
* 📧 **Email Notifications** (Account activation, Order updates)
* 🛠️ **Admin Dashboard** for managing users, products, and orders

---

##  Project Structure

```
greatkart/
│── greatcart/            # Main Django project folder
│   ├── settings.py       # Project settings
│   ├── urls.py           # Project URLs
│   ├── wsgi.py           # WSGI configuration
│
│── accounts/             # User authentication (login, register, reset, activation)
│── carts/                # Cart and checkout system
│── orders/               # Orders and order management
│── store/                # Products, categories, variations
│── templates/            # HTML templates
│── static/               # Static files (CSS, JS, Images)
│── media/                # Uploaded images (products, profiles)
│
│── manage.py             # Django project manager
│── requirements.txt      # Project dependencies
│── README.md             # Documentation
```

---

##  Requirements

Make sure you have the following installed:

* Python **3.8+**
* Django **3.x / 4.x**
* pip (Python package manager)
* Virtualenv (recommended)
* Git

---

##  Dependencies

Your `requirements.txt` should include:

```
Django>=3.2,<4.0
Pillow
django-crispy-forms
django-allauth
mysqlclient (or psycopg2 if using PostgreSQL)
django-filter
```

*(Adjust according to your installed libraries in the project.)*

---

##  Installation & Setup

Follow these steps to set up the project locally:

### 1️ Clone the repository

```bash
git clone https://github.com/NayabMalik1/greatkart.git
cd greatkart
```

### 2️ Create a virtual environment

```bash
python -m venv env
```

Activate it:

* Windows:

  ```bash
  env\Scripts\activate
  ```
* Mac/Linux:

  ```bash
  source env/bin/activate
  ```

### 3️ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️ Setup environment variables

Create a `.env` file in the root directory with:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
DATABASE_NAME=greatkart
DATABASE_USER=root
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=127.0.0.1
DATABASE_PORT=3306
```

### 5️ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️ Create a superuser

```bash
python manage.py createsuperuser
```

### 7️ Collect static files

```bash
python manage.py collectstatic
```

### 8️ Run the development server

```bash
python manage.py runserver
```

Now visit:  **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

##  Git Workflow

If you’re working with multiple branches (features), use:

```bash
git checkout -b feature/branch-name    # Create new feature branch
git add .
git commit -m "Your commit message"
git push origin feature/branch-name
```

To merge updates into `main`:

```bash
git checkout main
git pull origin main
git merge feature/branch-name
git push origin main
```

---



---

##  Contribution

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/xyz`)
3. Commit changes (`git commit -m 'Add xyz feature'`)
4. Push to branch (`git push origin feature/xyz`)
5. Create a Pull Request

---

##  Contact

For queries or contributions, feel free to connect:

 **Developer:** Nayab Zahoor
 Email: \[[nayabzahoor08@gmail.com](mailto:nayabzahoor08@gmail.com)]