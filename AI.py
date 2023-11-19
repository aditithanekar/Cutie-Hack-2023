import openai

# Set your OpenAI API key
openai.api_key = "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"

def answer_Generator(input_text):    
    # Send the input text to the ChatGPT API
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a useful assistant"},
            {"role": "user", "content": input_text},
        ]
    )
    # Get the output text from the API response
    output = completion.choices[0].message.content
    return output