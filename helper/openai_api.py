import os


import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')


def text_complition(prompt: str) -> dict:
    '''
    Call OpenAI API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict with 'status' and 'response' fields
    '''
    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            max_tokens=100,
            temperature=0.7,
            n=1,
            stop=None,
            #log_level="info"
        )
        
        if response and 'choices' in response and len(response['choices']) > 0:
            return {
                'status': 1,
                'response': response['choices'][0]['text']
            }
        else:
            return {
                'status': 0,
                'response': ''
            }
    except Exception as e:
        return {
            'status': 0,
            'response': str(e)
        }
