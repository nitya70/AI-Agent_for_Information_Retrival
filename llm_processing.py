import openai
import os

openai.api_key = "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"


def process_with_llm(prompt):
    try:
        """response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
             prompt=prompt,
            max_tokens=50
        )

        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: LLM processing failed. Details: {e}"
"""
import openai

# Directly set your API key here
openai.api_key = "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"

def process_with_llm(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            prompt=prompt
            max_tokens=50
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        breakpoint
        return f"Error: LLM processing failed. Details: {e}"


if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    result = process_with_llm(user_input)
    print(result)
"""