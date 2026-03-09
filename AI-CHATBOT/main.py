from openai import OpenAI

client = OpenAI(api_key="sorry cant reveal")

messages = []

def completion(user_message):
    global messages

    messages.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    assistant_message = response.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": assistant_message
    })

    print(f"Bro: {assistant_message}")


if __name__ == "__main__":
    print("Bro: Hi I'm your bro. Ask me anything!")

    while True:
        user_question = input("You: ")

        if user_question.lower() in ["exit", "quit"]:
            print("Bro: Bye!")
            break

        completion(user_question)
