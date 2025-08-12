# Login Feature - GreatKart

## Overview
This feature implements user authentication functionality, allowing users to securely log in and log out of the GreatKart platform. It includes:

- User login with email and password
- Password authentication using Django's built-in methods
- Login success and failure messages with UI alerts
- User logout with success message and session termination
- Redirects to appropriate pages after login/logout
- Message alerts that automatically fade after a few seconds for better UX

## Details

### Login Process
- The login form takes an email and password.
- On form submission, the backend authenticates the user credentials.
- Successful login redirects users to the home page with a success message.
- Failed login attempts show an error message.

## Files Modified
- `accounts/views.py` - login and logout view functions
- `accounts/templates/accounts/login.html` - login page with form and alert includes
- `includes/alerts.html` - alert block for showing messages
- `base.html` - included JavaScript for alert fadeout



