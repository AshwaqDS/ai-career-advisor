from google import genai


class GeminiService:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.chat_session = None

    def start_chat(self, system_prompt):
        self.chat_session = self.client.chats.create(
            model="gemini-2.5-flash",
            config=genai.types.GenerateContentConfig(
                system_instruction=system_prompt,
                max_output_tokens=600,
            )
        )

    def send_message(self, message):
        response = self.chat_session.send_message(message)
        return response.text