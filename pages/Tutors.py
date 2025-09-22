import streamlit as st
st.markdown("<h3 style='text-align: center;'>Book a Tutor!</h3>", unsafe_allow_html=True)
st.write("\n")
st.write("\n")

col1,col2 = st.columns(2)

with col1:
    st.write("\n")
    st.image("pics/tut1.png", width=300)

    st.write("\n")
    st.image("pics/tut2.png", width=300)


    st.write("\n")
    st.image("pics/tut3.png", width=300)


    st.write("\n")
    st.image("pics/tut4.png", width=300)

with col2:
    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("ABC Coaching")
    st.write("98765-XXXXX")
    a = st.button("Book Now", key="abc")
    b = st.selectbox("Pick a slot: ", ['','1:00 p.m. - 3:00 p.m.', '3:00 p.m. - 5:00 p.m.', '5:00 p.m. - 7:00 p.m.', '7:00 p.m. - 9:00 p.m.'], key="abcslot")
    if a:
        st.success("Your booking is confirmed. ABC Coaching are on their way!")
        st.write("Kindly select a payment method from the sidebar.")
    elif b:
        st.success(f"Your booking has been confirmed for the slot {b}")
        st.write("Kindly select a payment method from the sidebar.")

    st.write("\n")
    st.write("\n")
    st.write("DEF Coaching")
    st.write("87521-XXXXX")
    a = st.button("Book Now", key="jini")
    b = st.selectbox("Pick a slot: ", ['','1:00 p.m. - 3:00 p.m.', '3:00 p.m. - 5:00 p.m.', '5:00 p.m. - 7:00 p.m.', '7:00 p.m. - 9:00 p.m.'], key="jinislot")
    if a:
        st.success("Your booking is confirmed. DEF Coaching are on their way!")
        st.write("Kindly select a payment method from the sidebar.")
    elif b:
        st.success(f"Your booking has been confirmed for the slot {b}")
        st.write("Kindly select a payment method from the sidebar.")

    st.write("\n")
    st.write("\n")
    
    st.write("\n")
    st.write("PQR Coaching")
    st.write("73156-XXXXX")
    a = st.button("Book Now", key="pqr")
    b = st.selectbox("Pick a slot: ", ['','1:00 p.m. - 3:00 p.m.', '3:00 p.m. - 5:00 p.m.', '5:00 p.m. - 7:00 p.m.', '7:00 p.m. - 9:00 p.m.'], key="pqrslot")
    if a:
        st.success("Your booking is confirmed. PQR Coaching are on their way!")
        st.write("Kindly select a payment method from the sidebar.")
    elif b:
        st.success(f"Your booking has been confirmed for the slot {b}")
        st.write("Kindly select a payment method from the sidebar.")


    st.write("\n")
    st.write("\n")
    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("XYZ Coaching")
    st.write("97019-XXXXX")
    a = st.button("Book Now", key="rakhi")
    b = st.selectbox("Pick a slot: ", ['','1:00 p.m. - 3:00 p.m.', '3:00 p.m. - 5:00 p.m.', '5:00 p.m. - 7:00 p.m.', '7:00 p.m. - 9:00 p.m.'], key="rakhislot")
    if a:
        st.success("Your booking is confirmed. XYZ Coaching are on their way!")
        st.write("Kindly select a payment method from the sidebar.")
    elif b:
        st.success(f"Your booking has been confirmed for the slot {b}")
        st.write("Kindly select a payment method from the sidebar.")
