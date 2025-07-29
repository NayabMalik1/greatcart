# Grouping Cart Item Feature

This feature branch introduces functionality to handle grouping of cart items based on product **variation attributes** such as **color** and **size**.

---

##  Purpose

Previously, adding the same product with different variations (e.g., same shirt in Red/Large and Red/Medium) either:
- Overwrote the existing item in the cart, or
- Didn't clearly differentiate items with different variations.

This feature aims to:
- ✅ Group identical product+variation combinations.
- ✅ Allow multiple cart entries for the same product with **different color/size**.
- ✅ Show "Already added" only when the **exact variation** exists.
- ✅ Display already selected variations on the product page for clarity.

---

##  Changes in This Branch

- **Models Updated**: Ensured `CartItem` supports `color` and `size` as grouping keys.
- **Views Refactored**:
  - `add_cart()` groups only exact matches.
  - `remove_cart()` uses `color` and `size` to reduce the right item.
s.

---

##  How to Test

1. Visit the product page.
2. Select a color and size.
3. Add to cart.
4. Add the same product with **different variations**.
5. Observe:
   - Quantity increases for same variation.
   - New cart item appears for different variation.
6. View all variations listed clearly in the cart.

---

##  Folder/File Impact

| File                        | Description                        |
|-----------------------------|------------------------------------|
| `views.py`                 | Handles logic for cart item grouping |
| `product_detail.html`      | Dropdown + form structure improved  |
| `cart.html`                | Shows color and size per item       |

---

##  Author

Nayab Zahoor  
Student of Software Engineering  
Fatima Jinnah Women University  

---

