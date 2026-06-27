# Personal-Blog-Website
<h1>📝 Personal Blog Website</h1>
<p>A modern and responsive Personal Blog Website built with Flask, SQLAlchemy, and Bootstrap. The application allows users to register, log in securely, create and manage blog posts, and enjoy a clean user interface with randomly changing home page images for a fresh experience on every visit.</p>
<h2>🚀 Features</h2>
<h4>🔐 User Authentication</h4>
<ul>
  <li>User Registration</li>
  <li>Secure Login</li>
  <li>Logout</li>
</ul>
<h4>📝 Blog Management</h4>
<ul>
  <li>Create new blog posts</li>
  <li>Delete blog posts</li>
  <li>View all blog posts on the home page</li>
</ul>
<h4>🎨 Responsive UI</h4>
<ul>
  <li>Built with Bootstrap</li>
  <li>Mobile-friendly design</li>
</ul>
<h4>💾 Database Support</h4>
<ul>
  <li>SQLAlchemy ORM</li>
  <li>SQLite database (default)</li>
</ul>
<h2>🛠️ Tech Stack</h2>
<h4>Backend</h4>
<ul>
  <li>Flask</li>
  <li>Flask-SQLAlchemy</li>
  <li>Werkzeug (Password Hashing)</li>
</ul>
<h4>Frontend</h4>
<ul>
  <li>HTML5</li>
  <li>CSS 3</li>
  <li>Bootstrap 5</li>
  <li>Jinja2 Templates</li>
</ul>
<h4>Database</h4>
<ul>
  <li>SQLite</li>
</ul>
<h2>📂 Project Structure</h2>
<p>
  personal-blog/<br>
  │ <br>
  ├── static/<br>
  │<br>
  ├── css/<br>
  │<br>
  ├── images/<br> 
  │ └── js/<br>
  │ <br>
  ├── templates/<br>
  │ <br>
  ├── base.html<br>
  │ <br>
  ├── home.html <br>
  │ <br>
  ├── login.html<br>
  │<br>
  ├── register.html<br>
  │<br>
  ├── createblog.html<br>
  │ └── ...<br>
  │ ├── app.py<br>
  ├── models.py<br>
  ├── requirements.txt <br>
  ├── instance/<br>
  │ └── blog.db<br>
  │ └── README.md<br>
</p>
<h2>⚙️ Installation</h2>
<ol>
  <li>Clone the Repository</li>
  git clone https://github.com/bakshikul/Personal-Blog-Website.git<br>
  cd Personal-Blog-Website<br>
  <li>Create a Virtual Environment</li>
  <p>python -m venv venv<br>
  venv\Scripts\activate<br>
  Linux / macOS<br>
  python3 -m venv venv<br>
  source venv/bin/activate</p><br>
  <li>Install Dependencies</li>
  <p>pip install -r requirements.txt</p><br>
  <li>Run the Application</li>
  <p>python app.py</p><br>
  <p>The application will be available at:<br>
  http://127.0.0.1:5000/</p><br>
</ol>
<h2>🤝 Contributing</h2>
<p>Contributions are welcome!</p>
<ol>
  <li>Fork the repository</li>
  <li>Create a feature branch</li>
  <p>git checkout -b feature-name</p>
  <li>Commit Your Changes</li>
  <p>git commit -m "Add new feature"</p>
  <li>Push to your branch</li>
  <p>git push origin feature-name</p>
  <li>Open a Pull Request</li>
</ol>
<h2>📜 License</h2>
<p>This project is licensed under the MIT License.</p>
<h2>👨‍💻 Author</h2>
<h5>Kul Bakshi</h5>
<p>If you found this project helpful, consider giving it a ⭐ on GitHub!</p>
