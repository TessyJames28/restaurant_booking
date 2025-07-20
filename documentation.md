# Restaurant Booking and Menu App Documentation

This document describes the Django-based web application's Little lemon restaurant available routes, APIs, and backend behaviors for handling table reservations and menu displays.

---

## Home Page

- **Function**: `home`
- **URL**: `/`
- **Method**: `GET`
- **Description**: Renders the homepage using `index.html`.

---

## ℹAbout Page

- **Function**: `about`
- **URL**: `/about/`
- **Method**: `GET`
- **Description**: Renders the about page using `about.html`.

---

## Book Table

- **Function**: `book`
- **URL**: `/book/`
- **Methods**: `GET`, `POST`
- **Description**:
  - Displays a booking form for customers to reserve a table.
  - On successful submission, displays a success message using Django's messages framework.
  - If validation fails, form errors are rendered.
- **Form**: Uses a Django form called `BookingForm`.

---

## Bookings Dashboard Page (Admin View)

- **Function**: `bookings_page`
- **URL**: `/bookings/`
- **Method**: `GET`
- **Description**: Renders the bookings dashboard page as an HTML view.
- **Use Case**: Likely for internal/admin viewing of reservations.

---

## Fetch All Bookings (API)

- **Function**: `bookings`
- **URL**: `/api/bookings/`
- **Method**: `GET`
- **Returns**: All bookings in JSON format, sorted by `booking_date` and `reservation_slot`.

### Success Response Example

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "date": "2025-07-20",
    "time": "12:00 PM"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "date": "2025-07-20",
    "time": "1:00 PM"
  }
]
