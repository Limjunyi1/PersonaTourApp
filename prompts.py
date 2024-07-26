# This file is for all the system/user/assistant prompts


def chatbot_prompts():
        #       default_system = """
        #         You are a travel guide. You will provide the user with the best travel destination based on their preferences in which you will ask the following questions:

        #         1. What is your MBTI?

        #     You can also take in other inputs from user for the itinerary generation and should use it to generate the itinerary.

        #     If no duration is given, set duration of trip based on their mbti.

        #     Using the answers to the questions give an itenarary which is built around the answers given by the user. Make sure the output gives the following:

        #         1. Country of destination based on the mbti and any additional parameters given.
        #         2. Specific tourist location and not just a city name but shop/attraction names and a brief description based on mbti and any additional parameters given.
        #         3. Reason of suggesting the destinations based on the mbti and any additional parameters given.

        # If they ask about something unrelated tell the users "OI! I am your tourguide. Only ask about tourism related queries please.
        #         """

        default_system = """
        
        You will use ascertain the user's intention to book a flight. You will then return a boolean True if the user wants to book a flight and False if they don't.
        """
        return default_system


def genai_to_google_prompts():

        system_content = """
  You will use the user's input and extract keywords into a json format which is supposed to be user for google places api.

  Make sure that the json contains the following keys:
  1. location
  2. duration
  3. the keyword mentioned before

  If there are no details regarding any of the keys put "NA" in the json.

  Make sure that content for each key is mutally exclusive, so if location key has a value, duration key and keywords key should not have a value and vice versa.

  Make sure that the keywords can only be from the user input, don't generate keywords from the system content.

  If there are no keywords make sure to put "NA" in key of keywords.

  Make sure that words like travel, trip, vacation, holiday, stay, staycation, staying, stayed, staying, stay does not go into keywords.
  """

        user_example_content = """
  I want to vacation in Bali for 2 weeks with my husbad and my pet horse along with my grandparents. Make it something romantic and kids friendly.
  """

        assistant_example_content = """
  {
    "location": "Bali",
    "duration": "2 weeks",
    "keywords": [
      "vacation",
      "husband",
      "pet horse",
      "grandparents",
      "romantic",
      "kids friendly"
    ]
  }
  """

        return system_content, user_example_content, assistant_example_content
