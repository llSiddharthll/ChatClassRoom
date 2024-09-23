# 🌟 **ChatClassRoom** 🌟  
_A platform to share and explore notes, questions, and chat with friends!_

![Django](https://img.shields.io/badge/Django-v4.2.1-green) ![TailwindCSS](https://img.shields.io/badge/TailwindCSS-v3.3.2-blue) ![MIT License](https://img.shields.io/badge/License-MIT-yellow)

🚀 **Live Demo**: [ChatClassRoom](https://yourwebsite.pythonanywhere.com)

## 📝 **Project Overview**
Welcome to **ChatClassRoom**! This platform is built using **Django** and powered by some awesome technologies like **Django Allauth**, **Cloudinary**, **SQLite3**, and **Tailwind CSS** to give you a seamless, responsive, and visually appealing experience.  

### Features at a Glance ✨
- 📘 **Notes & Questions**: Organize your studies with subjects, topics, notes, and questions, all in one place.
- 🔍 **Real-time Search**: Find exactly what you need with our live search functionality.
- 🗂️ **User Dashboard**: Manage your notes and questions easily from your personal dashboard.
- 🗨️ **Chat Interface (In Development)**: Chat with peers, share knowledge, and collaborate (coming soon!).
- 🌈 **Responsive UI**: Beautifully designed with **Tailwind CSS**, ensuring a smooth experience across devices.

## 🛠️ **Tech Stack**
This project is built with the following awesome tools:

- **Backend**: [Django](https://www.djangoproject.com/) + [Django Allauth](https://django-allauth.readthedocs.io/) for user authentication.
- **Frontend**: [Tailwind CSS](https://tailwindcss.com/) + [Marked.js](https://marked.js.org/) and [Highlight.js](https://highlightjs.org/) for handling Markdown and syntax highlighting.
- **Storage**: [Cloudinary](https://cloudinary.com/) for media storage and hosting.
- **Database**: [SQLite3](https://www.sqlite.org/index.html) – Lightweight and perfect for development.
- **Hosting**: [PythonAnywhere](https://www.pythonanywhere.com/).

## ✨ **Key Pages**
- **Subjects & Topics**: Organize content by subjects and topics for easy navigation.
- **Notes & Questions**: Easily upload, view, and manage study materials.
- **Live Search**: Find what you’re looking for in real time!
- **User Dashboard**: Manage your content effortlessly.
- **Chat Interface**: (Coming soon) Collaborate and share notes with others.

## 🖥️ **Setup & Installation**

To run this project locally:

1. Clone the repo:
   ```bash
   git clone https://github.com/llSiddharthll/ChatClassRoom.git
   cd ChatClassRoom
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser to access the admin dashboard:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.

## 📂 **File Structure**
```
ChatClassRoom/
├── ChatClassRoom/         # Project settings
├── notes/                 # App handling notes and questions
├── static/                # Static assets like Tailwind CSS
├── templates/             # HTML templates
├── media/                 # Uploaded media (handled by Cloudinary)
├── .env                   # Environment variables
└── README.md              # This beautiful file!
```

## 🎨 **UI Preview**

Here's a sneak peek of our beautifully designed UI!

| 🖥️ Desktop View | 📱 Mobile View |
|-----------------|----------------|
| ![Desktop](https://your-desktop-screenshot-link.png) | ![Mobile](https://your-mobile-screenshot-link.png) |

## 🔧 **Future Enhancements**
- 🗣️ **Real-time Chat**: Let users communicate and collaborate instantly!
- 📊 **Analytics Dashboard**: Track note views and user interactions.
- 💬 **Comments**: Allow users to comment on notes and questions.
- 🌍 **Multi-language Support**: Expand reach by adding support for multiple languages.

## 📧 **Contact**
Have any questions or suggestions? Feel free to reach out to me at:  
**📧 llsiddharthtiwarill@gmail.com**

## 📝 **License**
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

Thank you for checking out **ChatClassRoom**!  
💡 *"Empowering students to learn, collaborate, and succeed!"* 💡
