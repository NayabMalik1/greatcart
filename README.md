# GreatKart - Order Management Feature

## Overview
This update introduces a complete **Order Management** system to the GreatKart e-commerce platform.  
It enables users to place orders, generate unique order numbers, manage ordered products, and handle payments.

---

## Features
- **Order Model** – Stores customer details, shipping info, order totals, and status.
- **OrderProduct Model** – Tracks each product in an order with quantity and pricing.
- **Payment Model** – Stores transaction and payment method details.
- **Dynamic Redirects** – Smart navigation to checkout or store depending on cart status.
- **Order Number Generator** – Creates a unique order number (`YYYYMMDD + order_id`).
- **Form Handling** – Captures shipping/billing details from `OrderForm`.
- **Tax Calculation** – Calculates 2% tax automatically.

---

