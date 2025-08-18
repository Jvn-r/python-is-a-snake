from hugchat import hugchat

chatbot = hugchat.ChatBot()


def career_counseling_bot():
    print("Welcome to the Career Counseling Bot!")
    print("I will help you explore different career options based on your interests and skills.")
    
    user_name = input("What is your name? ")
    print(f"Hello {user_name}, let's start with some questions to know more about you.")
    
    skills = input("What skills do you have or enjoy using? (e.g., coding, communication, management) ")
    interests = input("What areas are you most interested in? (e.g., technology, healthcare, arts) ")
    
    prompt = f"User has skills in {skills} and is interested in {interests}. Can you suggest possible career paths for them?"

    response = chatbot.chat(prompt)
    
    print(f"Based on your input, here are some career paths to consider: {response}")

    more_info = input("Would you like some advice on how to pursue these careers? (yes/no) ")
    if more_info.lower() == 'yes':
        advice_prompt = f"Provide advice for someone interested in pursuing a career in {response}. What skills should they focus on?"
        advice = chatbot.chat(advice_prompt)
        print(f"Here's some guidance to help you: {advice}")
    else:
        print("Good luck with your career journey!")

career_counseling_bot()