# 🧭 Pagination Feature

This branch adds pagination to the product listing in the `store` view of our Django project.

## 🔧 What’s Implemented

- Django’s `Paginator` class is used to paginate products.
- Pagination logic is included in the `store()` view.
- HTML pagination controls are added in `store.html`.

## 🖥️ Usage

### 1. View URL:
Visit: `http://127.0.0.1:8000/store/`

### 2. Features:
- Displays limited products per page (configured in `Paginator(products, 3)`).
- Users can navigate using Next/Previous links.

## ✅ Files Modified

- `store/views.py`  
- `store/store.html`  
- `urls.py` (indirectly supports pagination via GET param `?page=`)

## 🔗 Example URLs

- Page 1: `/store/?page=1`
- Page 2: `/store/?page=2`

---
