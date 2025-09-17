# Restaurant Booking System

A simple Django-based web application for Litle lemon table reservation. Users can book available time slots, and administrators can view all bookings.

---

## 🚀 Features

- Users can reserve tables by selecting a date and available time slots.
- Time slots that are already booked are automatically hidden.
- Past time slots on the current date are disabled.
- Prevents duplicate bookings.
- Confirmation message shown after successful booking.
- Booking dashboard to display all current bookings.

---

## 🛠️ Installation & Setup Guide

Follow the steps below to get the application running on your local machine.

---

### 🔧 Requirements

- Python 3.11+
- pip
- virtualenv *(recommended)*

---

### 📁 Step 1: Clone the Repository

```bash
git clone https://github.com/TessyJames28/restaurant_booking.git
cd restaurant-booking
```

### 🧪 Step 2: Create and activate a virtual environment

```bash
python -m venv .venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 📦 Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

### 🗃️ Step 4: Apply Migrations and Seed Menu Table
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py shell < seed_menu.py
```

### 🚦 Step 5: Run the Development Server
```bash
python manage.py runserver
```

### 🧪 How to Test the App
Automated tests are included in the project under bookings/tests.py
```bash
python manage.py test
```

### ✅ Test Cases (with expected actions and results)
#### 📅 Index Page

- Action: Visit ```/``` (e.g. http://localhost:8000/)
- Expected Result: Homepage (index.html) loads successfully with status ```200```

#### 📅 View Menu

- Action: Visit ```/menu/``` (e.g. http://localhost:8000/menu/)
- Expected Result: age loads with a list of menu items from the database.

#### 📅 View Single Menu

- Action: Visit ```/menu_item/<id>/```
- Expected Result: Menu item detail page loads for the selected item, displaying image, menu, menu description, and price

#### 📅 About Page

- Action: Visit ```/about/``` (e.g. http://localhost:8000/about/)
- Expected Result: About page loads with status 200 and displays the project info.

#### 📅 Book a Table

- Action 1: Visit ```/book/``` (e.g. http://localhost:8000/book/)
- Expected Result 1: The booking form is displayed

- Action 2: Submit a valid booking form with correct data. This includes:
- ```Select a date```
- ```Selecting available slot``` (already booked or past slots will be hidden).
- ```Enter your name.```
- ```Click Book Now.```
- Expected Result: A success message will be displayed after a successful booking saying ```Your table has been booked successfully for [slot] on [date].```

- Action 3: Submit booking form with missing or invalid data
- Expected Result 3: Error messages are displayed for each invalid field.

#### 📊 View All Bookings (Admin Dashboard)
- Action 1: Visit ```/bookings/``` (e.g. http://localhost:8000/bookings/)
- Expected Result 1: The bookings.html page is displayed and fetches booking data from the backend which is displayed in a table.
```
The page will show a list of all current bookings with: 
    Guest name
    Date
    Time (human-readable)
```

- Action 2: Filter booking data by date using the calendar picker
- Expected Result 2: Displayed all bookings for the filtered date


#### 📊 Bookings API 
- Action: Call endpoint ```/booking_data/``` (http://127.0.0.1:8000/booking_data/)
- Expected Result: Returns a JSON list of dictionary containing bookings, each containing id, name, date, and time

```json
[
  {"id": 1, "name": "Amara", "date": "2025-09-18", "time": "12:00 PM"},
  {"id": 2, "name": "Jane Doe", "date": "2025-09-19", "time": "10:00 AM"}
]
```


#### 📊 Available Slots API
- Action: Call endpoint with valid date ```/available_slots/?date=YYYY-MM-DD```
- Expected Result: Returns JSON with list of available slots for the given date.

- Action 2: Call endpoint without a date
- Expected Result: Returns error JSON ```{"error": "No date provided"}```

- Action 3: Call Endpoint with an Invalid Date Format
- Expected Result 3: Returns error JSON ```{"error": "Invalid date format"}.```

#### 📊 Booked Slots API
- Action: Call endpoint with a valid date ```/booked_slots/?date=YYYY-MM-DD```
- Expected Result: Returns JSON with a list of slot numbers that are already booked for that date.
