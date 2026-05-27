import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3

# PAGE CONFIG
st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

# DATABASE CONNECTION
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    stream TEXT,
    roll INTEGER,
    phone TEXT,
    address TEXT
)
""")

conn.commit()

# CUSTOM CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stApp {
    background: linear-gradient(to right, #0f0c29, #302b63, #24243e);
}

h1, h2, h3 {
    color: white;
}

div.stButton > button {
    background: linear-gradient(to right, #fc466b, #3f5efb);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    border: none;
    font-size: 18px;
}

div.stButton > button:hover {
    background: linear-gradient(to right, #3f5efb, #fc466b);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #141e30, #243b55);
}

.card {
    background-color: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR MENU
with st.sidebar:

    selected = option_menu(
        menu_title="SMS Dashboard",
        options=[
            "Dashboard",
            "Add Student",
            "View Students"
        ],
        icons=[
            "house",
            "person-plus",
            "table"
        ],
        menu_icon="cast",
        default_index=0,
    )

# TITLE
st.title("🎓 Student Management System")
st.write("Modern Streamlit Web Application")

# DASHBOARD
if selected == "Dashboard":

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
        <h2>{total_students}</h2>
        <p>Total Students</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h2>5</h2>
        <p>Total Streams</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h2>100%</h2>
        <p>Database Connected</p>
        </div>
        """, unsafe_allow_html=True)

# ADD STUDENT
elif selected == "Add Student":

    st.subheader("➕ Add Student")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Student Name")
        age = st.number_input("Age", 1, 100)
        stream = st.text_input("Stream")
        roll = st.number_input("Roll Number", 1, 1000)

    with col2:
        phone = st.text_input("Phone Number")
        address = st.text_area("Address")

    if st.button("Save Student"):

        cursor.execute(
            """
            INSERT INTO students
            (name, age, stream, roll, phone, address)

            VALUES (?, ?, ?, ?, ?, ?)
            """,

            (
                name,
                age,
                stream,
                roll,
                phone,
                address
            )
        )

        conn.commit()

        st.success("✅ Student Saved Successfully")

# VIEW STUDENTS
elif selected == "View Students":

    st.subheader("📋 Student Records")

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    df = pd.DataFrame(
        rows,
        columns=[
            "ID",
            "Name",
            "Age",
            "Stream",
            "Roll",
            "Phone",
            "Address"
        ]
    )

    st.dataframe(df, use_container_width=True)

# CLOSE CONNECTION
conn.close()