# -*- coding: utf-8 -*-
"""The Queen's Mirror / Artist Point invitation reveal app."""

import random
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler,
    AbstractExceptionHandler,
    AbstractRequestInterceptor,
    AbstractResponseInterceptor,
)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

voice_start = '<voice name="Joey">'
voice_end = "</voice>"

SKILL_NAME = "The Queen's Mirror"
HELP_MESSAGE = voice_start + "How may I help you?" + voice_end
HELP_REPROMPT = voice_start + "What can I help you with?" + voice_end
STOP_MESSAGE = voice_start + "Goodbye." + voice_end
FALLBACK_MESSAGE = HELP_REPROMPT
FALLBACK_REPROMPT = HELP_REPROMPT
EXCEPTION_MESSAGE = voice_start + "Sorry. I cannot help you with that." + voice_end

exaltations = [
    "I'm delighted to share that",
    "I'm elated to tell you that",
    "I'm pleased to share that",
    "",
    "",
    "",
    "",
    "",
]

queen_names = [
    "The Evil Queen",
    "The Queen",
    "Her Majesty the Evil Queen",
    "Her Majesty the Queen",
]

snow_white_names = [
    "Snow White",
    "Princess Snow White",
]

invitation_variations = [
    "has chosen",
    "has invited",
]

child2_names = [
    "Child2_FirstName",
    "Child2_FirstName Child2_MiddleName Family_LastName",
    "Child2_FirstName Family_LastName",
]

child1_names = [
    "Child1_FirstName",
    "Child1_FirstName Child1_MiddleName Family_LastName",
    "Child1_FirstName Family_LastName",
]

both_names = [
    "Child2_FirstName and Child1_FirstName",
    "Child1_FirstName and Child2_FirstName",
    "Child1_FirstName and Child2_FirstName Family_LastName",
    "Child2_FirstName and Child1_FirstName Family_LastName",
    "Child1_FirstName Child1_MiddleName and Child2_FirstName Child2_MiddleName Family_LastName",
    "Child2_FirstName Child2_MiddleName Family_LastName and Child1_FirstName Child1_MiddleName Family_LastName",
]

queen_dinner_variations = [
    "to join her for dinner",
    "to dine with her",
    "to join her for dinner",
    "to dine with her",
    "to join her for dinner",
    "to dine with her",
    "to join her and her minions for dinner",
    "to dine with her and her minions",
    "to join her and her evil minions for dinner",
    "to dine with her and her evil minions",
]

snow_white_dinner_variations = [
    "to join her for dinner",
    "to dine with her",
    "to join her for dinner",
    "to dine with her",
    "to join her for dinner",
    "to dine with her",
    "to join her and her dwarf friends for dinner",
    "to dine with her and her dwarf friends",
    "to join her and the seven dwarfs for dinner",
    "to dine with her and the seven dwarfs",
]


plural_dinner_variations = [
    "to join them for dinner",
    "to dine with them",
    "to dine with them and their friends",
    "to join them and their friends for dinner",
]


restaurant_names = [
    "at Artist Point",
    "",
    "",
    ""
]

park_names = [
    "at the Wilderness Lodge",
    "at Disneyworld",
    "",
    "",
]

geographic_names = [
    "in Orlando",
    "in Orlando Florida",
    "in Florida",
    "",
    "",
    "",
]

event_times = [
    "in December",
    "on the last night of the Family_LastName Family's vacation",
    "",
    "",
    "",
]


dwarfs_idea = [
    "I think it might have been Dopey's idea",
    "I think it was Dopey's idea",
    "It was probably Dopey's idea",
    "It was Dopey's idea",
]

# =========================================================================================================================================

sb = SkillBuilder()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def string_builder(phrase_options):
    phrase = random.choice(phrase_options)
    if phrase:
        phrase += " "
    return phrase


# Intent Handlers
class EvilQueenHandler(AbstractRequestHandler):
    """Handler for EvilQueen Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("EvilQueenIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In EvilQueenHandler")

        speech = " "
        speech += string_builder(exaltations)
        speech += string_builder(queen_names)
        speech += string_builder(invitation_variations)
        speech += string_builder(child2_names)
        speech += string_builder(queen_dinner_variations)
        speech += string_builder(restaurant_names)
        speech += string_builder(park_names)
        speech += string_builder(geographic_names)
        speech += string_builder(event_times)

        handler_input.response_builder.speak(voice_start + speech + voice_end).set_card(
            SimpleCard(SKILL_NAME, speech)
        )
        return handler_input.response_builder.response


class SnowWhiteHandler(AbstractRequestHandler):
    """Handler for SnowWhite Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("SnowWhiteIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SnowWhiteHandler")

        speech = " "
        speech += string_builder(exaltations)
        speech += string_builder(snow_white_names)
        speech += string_builder(invitation_variations)
        speech += string_builder(child1_names)
        speech += string_builder(snow_white_dinner_variations)
        speech += string_builder(restaurant_names)
        speech += string_builder(park_names)
        speech += string_builder(geographic_names)
        speech += string_builder(event_times)

        handler_input.response_builder.speak(voice_start + speech + voice_end).set_card(
            SimpleCard(SKILL_NAME, speech)
        )
        return handler_input.response_builder.response


class BothHandler(AbstractRequestHandler):
    """Handler for BothIntent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("BothIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In BothHandler")

        speech = " "
        speech += string_builder(exaltations)
        speech += string_builder(snow_white_names)
        speech += "and "
        speech += string_builder(queen_names)
        speech += "invite "
        speech += string_builder(both_names)
        speech += string_builder(plural_dinner_variations)
        speech += string_builder(restaurant_names)
        speech += string_builder(park_names)
        speech += string_builder(geographic_names)
        speech += string_builder(event_times)

        handler_input.response_builder.speak(voice_start + speech + voice_end).set_card(
            SimpleCard(SKILL_NAME, speech)
        )
        return handler_input.response_builder.response

class ParentHandler(AbstractRequestHandler):
    """Handler for ParentIntent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("ParentIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In BothHandler")

        speech = "The Seven Dwarfs invited Mommy and Daddy. "
        speech += string_builder(dwarfs_idea)

        handler_input.response_builder.speak(voice_start + speech + voice_end).set_card(
            SimpleCard(SKILL_NAME, speech)
        )
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")

        handler_input.response_builder.speak(HELP_MESSAGE).ask(HELP_REPROMPT).set_card(
            SimpleCard(SKILL_NAME, HELP_MESSAGE)
        )
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name(
            "AMAZON.StopIntent"
        )(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")

        handler_input.response_builder.speak(STOP_MESSAGE)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.

    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")

        handler_input.response_builder.speak(FALLBACK_MESSAGE).ask(FALLBACK_REPROMPT)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")

        logger.info(
            "Session ended reason: {}".format(
                handler_input.request_envelope.request.reason
            )
        )
        return handler_input.response_builder.response


# Exception Handler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.info("In CatchAllExceptionHandler")
        logger.error(exception, exc_info=True)

        handler_input.response_builder.speak(EXCEPTION_MESSAGE).ask(HELP_REPROMPT)

        return handler_input.response_builder.response


# Request and Response loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the alexa requests."""

    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(handler_input.request_envelope.request))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the alexa responses."""

    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.debug("Alexa Response: {}".format(response))


# Register intent handlers
sb.add_request_handler(EvilQueenHandler())
sb.add_request_handler(ParentHandler())
sb.add_request_handler(SnowWhiteHandler())
sb.add_request_handler(BothHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Register exception handlers
sb.add_exception_handler(CatchAllExceptionHandler())

# Request, response logs.
sb.add_global_request_interceptor(RequestLogger())
sb.add_global_response_interceptor(ResponseLogger())

# Handler name that is used on AWS lambda
lambda_handler = sb.lambda_handler()
