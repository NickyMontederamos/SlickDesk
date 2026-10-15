# 🛠️ SlickDesk — IT Helpdesk & Asset Management System

![Python](https://img.shields.io/badge/Python-Flask-blue?style=flat-square&logo=python)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat-square&logo=sqlite)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange?style=flat-square)
![Automation](https://img.shields.io/badge/Automation-PowerShell-blue?style=flat-square&logo=powershell)

> A full-stack IT Helpdesk and Asset Management web application built as a portfolio project by **Nicole Dominique Montederamos** | [slicklab.digital](http://slicklab.digital)

---

## 🎯 Project Overview

SlickDesk is a lightweight internal IT helpdesk system that allows users to submit support tickets, track IT assets, and view a live dashboard — with email automation and PowerShell reporting built in.

---

## ✨ Features

- 📋 **Ticket Submission** — Users submit IT issues with category and priority
- 📊 **Dashboard** — Live stats on open, resolved tickets and total assets
- 🖥️ **Asset Management** — Track hardware/software assigned to staff
- 📧 **Email Automation** — Auto-reply confirmation emails via Python SMTP
- 📄 **PowerShell Reports** — Daily ticket summary report generation
- 🗄️ **SQLite Database** — Lightweight SQL database for all data

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python (Flask) |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite (SQL) |
| Automation | PowerShell, Python |
| Email API | Gmail SMTP / SendGrid |

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/NickyMontederamos/SlickDesk.git
cd SlickDesk

# 2. Install dependencies
pip install flask

# 3. Run the app
python app.py

# 4. Open in browser
http://localhost:5000
```

---

## 📁 Project Structure

```
SlickDesk/
├── app.py                  # Main Flask application
├── database/
│   └── db.py               # Database setup and connection
├── templates/
│   ├── base.html           # Base layout
│   ├── index.html          # Ticket list
│   ├── submit.html         # Submit ticket form
│   ├── ticket.html         # View single ticket
│   ├── dashboard.html      # Stats dashboard
│   └── assets.html         # Asset list
├── static/
│   ├── css/style.css       # Stylesheet
│   └── js/main.js          # Frontend JS
├── scripts/
│   ├── email_notify.py     # Email automation
│   └── generate_report.ps1 # PowerShell report generator
└── README.md
```

---

## 👩‍💻 Author

**Nicole Dominique Montederamos**
- GitHub: [@NickyMontederamos](https://github.com/NickyMontederamos)
- LinkedIn: [ndmontederamos](https://linkedin.com/in/ndmontederamos)
- Website: [slicklab.digital](http://slicklab.digital)

---

*Built as a portfolio project — May 2026.*
