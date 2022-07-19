# Next-Word-Predictor

Installing Virtual Environment :

`pip3 install virtualenv`

Creating a Python Virtual Environment:

`python -m venv venv`

Activating the newly created virtual env - venv:

`.\venv\Scripts\activate`

Install all the libraries from requirements file:

`pip install -r .\requirements`

Making all default migrations to the local:

`python manage.py migrate`

Run the server locally by manually hosting:

`python manage.py runserver`

Activating and running the project on local server

![image](https://user-images.githubusercontent.com/99491659/176275116-1d9ef240-1d6e-4abb-a6de-f0ad67affb24.png)

SignIn Page

![image](https://user-images.githubusercontent.com/99491659/176275230-ed31d349-3e24-4650-9978-1d2fe8a5c766.png)

SignUp Page

![image](https://user-images.githubusercontent.com/99491659/176275290-8d05529a-b4bc-416a-bfaf-3972223d402f.png)

The application runs on a Django framework and gives a rapid response through a Webscoket connection using BERT engine for prediction. The app takes in the user input text and provides a 3 suggested word predcitons that the user can use as follows.

![NWP_gif](https://user-images.githubusercontent.com/49874034/179851396-42c78e33-d1d9-4936-b975-92a527943de9.gif)

The application stores the user details on the Django's default database viewed from the admin's portal. It stores details like user's name, session id, date and timestamp, typed sentences and predicted words.

![DB](https://user-images.githubusercontent.com/49874034/179852209-14573fe8-a453-48b8-8078-7ab89cbbf9e5.JPG)

![DB 2](https://user-images.githubusercontent.com/49874034/179852245-cafd8185-d660-4c49-8860-7caea2ea1a34.JPG)

Further, in the upcoming developments, this data will be used for developing analytics for the application. Stay tuned!
