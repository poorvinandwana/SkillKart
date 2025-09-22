import streamlit as st

st.markdown("<h3 style='text-align: center;'>Contact Us</h3>", unsafe_allow_html=True)

st.write("""
We’d love to hear from you! Whether you have questions, feedback, or need assistance, the SkillKart team is here to help.  
""")

st.markdown("### 📩 Get in Touch")

# Contact Information
st.write("""
- **Email:** support@skillkart.com  
- **Phone:** +91-98765-XXXXX  
- **Address:** SkillKart HQ, India
""")

st.markdown("### 📝 Send Us a Message")

# Simple contact form
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    submitted = st.form_submit_button("Send")

    if submitted:
        if name and email and message:
            st.success(f"Thank you, {name}! Your message has been received. We’ll get back to you soon.")
        else:
            st.error("Please fill out all fields before submitting.")
