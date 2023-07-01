import openai

openai.api_key = 'your-api-key'
chat_models = "text-davinci-003"

class OpenAIChatGPT:
    @staticmethod
    def execute_chat(scenario):
        response = openai.ChatCompletion.create(
            model=chat_models,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": scenario
                }
            ]
        )
        return response.choices[0].message['content']