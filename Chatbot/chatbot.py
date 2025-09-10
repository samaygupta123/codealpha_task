def get_bot_response(user_input):
    """
    Returns a predefined response based on user input.
    """
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    elif "your name" in user_input:
        return "I'm just a simple chatbot."
    elif "what can you do" in user_input:
        return "I can chat with you using basic responses!"
    else:
        return "Sorry, I don't understand that."


def main():
    """
    Main function to run the chatbot.
    """
    print("🤖 Simple Chatbot (Type 'bye' to exit)\n")

    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("Bot:", response)

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    main()
