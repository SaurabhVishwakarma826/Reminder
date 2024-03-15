# Remind-me-later

Remind-me-later is a simple web application that allows users to set up reminders with messages. It provides a user-friendly interface to input the date, time, and message for the reminder. The application supports reminders via SMS and Email, with the potential to add support for other notification methods in the future.

## Features

- User registration: Users can sign up for an account by providing their name, email, username, and password.
- User authentication: Registered users can log in using their username and password, and token authentication is used to authenticate users for creating reminders.
- Reminder creation: Users can create reminders by specifying the date, time, and message for the reminder.
- Email reminder: Reminders are sent to users via email at the specified date and time.
- Future enhancements: The application can be extended to support additional notification methods such as SMS.

## How to Use

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SaurabhVishwakarma826/Reminder.git
    cd Reminder
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the application in your web browser at http://localhost:8000.

### Usage

1. Register an account: Navigate to the registration page and sign up for a new account.

2. Log in: Once registered, log in using your username and password.

3. Create a reminder: After logging in, you can create reminders by providing the date, time, and message for the reminder.

4. View reminders: You can view your created reminders in the application.

5. Receive reminders: Reminders will be sent to your email at the specified date and time.

## Technologies Used

- Django: Python-based web framework used for backend development.
- Django Rest Framework: Toolkit for building Web APIs in Django.
- Celery: Distributed task queue used for asynchronous processing (optional).
- Redis or RabbitMQ: Message broker used with Celery (optional).
- SMTP: Simple Mail Transfer Protocol used for sending reminder emails.

## Contributors

- Your Name (@SaurabhVishwakarma826)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
