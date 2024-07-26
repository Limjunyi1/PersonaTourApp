import streamlit as st
from streamlit_option_menu import option_menu
from home import run_home
from booking_flight import run_booking_flights
from chatbot import main
from route import route
from findplaces import api

# Initialize session state attributes if they don't exist
if 'page' not in st.session_state:
    st.session_state.page = 'Home'
if 'page_changed' not in st.session_state:
    st.session_state.page_changed = False


# Function to handle page change and clear session state
def switch_page(page):
    st.session_state.page = page
    st.session_state.page_changed = True
    # Clear all other session state keys except 'page' and 'page_changed'
    for key in list(st.session_state.keys()):
        if key not in ['page', 'page_changed']:
            del st.session_state[key]
    st.experimental_rerun()


# Sidebar navigation with option_menu
selected = option_menu(
    menu_title="PersonaTours",
    options=["Home", "Chatbot", "Booking", "Route", "Discover"],
    icons=["house", "chat", "book", "map", "search"],
    menu_icon="user",
    default_index=["Home", "Chatbot", "Booking", "Route",
                   "Discover"].index(st.session_state.page),
    orientation="horizontal")

# Handle sidebar selection
if selected != st.session_state.page:
    switch_page(selected)

# Display content based on selected page
if st.session_state.page == "Home":
    run_home()

elif st.session_state.page == "Booking":
    run_booking_flights()

elif st.session_state.page == "Chatbot":
    # Ensure 'messages' is initialized
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    main()

elif st.session_state.page == "Route":
    route()

elif st.session_state.page == "Discover":
    api()

# Reset page_changed flag after rerun
if st.session_state.page_changed:
    st.session_state.page_changed = False
