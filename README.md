
# Forget & Reset Password Feature

This feature allows users to reset their account password via email securely.

## **Features**

* Forgot Password page where users enter their registered email.
* Sends a secure password reset link to the user's email.
* Link contains a token for authentication.
* Reset Password page to enter and confirm a new password.
* Uses Django's built-in `default_token_generator` for security.

## **Flow**

1. **User clicks "Forgot Password"** on the login page.
2. Enters their registered email address.
3. Email is sent containing a password reset link:

   ```
   https://yourdomain.com/reset/<uidb64>/<token>/
   ```
4. User clicks the link, which opens the **Reset Password** form.
5. User enters and confirms a new password.
6. Password is updated and user can log in with the new credentials.

## **Tech Used**

* **Django**
* `django.contrib.auth.tokens.default_token_generator`
* Django's `urlsafe_base64_encode` and `urlsafe_base64_decode`
* SMTP Email backend for sending reset emails

