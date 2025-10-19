
import streamlit as st

st.set_page_config(page_title="GPA & CGPA Calculator", page_icon="🎓")
st.title("🎓 GPA & CGPA Calculator")

# GPA calculation function
def calculate_gpa(marks):
    points = []
    for m in marks:
        if m >= 85:
            points.append(4.0)
        elif m >= 80:
            points.append(3.7)
        elif m >= 75:
            points.append(3.3)
        elif m >= 70:
            points.append(3.0)
        elif m >= 65:
            points.append(2.7)
        elif m >= 60:
            points.append(2.3)
        elif m >= 55:
            points.append(2.0)
        elif m >= 50:
            points.append(1.7)
        else:
            points.append(0.0)
    return round(sum(points) / len(points), 2)

# --- GPA Section ---
st.header("📘 GPA Calculator")
num_subjects = st.number_input("Enter number of subjects:", min_value=1, max_value=15, step=1, key="num_sub")
marks = [st.number_input(f"Enter marks for Subject {i+1}:", min_value=0, max_value=100, step=1, key=f"m{i}") for i in range(num_subjects)]

if st.button("Calculate GPA", key="calc_gpa"):
    gpa = calculate_gpa(marks)
    st.success(f"✅ Your GPA is: {gpa}")
    st.session_state["latest_gpa"] = gpa  # Save GPA for CGPA use

# --- Divider ---
st.write("---")

# --- CGPA Section ---
st.header("📗 CGPA Calculator")
prev_cgpa = st.number_input("Enter previous CGPA:", min_value=0.0, max_value=4.0, step=0.01, key="prev_cgpa")
prev_sem = st.number_input("Enter number of previous semesters:", min_value=0, step=1, key="prev_sem")

if st.button("Calculate CGPA", key="calc_cgpa"):
    if prev_sem > 0:
        gpa = st.session_state.get("latest_gpa", None)
        if gpa is None:
            st.warning("Please calculate GPA first before calculating CGPA.")
        else:
            cgpa = ((prev_cgpa * prev_sem) + gpa) / (prev_sem + 1)
            st.success(f"🎯 Your Updated CGPA is: {round(cgpa, 2)}")
    else:
        st.info("Add previous semester details to calculate CGPA.")
