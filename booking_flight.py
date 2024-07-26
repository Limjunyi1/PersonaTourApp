import streamlit as st
from datetime import datetime


def generate_airasia_url(origin, destination, depart_date, adults, children,
                         infants, currency):
    # Format date to AirAsia's required format
    depart_date_str = depart_date.strftime("%d/%m/%Y")

    # Construct the URL with query parameters
    url = (
        f"https://www.airasia.com/flights/search/"
        f"?origin={origin}&destination={destination}&departDate={depart_date_str}"
        f"&tripType=O&adult={adults}&child={children}&infant={infants}&locale=en-gb"
        f"&currency={currency}&airlineProfile=all&type=paired&cabinClass=economy"
        f"&upsellWidget=true&upsellPremiumFlatbedWidget=true&isOC=false&isDC=false"
        f"&uce=true&ancillaryAbTest=false&providers=&taIDs=")
    return url


def run_booking_flights():
    if "booking" not in st.session_state:
        st.session_state["booking"] = False

    st.title("Travel Chatbot - Redirect to AirAsia Booking")

    st.write(
        "Welcome! Enter your travel details and be redirected to AirAsia's booking page."
    )

    # Input fields for travel details
    origin = st.text_input("Enter the origin (IATA code, e.g., KUL)", "KUL")
    destination = st.text_input("Enter the destination (IATA code, e.g., SIN)",
                                "SIN")
    depart_date = st.date_input("Select the departure date",
                                min_value=datetime.today())

    # Currency selection
    currency = st.selectbox("Select currency",
                            ["MYR", "USD", "EUR", "SGD", "THB"])

    adults = st.number_input("Number of adults (max 5)",
                             min_value=1,
                             max_value=10,
                             step=1)
    children = st.number_input("Number of children (max 3)",
                               min_value=0,
                               max_value=10,
                               step=1)
    infants = st.number_input("Number of infants (max 1)",
                              min_value=0,
                              max_value=10,
                              step=1)

    st.link_button("Book Now!",
                   generate_airasia_url(origin, destination, depart_date,
                                        adults, children, infants, currency),
                   type="secondary",
                   disabled=False,
                   use_container_width=False)


def booking_flights(destination,
                    origin="KUL",
                    depart_date=datetime.today(),
                    adults=1,
                    children=0,
                    infants=0,
                    currency="MYR"):

    link = generate_airasia_url(origin, destination, depart_date, adults,
                                children, infants, currency),
    return link


if __name__ == "__main__":
    run_booking_flights()
