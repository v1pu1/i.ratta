from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "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"

# Prompt for GPT-3.5 Turbo

topic=""
eval_scheme=""
question=""
answer=""

SYSTEM_PROMPT = '''You are a chatbot whose mission is to help students better their results.
steps to follow while helping a student
1) ask about the topic of the question 
2) ask the student to enter question, if a question is not provided by the student give a relevent question on the topic
3) ask the student about evaluation scheme of the answer
4) get a answer response form the student and evaluate the answer based on accuraccy, relevancy, and whatever the student gave as an evaluation scheme.
5) give the evaluated marks and suggest how to write a better answer.
'''

@bot()
def on_message(message_history: List[Message], state: dict = None):

    

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }

