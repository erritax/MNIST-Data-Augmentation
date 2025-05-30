from google import genai

genai.configure(api_key="ENTER KEY")

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("Explain how AI works in a few words")

print(response.text)