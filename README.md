# Cart & Checkout Auth Sync

## Overview
This branch implements a complete set of improvements for the cart and checkout system, focusing on seamless user experience for both guest and authenticated users.

## Features
1. **Checkout Page Design**
   - Responsive, centered layout.
   - Product list with variations (color, size), quantity, and price.
   - Billing address form with validation.
   - Order notes support.

2. **Assign User to Cart Items on Login**
   - On login, any existing guest cart items are merged and assigned to the authenticated user.
   - Prevents cart reset after login.

3. **Update Cart Counter for Logged-in Users**
   - Real-time cart counter updates after login or cart actions.
   - Shared logic for both guest and authenticated users.

4. **Variation Grouping for Logged-in Users**
   - Ensures cart items are grouped correctly by product, color, and size for logged-in users.
   - Prevents duplicate rows in the cart.

## How It Works
- Guest users create a session cart (`cart_id`).
- On login, guest cart items are merged with the authenticated user's cart items.
- All cart-related queries for authenticated users use `user=request.user` to ensure data consistency.
- Checkout page fetches cart items based on authentication state and displays all relevant details.


