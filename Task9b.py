import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready! Type 'quit()' to exit.")

while True:
    message = input()
    if message == "quit()":
        break
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
