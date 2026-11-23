# 🥣 Sambar Handbook

A comprehensive web application celebrating the culinary heritage, regional varieties, authentic recipes, and nutritional profile of South India's most beloved dish — **Sambar**.

---

## 🌟 Features

- **📖 Rich History & Legends**: Explores both ancient literary references (1517 Telugu poem *Amuktamalyada*) and the popular 17th-century Maratha Thanjavur royal court legend.
- **🗺️ Regional Varieties**: Details signature sambar profiles across Tamil Nadu, Karnataka, Kerala, Andhra Pradesh, and Telangana.
- **🥗 Ingredients Encyclopedia**: Covers authentic lentils, spices, vegetables, tempering techniques, and garnishes.
- **🍲 Curated Recipes & State Filtering**: Step-by-step recipes with difficulty ratings, preparation/cooking times, instructions, and interactive state filtering with pagination.
- **📊 Nutritional Breakdown**: Provides calorie counts, protein, carbohydrates, and dietary fiber per serving for balanced healthy eating.
- **💡 Cooking Tips & Facts**: Master tips for tempering, dal consistency, tamarind timing, and fun cultural facts.
- **🖼️ Image Gallery & Search**: Categorized visual showcase and a global search bar for instant lookup.
- **🛒 Quick Shopping List & Functional Contact Form**: Everything you need to prepare classic homemade sambar.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.14, Django 6.0
- **Database**: SQLite (Development)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5, Bootstrap Icons
- **Typography**: Google Fonts (*Plus Jakarta Sans* & *Outfit*)
- **Static Assets & Server**: WhiteNoise, Gunicorn
- **Deployment Ready**: Render configuration (`render.yaml`, `build.sh`)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/charanepuri/sambar-handbook.git
cd sambar-handbook
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 📂 Project Structure

```text
sambar_handbook/
│
├── handbook/                     # Main Django application
│   ├── migrations/               # Database migrations
│   ├── static/handbook/          # CSS, images, and brand assets
│   ├── templates/handbook/       # Template HTML files
│   ├── admin.py                  # Admin configuration
│   ├── models.py                 # Data models (Recipe, Ingredient, Variety, etc.)
│   ├── urls.py                   # App URL patterns
│   └── views.py                  # View controllers
│
├── sambar_handbook/              # Project settings & configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/                        # User-uploaded images & PDF documentation
│   └── Sambar Handbook.pdf
│
├── staticfiles/                  # Collected static assets (WhiteNoise)
├── build.sh                      # Build script for production deployment
├── render.yaml                   # Render deployment configuration
├── requirements.txt              # Project dependencies
└── manage.py                     # Django management CLI
```

---

## 👨💻 Author

**Charan Teja Epuri**

Aspiring Full Stack Developer

- Portfolio(Django): [Link](https://portfolio-site-django.onrender.com)
- GitHub: [Profile](https://github.com/charanepuri)
- Portfolio(React): [Link](https://charan-react-portfolio.vercel.app)
- LinkedIn: [Profile](https://www.linkedin.com/in/charan-teja-972aa9231)
- Portfolio(Flask): [Link](https://flask-developer-dashboard-portfolio.onrender.com)

---

## 📄 License

This project is licensed under the MIT License - feel free to use and adapt it!
