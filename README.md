#  Search Feature

This branch adds a basic search functionality to the store page.

##  What’s Implemented

- A search bar is added to the navbar or sidebar.
- Users can search products by name or description.
- Results appear on the same product listing page.

##  Usage

### 1. Search URL:
Visit: `http://127.0.0.1:8000/store/search/?keyword=shoes`

### 2. Features:
- Searches through `product_name` and `description` fields.
- Case-insensitive and partial matches supported.
- Rendered in the same `store.html` template.

##  Files Modified

- `store/views.py` (added `search()` view)
- `store/store.html` (added form and logic)
- `urls.py` (added search path)

##  Example

URL: `/store/search/?keyword=hoodie`  
Returns: All products with “hoodie” in the name or description.

---
