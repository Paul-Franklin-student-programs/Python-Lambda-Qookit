import json

def lambda_handler(event, context):
    """ Main handler for Alexa skill requests """

    if event['request']['type'] == 'LaunchRequest':
        return build_response("Welcome to Qookit, your virtual sous-chef."
                              "What would you like to eat today?")

    elif event['request']['type'] == 'IntentRequest':
        intent_name = event['request']['intent']['name']

        if intent_name == 'HelloWorldIntent':
            return build_response("Hello, world!")

        elif intent_name == 'GetRecipeSuggestionBasedOnPantryIntent':
            return build_response("FIXME: add response")

        elif intent_name == 'GetNextStepInRecipeIntent':
            return build_response("FIXME: add response")

        elif intent_name == 'ManuallyAddFoodItemsToPantryIntent':
            return build_response("FIXME: add response")

        elif intent_name == 'GetRecipeSuggestionBasedOnPantryIntent':
            return build_response("FIXME: add response")

        elif intent_name == 'FindRecipeByNameIntent':
            return build_response("FIXME: add response")

        elif intent_name == 'FindRecipeByIngredientIntent':
            return build_response("FIXME: add response")

        elif intent_name == 'FindRecipeByTypeIntent':
            return build_response("FIXME: add response")

        elif intent_name == 'AddDietaryRestriction':
            return build_response("FIXME: add response")

        elif intent_name == 'AMAZON.CancelIntent':
            return build_response("FIXME: add response")

        elif intent_name == 'AMAZON.HelpIntent':
            return build_response("FIXME: add response")

        elif intent_name == 'AMAZON.StopIntent':
            return build_response("FIXME: add response")

        elif intent_name == 'AMAZON.NavigateHomeIntent':
            return build_response("FIXME: add response")

        elif intent_name == 'AMAZON.FallbackIntent':
            return build_response("FIXME: add response")

        else:
            return build_response("Sorry, I don't know that command.")

    return build_response("Something went wrong. Please try again.")


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