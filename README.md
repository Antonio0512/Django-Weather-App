# Simple Django Weather Project with OpenWeatherMap API

This is a basic Django project that fetches weather data using the OpenWeatherMap API. It demonstrates how to integrate external APIs into a Django application to display weather information for a specified location.


## Prerequisites

- Python (3.x recommended)
- Django (3.x recommended)
- An OpenWeatherMap API Key (Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up))


## Setup

1. **Create and activate a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install project dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Obtain your OpenWeatherMap API Key and store it in a secure manner.**

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application in your web browser at http://127.0.0.1:8000/**


## Usage

1. Enter a city name or coordinates in the search bar on the homepage.

2. Click the "Get Weather" button.

3. The weather information for the specified location will be displayed.


## Happy Coding!
