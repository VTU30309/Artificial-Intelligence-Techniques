import openai
import gradio as gr

openai.api_key = "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"

messages = [{"role": "system", "content": 
             "You are a financial expert specializing in real estate investment."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply

demo = gr.Interface(fn=CustomChatGPT, inputs="text", outputs="text", 
                    title="INTELLIGENT CHATBOT")
demo.launch(share=True)
