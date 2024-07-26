import streamlit as st
from openai import OpenAI
import os

# OpenAI setup
api_key = os.environ['OPENAI_API_KEY']
# api_key = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=api_key)


def generate_itinerary(last_message):
    # Define the prompt for generating itinerary
    prompt = (
        f"Generate a detailed travel itinerary based on the following last message:\n"
        f"{last_message}\n"
        f"Include a title, pricing, a daily schedule, and reviews from travelers."
    )

    # Call OpenAI API to generate itinerary details
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":
            "system",
            "content":
            "You are an itinerary planner. Generate a detailed travel itinerary based on the provided last message."
        }, {
            "role": "user",
            "content": f"{prompt}"
        }],
        max_tokens=200,
        temperature=0.7)
    return response.choices[0].message.content


def travel_itinerary_tab(last_message):
    st.title("Travel Itinerary")

    # Generate itinerary details from the last message
    itinerary_text = generate_itinerary(last_message)

    # Display the generated itinerary
    st.write(itinerary_text)
