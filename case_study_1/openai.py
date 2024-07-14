import openai

class OpenAI:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_response(self, prompt):
        completion = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=150
        )
        return completion.choices[0].text.strip()

    def chat_completions(self, messages, model="gpt-3.5-turbo"):
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        return response
