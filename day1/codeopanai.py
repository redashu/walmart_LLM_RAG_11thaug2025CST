# calling gpt5 model 
from openai import OpenAI
ashu_key = "sk-ashu1234567890abcdefg"  # Replace with your actual API key
client = OpenAI(api_key=ashu_key)

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)