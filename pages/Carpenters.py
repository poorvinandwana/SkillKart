import streamlit as st
st.markdown("<h3 style='text-align: center;'>Book a Carpenter!</h3>", unsafe_allow_html=True)
st.write("\n")
st.write("\n")

col1,col2 = st.columns(2)

with col1:
    st.write("\n")
    st.image("pics/carp1.png", width=300)

    st.write("\n")
    st.image("pics/carp2.png", width=300)


    st.write("\n")
    st.image("pics/carp3.png", width=300)


    st.write("\n")
    st.image("pics/carp4.png", width=300)

with col2:
    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("ABC Carpenters")
    st.write("98765-XXXXX")
    a = st.button("Book Now", key="abc")
    b = st.selectbox("Pick a slot: ", ['','1:00 p.m. - 3:00 p.m.', '3:00 p.m. - 5:00 p.m.', '5:00 p.m. - 7:00 p.m.', '7:00 p.m. - 9:00 p.m.'], key="abcslot")
    if a:
        st.success("Your booking is confirmed. ABC Carpenters are on their way!")
        st.write("Kindly select a payment method from the sidebar.")
    elif b:
        st.success(f"Your booking has been confirmed for the slot {b}")
        st.write("Kindly select a payment method from the sidebar.")

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("DEF Carpenters")
    st.write("87521-XXXXX")
    a = st.button("Book Now", key="jini")
    b = st.selectbox("Pick a slot: ", ['','1:00 p.m. - 3:00 p.m.', '3:00 p.m. - 5:00 p.m.', '5:00 p.m. - 7:00 p.m.', '7:00 p.m. - 9:00 p.m.'], key="jinislot")
    if a:
        st.success("Your booking is confirmed. DEF Carpenters are on their way!")
        st.write("Kindly select a payment method from the sidebar.")
    elif b:
        st.success(f"Your booking has been confirmed for the slot {b}")
        st.write("Kindly select a payment method from the sidebar.")

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("PQR Carpenters")
    st.write("73156-XXXXX")
    a = st.button("Book Now", key="pqr")
    b = st.selectbox("Pick a slot: ", ['','1:00 p.m. - 3:00 p.m.', '3:00 p.m. - 5:00 p.m.', '5:00 p.m. - 7:00 p.m.', '7:00 p.m. - 9:00 p.m.'], key="pqrslot")
    if a:
        st.success("Your booking is confirmed. PQR Carpenters are on their way!")
        st.write("Kindly select a payment method from the sidebar.")
    elif b:
        st.success(f"Your booking has been confirmed for the slot {b}")
        st.write("Kindly select a payment method from the sidebar.")


    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("XYZ Carpenters")
    st.write("97019-XXXXX")
    a = st.button("Book Now", key="rakhi")
    b = st.selectbox("Pick a slot: ", ['','1:00 p.m. - 3:00 p.m.', '3:00 p.m. - 5:00 p.m.', '5:00 p.m. - 7:00 p.m.', '7:00 p.m. - 9:00 p.m.'], key="rakhislot")
    if a:
        st.success("Your booking is confirmed. XYZ Carpenters are on their way!")
        st.write("Kindly select a payment method from the sidebar.")
    elif b:
        st.success(f"Your booking has been confirmed for the slot {b}")
        st.write("Kindly select a payment method from the sidebar.")
