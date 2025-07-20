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

## 🗄️ Database Setup: MySQL for Django

To run this project with MySQL as the database backend, follow these steps to install MySQL, create the necessary database, and configure Django to connect to it.

---

### ✅ 1. Install MySQL

#### On Windows:

- Download MySQL Installer from [https://dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/)
- Choose the **Developer Default** or **Custom** setup and install MySQL Server
- During installation, set the **root password** and **create a user** (e.g., `web_dev`)

#### On macOS (using Homebrew):

```bash
brew install mysql
brew services start mysql
```

#### On Ubuntu/Linux:
```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
```

### ✅ 2. Create Database and User
```sql
mysql -u root -p
```

-- Then run the following SQL:
```sql
CREATE DATABASE reservations CHARACTER SET UTF8MB4;
CREATE USER 'web_dev'@'localhost' IDENTIFIED BY 'web_dev@123';
GRANT ALL PRIVILEGES ON reservations.* TO 'web_dev'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

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
