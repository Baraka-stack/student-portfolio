import streamlit as st
from PIL import Image
import time


# Set page configuration
st.set_page_config(page_title="Student Portfolio", page_icon="🎓", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #2b2d42;
            color: #f0f0f0;
            font-family: 'Arial', sans-serif;
        }
        .sidebar .sidebar-content {
            background: linear-gradient(to bottom, #9c27b0, #3f51b5);
            color: white;
        }
        .stButton>button {
            background-color: #4caf50;
            color: white;
            font-size: 18px;
            border-radius: 12px;
            padding: 12px;
            transition: 0.4s;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover {
            background-color: #8bc34a;
            box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.2);
        }
        .st-expander {
            background-color: #444;
            border-radius: 12px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.15);
        }
        .stProgress>div>div {
            background-color: #8bc34a !important;
        }
        h1, h2, h3 {
            font-family: 'Helvetica', sans-serif;
            font-weight: bold;
        }
        .stMarkdown {
            font-family: 'Arial', sans-serif;
            color: #e0e0e0;
        }
        .card-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); /* Responsive grid layout */
            gap: 20px; /* Space between cards */
            justify-items: center; /* Centers cards horizontally */
        }
        .card {
            background-color: #3e4a61;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
            height: 300px; /* Fixed height for all cards */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            width: 100%;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 16px rgba(0, 0, 0, 0.3);
        }
        .card img {
            border-radius: 8px;
            max-width: 100%;
            height: auto;
            object-fit: cover;
            height: 140px;
        }
        .card-title {
            font-size: 20px;
            font-weight: bold;
            margin-top: 10px;
            color: #ffffff;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
        }
        .card-desc {
            color: #b0b0b0;
            margin-top: 10px;
            font-size: 14px;
            overflow: hidden;
            text-overflow: ellipsis;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
        }
        .card a button {
            background-color: #4caf50;
            color: white;
            font-size: 16px;
            border-radius: 12px;
            padding: 10px;
            transition: 0.3s;
            border: none;
            width: 80%;
            margin-top: 10px;
            cursor: pointer;
        }
        .card a button:hover {
            background-color: #8bc34a;
            transform: scale(1.05);
        }
        .project-header {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: linear-gradient(90deg, #2b2d42, #3e4a61);
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .profile-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 20px;
            padding: 20px;
            background-color: #3e4a61;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .profile-image {
            border-radius: 50%;
            border: 3px solid #4caf50;
            margin-bottom: 15px;
        }
        .resume-container {
            padding: 20px;
            background-color: #3e4a61;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-top: 30px;
        }
        .resume-button {
            margin-top: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Contact"])

# Animations Function
def animated_text(text, delay=0.05):
    placeholder = st.empty()
    animated_str = ""
    for char in text:
        animated_str += char
        placeholder.markdown(f"### {animated_str}")
        time.sleep(delay)

# Home Page
if page == "Home":
    st.title("🏠 Welcome to My Portfolio")
    
    # Fixed Profile Picture
    st.markdown('<div class="profile-container">', unsafe_allow_html=True)
    # Use a default profile image path - replace with your actual image path
    profile_image_path = "profile.jpg"  # You'll need to place this image in the same directory as your script
    
    # Try to load the profile image, or use a placeholder if it doesn't exist
    try:
        img = Image.open(profile_image_path)
        st.image(img, width=600, output_format="JPEG", clamp=True, channels="RGB", 
                 use_column_width=False, caption="", class_name="profile image")
    except:
        # If image file is not found, display a placeholder message
        st.markdown('<div style="width:150px;height:150px;border-radius:50%;'
                    'background-color:#555;display:flex;justify-content:center;'
                    'align-items:center;color:white;font-weight:bold">'
                    'Profile<br>Photo</div>', unsafe_allow_html=True)
        st.info("Profile photo not found. Please place 'profile.jpg' in the app directory.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    animated_text("Hello! I'm a student passionate about software development.")
    st.success("Explore my portfolio to know more about my work and expertise!")
    
    # Fixed Resume Display Section
    st.markdown('<div class="resume-container">', unsafe_allow_html=True)
    st.title("Resume")
    
    # Replace with the path to your actual resume file
    resume_path = "resume.pdf"
    
    # Display a download button for the resume if it exists
    try:
        with open(resume_path, "rb") as file:
            resume_data = file.read()
            st.download_button(
                label="Download Resume",
                data=resume_data,
                file_name="student_resume.pdf",
                mime="application/pdf",
                key="resume-button",
                help="Click to download my resume"
            )
    except:
        st.warning("Resume file not found. Please place 'resume.pdf' in the app directory.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Projects Page
elif page == "Projects":
    # Enhanced project header
    st.markdown('<div class="project-header">', unsafe_allow_html=True)
    st.title("📂 My Projects")
    st.write("Here are some of the projects I've worked on during my journey as a software developer.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Updated project data - removed the last 5 projects
    project_data = {
        "Student Management System": {
            "desc": "A desktop app built using C# (.NET) and SQLite for managing student records. Includes features for creating, reading, updating, and deleting student information.",
            "img": "https://source.unsplash.com/random/300x200/?student,technology",
            "link": "https://github.com/Baraka-stack/student-management-system"
        },
        "AI-Powered Symptom Checker": {
            "desc": "A web-based tool developed with Python and machine learning algorithms. It analyzes user-submitted symptoms and suggests possible illnesses using trained models.",
            "img": "https://source.unsplash.com/random/300x200/?ai,health",
            "link": "https://github.com/yourusername/ai-symptom-checker"
        },
        "E-commerce Website": {
            "desc": "A fully responsive online store built using Django for the backend and React for the frontend. Features include user authentication, product management, and a payment gateway.",
            "img": "https://source.unsplash.com/random/300x200/?ecommerce,shop",
            "link": "https://github.com/yourusername/e-commerce-website"
        },
        "Task Management App": {
            "desc": "A productivity app that helps users manage tasks efficiently. Built with Node.js and MongoDB, it supports features like task prioritization, deadlines, and notifications.",
            "img": "https://source.unsplash.com/random/300x200/?task,productivity",
            "link": "https://github.com/yourusername/task-management-app"
        },
        "Weather Forecast Web App": {
            "desc": "A weather forecasting web app built using React and the OpenWeatherMap API. Users can input a city and get real-time weather data and forecasts.",
            "img": "https://source.unsplash.com/random/300x200/?weather,forecast",
            "link": "https://github.com/yourusername/weather-forecast-app"
        },
        "Blog Website": {
            "desc": "A personal blog website built with WordPress. Users can post, edit, and comment on articles.",
            "img": "https://source.unsplash.com/random/300x200/?blog,writing",
            "link": "https://github.com/yourusername/blog-website"
        },
        "Portfolio Website": {
            "desc": "A personal portfolio website built with HTML, CSS, and JavaScript. Features a responsive layout and project showcase.",
            "img": "https://source.unsplash.com/random/300x200/?portfolio,developer",
            "link": "https://github.com/yourusername/portfolio-website"
        }
    }
    
    # Create a container for the cards
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    
    # Loop through each project and display as a card
    for project, details in project_data.items():
        st.markdown(f"""
            <div class="card">
                <img src="{details["img"]}" alt="{project}" />
                <div class="card-title">{project}</div>
                <div class="card-desc">{details["desc"]}</div>
                <a href="{details["link"]}" target="_blank"><button>View Project</button></a>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Skills Page
elif page == "Skills":
    st.title("🛠️ My Skills")
    skills = ["Python 🐍", "JavaScript ⚡", "HTML & CSS 🎨", "Django 🌍", "React ⚛️", "SQL 🗄️", "Machine Learning 🤖"]
    st.write("Here are some of the technologies and tools I am proficient in:")
    st.write(", ".join(skills))
    
    st.progress(85)
    st.info("Always learning new technologies to stay updated!")

# Contact Page
elif page == "Contact":
    st.title("📞 Contact Me")
    st.write("Feel free to reach out!")
    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Your Message")
    st.button("Send Message")
