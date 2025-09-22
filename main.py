import streamlit as st
from streamlit_carousel import carousel

if "page" not in st.session_state:
    st.session_state.page = "Home"

def Home():
    test = (
        dict(
            title="",
            text="",
            img="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ),
        dict(
            title="",
            text="",
            img="https://plus.unsplash.com/premium_photo-1661908782924-de673a5c6988?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ),
        dict(
            title="",
            text="",
            img="https://plus.unsplash.com/premium_photo-1673958771843-12c73b278bd0?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ),
        dict(
            title="",
            text="",
            img="https://plus.unsplash.com/premium_photo-1667520168395-c1f60f1d6996?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        )
    )
    carousel(items=test, interval=1500)

    st.markdown("<h1 style='text-align: center;'>SkillKart</h1>", unsafe_allow_html=True)
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    col1, col2, col3 = st.columns(3, gap='large')

    with col1:
        st.image("https://plus.unsplash.com/premium_photo-1661911309991-cc81afcce97d?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=450)
        st.write("Electricians")
        if st.button("Book Electricians", key="elec"):
            st.switch_page("pages/Electricians.py")
        st.text("")
        st.text("\n")

    with col2:
        st.image("https://media.istockphoto.com/id/2180801869/photo/working-in-a-kitchen.jpg?s=2048x2048&w=is&k=20&c=1LW56z50sTWav7X-Th78tRMg1rqCKwyUKQjGag5NmdM=", width=450)
        st.write("Plumbers")
        if st.button("Book Plumbers", key="plum"):
            st.switch_page("pages/Plumbers.py")
        st.text("")
        st.text("\n")

    with col3:
        st.image("https://plus.unsplash.com/premium_photo-1661657619286-ef75727fcaef?q=80&w=1169&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=450)
        st.write("Technicians")
        if st.button("Book Technicians", key="tech"):
            st.switch_page("pages/Technicians.py")
        st.text("")
        st.text("\n")

    with col1:
        st.image("https://plus.unsplash.com/premium_photo-1664908457766-61ce2636be21?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=450)
        st.write("Cleaners")
        if st.button("Book Cleaners", key="clean"):
            st.switch_page("pages/Cleaners.py")
        st.text("")
        st.text("\n")

    with col2:
        st.image("https://images.unsplash.com/photo-1683115096447-5d01c11d3ead?q=80&w=1176&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=450)
        st.write("Carpenters")
        if st.button("Book Carpenters", key="carp"):
            st.switch_page("pages/Carpenters.py")
        st.text("")
        st.text("\n")

    with col3:
        st.image("https://media.istockphoto.com/id/509040406/photo/painter-painting-a-wall-with-paint-roller.jpg?s=2048x2048&w=is&k=20&c=ikytuUCTTXc5jwgBng1PjLN23DLrveW_9Aj4NZPIrK0=", width=450)
        st.write("Painters")
        if st.button("Book Painters", key="paint"):
            st.switch_page("pages/Painters.py")
        st.text("")
        st.text("\n")

    with col1:
        st.image("https://plus.unsplash.com/premium_photo-1661964295676-8e76902727ef?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHV0b3JzfGVufDB8fDB8fHww", width=450)
        st.write("Tutors")
        if st.button("Book Tutors", key="tut"):
            st.switch_page("pages/Tutors.py")
        st.text("")
        st.text("\n")

    with col2:
        st.image("https://plus.unsplash.com/premium_photo-1663036991651-82ee96fcc8d5?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=450)
        st.write("Nurses")
        if st.button("Book Nurses", key="nur"):
            st.switch_page("pages/Nurses.py")


pg = st.navigation(
    pages=[
        st.Page(Home, title="Home"),
        st.Page("pages/ContactUs.py", title="Contact Us"),
        st.Page("pages/AboutUs.py", title="About Us"),
        st.Page("pages/Nurses.py", title="Nurses"),
        st.Page("pages/Tutors.py", title="Tutors"),
        st.Page("pages/Technicians.py", title="Technicians"),
        st.Page("pages/Plumbers.py", title="Plumbers"),
        st.Page("pages/Painters.py", title="Painters"),
        st.Page("pages/Electricians.py", title="Electricians"),
        st.Page("pages/Cleaners.py", title="Cleaners"),
        st.Page("pages/Carpenters.py", title="Carpenters"),
    ]
)
pg.run()


pay = st.sidebar.selectbox("Select payment method: ", ['', 'Cash on Delivery', 'UPI', 'Card'])


if pay:

    def customize_toast():
        st.markdown(
            """
            <style>
            div[data-testid=stToast] {
                padding: 20px 10px 40px 10px;
                margin: 10px 400px 200px 10px;
                background-color: #1a3300;
                width: 30%;
            }
            div[data-testid=stToast] * {
                font-size: 15px !important;
                color: #ffffff !important;
                font-family: 'Georgia', sans-serif !important;
                font-style: italic !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    customize_toast()



    st.toast(f"Your serivce is conrfirmed, to be paid by {pay} method. ")
    st.toast("Sit back, relax, and let us handle it! 😌✨")
    st.balloons()
    