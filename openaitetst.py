import os
import openai
from config import apikey

from openai import OpenAI
oaikey="Your_key"
client = OpenAI(api_key="Your_key")
# sk-proj-PbDCMhmogn0tqh2HkaqfT3BlbkFJCCVzfD9TjMmbVLdZfam0
# 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

response = client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Write an email to boss for resignation"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "logprobs": null,
#       "text": "\n\nSubject: Resignation\n\nDear [Name],\n\nI am writing to inform you of my intention to resign from my current position at [Company]. My last day of work will be [date].\n\nI have enjoyed my time at [Company], and I am grateful for the opportunity to work here. I have learned a great deal during my time in this position, and I am grateful for the experience.\n\nIf I can be of any assistance during this transition, please do not hesitate to ask.\n\nThank you for your understanding.\n\nSincerely,\n[Your Name]"
#     }
#   ],
#   "created": 1683815400,
#   "id": "cmpl-7F1aqg7BkzIY8vBnCxYQh8Xp4wO85",
#   "model": "text-davinci-003",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 125,
#     "prompt_tokens": 9,
#     "total_tokens": 134
#   }
# }
