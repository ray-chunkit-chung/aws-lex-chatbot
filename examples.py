
import boto3

# Initialize the Bedrock client
bedrock_client = boto3.client('bedrock')

# Define the agents
agents = [
    {
        'name': 'Agent1',
        'model': 'anthropic_claude',
        'task': 'greeting'
    },
    {
        'name': 'Agent2',
        'model': 'amazon_titan',
        'task': 'faq'
    }
]

# Function to get response from Bedrock
def get_response(agent_name, user_input):
    response = bedrock_client.invoke_model(
        ModelId=agent_name,
        InputText=user_input
    )
    return response['OutputText']

# Example interaction
user_input = "Hello, how can I reset my password?"
response = get_response('Agent2', user_input)
print(response)

#############################################################

import boto3

# Initialize the Lex client
lex_client = boto3.client('lex-runtime')

# Function to get response from Lex
def get_lex_response(bot_name, bot_alias, user_id, user_input):
    response = lex_client.post_text(
        botName=bot_name,
        botAlias=bot_alias,
        userId=user_id,
        inputText=user_input
    )
    return response['message']

# Example interaction
bot_name = 'OrderFlowers'
bot_alias = 'Prod'
user_id = 'user123'
user_input = "I want to order flowers."

response = get_lex_response(bot_name, bot_alias, user_id, user_input)
print(response)
