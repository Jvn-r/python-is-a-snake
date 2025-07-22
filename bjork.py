from hugchat import hugchat

# Initialize the default chatbot
chatbot = hugchat.ChatBot()

# Define the career counseling chatbot function
def career_counseling_bot():
    print("Welcome to the Career Counseling Bot!")
    print("I will help you explore different career options based on your interests and skills.")
    
    user_name = input("What is your name? ")
    print(f"Hello {user_name}, let's start with some questions to know more about you.")
    
    skills = input("What skills do you have or enjoy using? (e.g., coding, communication, management) ")
    interests = input("What areas are you most interested in? (e.g., technology, healthcare, arts) ")
    
    # Create a conversational prompt based on user input
    prompt = f"User has skills in {skills} and is interested in {interests}. Can you suggest possible career paths for them?"

    # Get the chatbot's response to the prompt
    response = chatbot.chat(prompt)
    
    print(f"Based on your input, here are some career paths to consider: {response}")

    # Ask if the user needs further guidance on how to pursue those careers
    more_info = input("Would you like some advice on how to pursue these careers? (yes/no) ")
    if more_info.lower() == 'yes':
        advice_prompt = f"Provide advice for someone interested in pursuing a career in {response}. What skills should they focus on?"
        advice = chatbot.chat(advice_prompt)
        print(f"Here's some guidance to help you: {advice}")
    else:
        print("Good luck with your career journey!")

# Start the career counseling bot
career_counseling_bot()
