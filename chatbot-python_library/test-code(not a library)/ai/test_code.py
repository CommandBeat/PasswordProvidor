def ai_bot():
    print("AI Bot: Hello! I'm your assistant. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("AI Bot: Goodbye! 👋")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("AI Bot: Hi there! How can I help you?")
        elif "how are you" in user_input:
            print("AI Bot: I'm just code, but I'm doing great! 😄")
        elif "your name" in user_input:
            print("AI Bot: I'm your friendly AI assistant.")
        elif "help" in user_input:
            print("AI Bot: Sure! Ask me anything about Python, math, or general knowledge.")
        else:
            print("AI Bot: Hmm, I didn't quite get that. Can you rephrase?")


# Run the bot
ai_bot()
