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

### 🗃️ Step 4: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 🚦 Step 5: Run the Development Server
```bash
python manage.py runserver
```

### 🧪 How to Test the App

#### 📅 Index Page

- Visit / (e.g. http://localhost:8000/)

#### 📅 View Menu

- Visit /menu/ (e.g. http://localhost:8000/menu/)

#### 📅 About Page

- Visit /about/ (e.g. http://localhost:8000/about/)

#### 📅 Book a Table

- Visit /book/ (e.g. http://localhost:8000/book/)
- Select a date.
- Select an available slot (already booked or past slots will be hidden).
- Enter your name.
- Click Book Now.
- A success message will be displayed after a successful booking.

#### 📊 View All Bookings (Admin Dashboard)
- Visit /bookings/ (e.g. http://localhost:8000/bookings/)
```
The page will show a list of all current bookings with: 
    Guest name
    Date
    Time (human-readable)
```
