# calling gpt5 model 
from openai import OpenAI
ashu_key = "sk-ashu1234567890abcdefg"  # Replace with your actual API key
client = OpenAI(api_key=ashu_key)

response = client.responses.create(
    model="gpt-4.1-nano",
    input="Write a short bedtime story about a unicorn in 15 words.",
    max_output_tokens=20
)

print(response.output_text)