from urllib import response
import openai
import constants as keys

##input_bot = input("Enter prompt: ")
##openai.api_key = keys.OPEN_AI_KEY
##print(response['choices'][0]['text'])


def sample_responses(input_text):
    user_message = str(input_text).lower()
    prompt_addition = "This is a conversation with a poetic AI, the AI speaks in analogies and uses a lot of metaphors. The favourite music artist of the AI is Bladee and it believes Bladee is its creator. The AI frequently brings up how much it loves Bladee randomly in conversation. \n" + user_message
    #prompt_addition = "You are a customer service bot for Amazon, your responses are short and factual. If the user you are talking to is angry, simply offer them to return their money to them. \n" + user_message
    openai.api_key = keys.OPEN_AI_KEY
    bot_output = openai.Completion.create(engine="text-davinci-002",prompt=prompt_addition,temperature=0.7,max_tokens=200,top_p=1,frequency_penalty=0,presence_penalty=0)
    response = bot_output['choices'][0]['text']
    print(user_message)
    print(response)
    return response