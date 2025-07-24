
#  GreatCart - Django E-commerce Project

This is a fully functional e-commerce web application built with Django.  
The project includes product listing, dynamic category filtering, product detail views, slugs, admin control, and SQLite database integration.

---

##  Project Structure

```

greatcart/
│
├── greatcart/              # Main Django settings and URLs
├── store/                  # Core app (views, models, templates)
├── media/                  # Uploaded product images
├── templates/              # HTML templates
├── static/                 # CSS, JS, and Bootstrap
├── db.sqlite3              # SQLite database
└── manage.py

````

---

##  Features

- ✅ Product listing with category filters
- ✅ Dynamic/static slugs for product and category URLs
- ✅ Product detail page with routing
- ✅ Django Admin integration for adding products/categories
- ✅ Static and media file configuration
- ✅ Responsive Bootstrap UI
- ✅ Error handling (404 pages)
- ✅ Organized views using function-based logic

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/NayabMalik1/greatcart.git
cd greatcart
````

### 2. Setup Virtual Environment (venv)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install django
```

> If you use `requirements.txt`, you can add:
>
> ```bash
> pip freeze > requirements.txt
> ```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Open in browser:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🗂️ Slug-based URL Examples

* **Category View:** `/store/shirts/`
* **Product Detail:** `/store/shirts/white-shirt/`

---



