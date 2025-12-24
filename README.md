# Student Management System (Django)

A simple **Django-based web application** for managing student records. This project is built as part of a Django workshop and demonstrates full **CRUD (Create, Read, Update, Delete)** functionality using Django’s **MVT (Model–View–Template)** architecture.

---

## 📌 Project Overview

The **Student Management System** allows users to:

* Add new student records
* View a list of students
* Update existing student details
* Delete student records with confirmation

The application uses Django ORM with SQLite3 and clean, responsive templates built using **HTML, CSS, and Bootstrap**.

---

## 🛠️ Technologies Used

* **Python 3**
* **Django 5.x**
* **SQLite3** (default Django database)
* **HTML5**
* **CSS3**
* **Bootstrap 5**

---

## 📂 Features Implemented

### 1. Student Model

The Student model includes the following fields:

* Student ID (Auto-generated)
* Full Name
* Email Address
* Age
* Address

### 2. CRUD Operations

* **Create:** Add new students using a Django form
* **Read:** Display all student records in a table
* **Update:** Edit existing student details
* **Delete:** Delete a student with a confirmation page

### 3. Templates

Separate templates are used for:

* Student listing page
* Add/Edit student form
* Delete confirmation page

### 4. URL Routing

Dedicated URL patterns for:

* Listing students
* Adding a student
* Editing a student
* Deleting a student

### 5. Database

* Uses **SQLite3**, configured by default in Django

---

## 📁 Project Structure

```
Student-Management-System/
│
├── student/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── templates/
│   ├── base.html
│   ├── student_list.html
│   ├── student_form.html
│   └── student_confirm_delete.html
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🚀 How to Run the Project

1. **Clone the repository**

```bash
git clone https://github.com/utsavgayawali/Student-Management-System.git
```

2. **Navigate to the project directory**

```bash
cd Student-Management-System
```

3. **Create and activate a virtual environment (optional but recommended)**

```bash
python -m venv env
env\Scripts\activate
```

4. **Install Django**

```bash
pip install django
```

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Start the development server**

```bash
python manage.py runserver
```

7. **Open in browser**

```
http://127.0.0.1:8000/
```

---

## ✅ Project Requirements Fulfilled

✔ Django MVT architecture
✔ Student model with required fields
✔ Full CRUD functionality
✔ Separate templates for each operation
✔ Proper URL routing
✔ SQLite3 database

---

## 👤 Author

**Utsav Gayawali**
GitHub: [https://github.com/utsavgayawali](https://github.com/utsavgayawali)

---

## 📜 License

This project is for educational purposes and learning Django fundamentals.
