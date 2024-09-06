import json

def lambda_handler(event, context):
    """ Main handler for Alexa skill requests """

    if event['request']['type'] == 'LaunchRequest':
        return build_response("Welcome to Qookit, your virtual sous-chef."
                              "What would you like to eat today?")

    elif event['request']['type'] == 'IntentRequest':
        intent_name = event['request']['intent']['name']


def build_response(speech_text):
    return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': speech_text
            },
            'shouldEndSession': False
        }
    }