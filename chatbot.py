import streamlit as st
from openai import OpenAI
import os
from cards import travel_packages_tab
from context import context

# Initialize OpenAI client with your API key
my_secret = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=my_secret)

# Initialize session state attributes if they don't exist
if 'page' not in st.session_state:
  st.session_state.page = 'Chatbot'
if 'page_changed' not in st.session_state:
  st.session_state.page_changed = False

if 'page' in st.session_state and 'page_changed' in st.session_state and st.session_state.page_changed == True:
  st.session_state.page_changed = False


# Function to handle page change
def switch_page(page):
  st.session_state.page = page
  st.session_state.page_changed = True


# Function to check if the user wants to book a flight
def check_booking_intent(messages):
  for message in messages:
    if message['role'] == 'user':
      if any(keyword in message["content"].lower() for keyword in
             ["book a flight", "go", "travel", "fly", "book", "flight"]):
        return True
  return False


def check_itinerary_intent(messages):
  for message in messages:
    if message['role'] == 'assistant':
      if any(
          keyword in message["content"].lower()
          for keyword in ["click on the button to generate related packages"]):
        return True
  return False


def check_route_intent(messages):
  for message in messages:
    if message['role'] == 'assistant':
      if any(keyword in message["content"].lower()
             for keyword in ["click on the button to plan route"]):
        return True
  return False


# Function to get assistant response
def get_assistant_response():
  # Chat input and response
  system_message = {"role": "system", "content": context}
  st.session_state.messages.append(system_message)
  if prompt := st.chat_input("Ask me a travel query!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
      st.markdown(prompt)
    with st.chat_message("assistant"):
      stream = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[{
              "role": m["role"],
              "content": m["content"]
          } for m in st.session_state.messages],
          stream=True,
          max_tokens=500,
          temperature=1.2)
      response = st.write_stream(stream)
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
    return response


# Main function to run the Streamlit app
def main():
  st.title("Flight Booking Chatbot")
  if "messages" not in st.session_state:
    st.session_state["messages"] = []
    system_message = {"role": "system", "content": context}
    st.session_state.messages.append(system_message)

  greeting = """
  Hello there I am your personal 24/7 travel support do ask me anything regarding anything related to travelling or ask any of the following questions: 
  1. Book me a flight.
  2. Suggest me an itinerary based on my preferences.
  3. Plan route.
  """
  # Greeting
  with st.chat_message("assistant"):
    st.write(f'{greeting}')

  # Display chat history
  for message in st.session_state.messages:
    if message["content"] != context or message["role"] != "system":
      with st.chat_message(message["role"]):
        st.markdown(message["content"])
      if message["role"] == "assistant":
        last_assistant_message = message["content"]

  # Get assistant response
  assistant_response = get_assistant_response()

  # Check if the user wants to book a flight
  booking_intent = check_booking_intent(st.session_state.messages)

  itinerary_intent = check_itinerary_intent(st.session_state.messages)

  route_intent = check_route_intent(st.session_state.messages)

  # # Display the booking intent as boolean
  # st.write("Booking Intent:", booking_intent)

  # # Display the booking intent as boolean
  # st.write("itinerary Intent:", itinerary_intent)

  if booking_intent:
    if st.button("End chat and book a flight"):
      switch_page("Booking")

  if itinerary_intent:
    if st.button("End chat and generate itinerary"):
      travel_packages_tab(last_assistant_message)

  if route_intent:
    if st.button("End chat and plan route"):
      switch_page("Route")

  # Rerun the app only if the page changed
  if st.session_state.page_changed:
    st.session_state.page_changed = False
    st.experimental_rerun()


if __name__ == "__main__":
  main()
