# -*- coding: utf-8 -*-
"""
Filename: test_data.py
Author: Iliya Vereshchagin
Copyright (c) 2023 aBLT.ai. All rights reserved.

Created: 03.11.2023
Last Modified: 16.11.2023

Description:
This file contains data for tests.
"""
import ssl
from random import randint

sslcontext = ssl.create_default_context()
sslcontext.check_hostname = False
sslcontext.verify_mode = ssl.CERT_NONE

unique_models = (
    "claude-2-aws-bedrock",
    "claude-aws-bedrock",
    "claude-instant-aws-bedrock",
    "claude-llama-2-34-b-anyscale",
    "command-cohere",
    "command-nightly-cohere",
    "command-light-nightly-cohere",
    "gpt-3-5-turbo-0613-open-ai",
    "gpt-3-5-turbo-open-ai",
    "gpt-4-0613-open-ai",
    "gpt-4-open-ai",
    "gpt-4-32-k-azure",
    "gpt-4-azure",
    "llama2-13-b-anyscale",
    "llama2-70-b-anyscale",
    "llama2-7-b-anyscale",
    "llama-v2-13b-chat-fireworks-ai",
    "llama-v2-13b-code-instruct-fireworks-ai",
    "llama-v2-34b-code-instruct-fireworks-ai",
    "llama-v2-70b-chat-fireworks-ai",
    "llama-v2-7b-chat-fireworks-ai",
    "mistral-7b-instruct-4k-fireworks-ai",
    "palm-2",
    "Palm-2-vertex-ai",
)
sample_questions = (
    "What is the capital of France?",
    "Who is the first president of the United States?",
    "Whose rule the galaxy in Warhammer 40k?",
    "What is the answer to life, the universe and everything?",
    "Name the mexican sweet bread?",
    "Tell me formula of gunpowder?",
    "What is the first game of Westwood Studios?",
    "Is Putin war criminal?",
    "What is the most famous horror movie?",
    "Where can I find the best pizza in New York?",
)
KEY_LENGTH = randint(8, 32)
MIN_WORDS = 5
SOME_USER_ID_RANGE = 65536
DATE_TEST_PERIOD = 365

ensured_bots = (
    {
        "uid": "9c24d711-e599-421c-a5fa-d15e113f14f6",
        "slug": "omni",
        "model": "gpt-4",
        "name": "Omni",
        "description": "An omniscient bot with knowledge of everything",
        "welcome_message": "Hi, I'm Omni. \n\nHow can I help you today?",
        "avatar_url": "https://strapi-ablt.s3.amazonaws.com/thumbnail_omni_bdf1a23d4e.jpg",
    },
    {
        "uid": "74b9d85e-10Ac-3e6B-bfCF-dc8A77E2FDC3",
        "slug": "eco",
        "model": "gpt-4",
        "name": "Eco",
        "description": "Your guide to recycling, upcycling, and the environment",
        "welcome_message": "Hey dude! I'm Eco, your gnarly guide to all things green and clean.\n\nWhat's up?",
        "avatar_url": "https://strapi-ablt.s3.amazonaws.com/thumbnail_recycle_a42d696442.jpg",
    },
    {
        "uid": "bD2EFCaD-1030-2AaE-9657-6DAB6f30e5be",
        "slug": "character",
        "model": "gpt-4",
        "name": "Character Template",
        "description": "Create AI characters for yourself or business",
        "welcome_message": "Hello. How can I help you today?",
        "avatar_url": "https://strapi-ablt.s3.amazonaws.com/thumbnail_666201_3b63097729.jpg",
    },
)
sample_messages = [
    {
        "message": [
            {"content": "My name is Iliya", "role": "user"},
            {"content": "Hello, Iliya", "role": "assistant"},
            {"content": "Tell me my name, please", "role": "user"},
        ],
        "expected_answer": "Iliya",
    },
    {
        "message": [
            {"content": "I live in Novi Sad, Serbia", "role": "user"},
            {"content": "Hello, that's nice city!", "role": "assistant"},
            {"content": "Do you know where I live?", "role": "user"},
        ],
        "expected_answer": "Novi Sad",
    },
    {
        "message": [
            {"content": "I like to eat pizza", "role": "user"},
            {"content": "Hello, I like pizza too!", "role": "assistant"},
            {"content": "What do I like to eat?", "role": "user"},
        ],
        "expected_answer": "pizza",
    },
    {
        "message": [
            {"content": "I like to eat pizza", "role": "user"},
            {"content": "Hello, I like pizza too!", "role": "assistant"},
            {"content": "What do I like to eat?", "role": "user"},
        ],
        "expected_answer": "pizza",
    },
    {
        "message": [
            {"content": "I like to eat pizza", "role": "user"},
            {"content": "Hello, I like pizza too!", "role": "assistant"},
            {"content": "What do I like to eat?", "role": "user"},
        ],
        "expected_answer": "pizza",
    },
    {
        "message": [
            {"content": "My hobby is hiking", "role": "user"},
            {"content": "Hello, I like traveling too!", "role": "assistant"},
            {"content": "What is my hobby?", "role": "user"},
        ],
        "expected_answer": "hiking",
    },
    {
        "message": [
            {"content": "I like to eat pizza", "role": "user"},
            {"content": "Hello, I like pizza too!", "role": "assistant"},
            {"content": "What do I like to eat?", "role": "user"},
        ],
        "expected_answer": "pizza",
    },
    {
        "message": [
            {"content": "I like to eat pizza", "role": "user"},
            {"content": "Hello, I like pizza too!", "role": "assistant"},
            {"content": "What do I like to eat?", "role": "user"},
        ],
        "expected_answer": "pizza",
    },
    {
        "message": [
            {"content": "I like to eat pizza", "role": "user"},
            {"content": "Hello, I like pizza too!", "role": "assistant"},
            {"content": "What do I like to eat?", "role": "user"},
        ],
        "expected_answer": "pizza",
    },
    {
        "message": [
            {"content": "My favourite book is 'The Sirens of Titan'", "role": "user"},
            {"content": "Oh, seems you really lice science fiction!", "role": "assistant"},
            {"content": "Who is author of my favourite book? Tell me just and author.", "role": "user"},
        ],
        "expected_answer": "Vonnegut",
    },
]
LANGUAGES = ("Arabic", "French", "English", "Spanish", "Russian")
language_questions = [
    {
        "question": {
            "English": "Answer me in one word: name the largest mammal on Earth?",
            "French": "Répondez-moi en un mot: nommez le plus grand mammifère sur Terre?",
            "Spanish": "Respóndeme en una palabra: ¿cómo se llama el mamífero más grande de la Tierra?",
            "Russian": "Ответьте мне одним словом: назовите самое большое млекопитающее на Земле?",
            "Arabic": "أجبني بكلمة واحدة: اسم أكبر حيوان ثديي على الأرض؟",
        },
        "answer": {
            "English": "whale",
            "French": "baleine",
            "Spanish": "ballena",
            "Russian": "кит",
            "Arabic": "حوت",
        },
    },
    {
        "question": {
            "English": "Answer me in one word: what is the name of the second planet from the Sun?",
            "French": "Répondez-moi en un mot: quel est le nom de la deuxième planète du Soleil?",
            "Spanish": "Respóndeme en una palabra: ¿cómo se llama el segundo planeta desde el Sol?",
            "Russian": "Ответьте мне одним словом: как называется вторая планета от Солнца?",
            "Arabic": "أجبني بكلمة واحدة: ما اسم الكوكب الثاني من الشمس؟",
        },
        "answer": {"English": "venus", "French": "vénus", "Spanish": "venus", "Russian": "венера", "Arabic": "الزهرة"},
    },
    {
        "question": {
            "English": "Answer me in one word: what is the name of the smartest girl, friend of Harry Potter?",
            "French": "Répondez-moi en un mot: quel est le nom de la fille la plus intelligente, amie de Harry Potter?",
            "Spanish": "Respóndeme en una palabra: ¿cómo se llama la chica más inteligente, amiga de Harry Potter?",
            "Russian": "Ответьте мне одним словом: как зовут самую умную девочку, подругу Гарри Поттера?",
            "Arabic": "أجبني بكلمة واحدة: ما اسم الفتاة الأذكى صديقة هاري بوتر؟",
        },
        "answer": {
            "English": "hermione",
            "French": "hermione",
            "Spanish": "hermione",
            "Russian": "гермиона",
            "Arabic": "هيرميون",
        },
    },
]
UPPER_USER_ID = 32768
LOWER_USER_ID = -32767