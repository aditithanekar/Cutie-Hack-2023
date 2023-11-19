import openai

# Set your OpenAI API key
openai.api_key = "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"

def answer_Generator(input_text):    
    # Send the input text to the ChatGPT API
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
            max_tokens = 400,
            messages=[
                {"role": "system", "content": "You are a teacher at a university level and your job is to answer each question made by a student step by step showing work"},
                {"role": "user", "content": input_text},
            ]
    )
    # Get the output text from the API response
    output = completion.choices[0].message.content
    return output