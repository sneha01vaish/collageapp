# **College Editor Collage Creator**

A Django-based web application that allows users to:
- Upload multiple images.
- Select images from uploaded ones.
- Choose a collage layout (2, 3, or 4 pics).
- Generate a visual collage using HTML/CSS and JavaScript.
- Download the collage as an image.

---

## ** Project Title**
**collageapp** – A user-friendly tool to generate downloadable photo collages.

---

## ** Getting Started**

### **1. Clone the Repository**
```bash
git clone https://github.com/sneha01vaish/collageapp.git
cd collageapp
```

---

### **2. Create a Virtual Environment and Install Dependencies**
```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# or
source venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt
```

---

### **3. Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **4. Run the Project**
```bash
python manage.py runserver
```

Then open your browser and visit:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## **🛠 Features**
- Clean and responsive UI with image previews
- Select desired layout (2, 3, or 4 images)
- Collage layout generated using CSS Grid
- Downloadable collage image using html2canvas

---

## **👩‍💻 Developer**
**Sneha Vaish**

---

## **📝 Note**
This project is for demonstration and learning purposes. Feel free to enhance it by adding layout previews, drag-and-drop, or permanent saving of generated collages.
