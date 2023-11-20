# -*- coding: utf-8 -*-
"""
Filename: test_sync_bots.py
Author: Iliya Vereshchagin
Copyright (c) 2023 aBLT.ai. All rights reserved.

Created: 20.11.2023
Last Modified: 20.11.2023

Description:
This file tests for sync bots.
"""

from random import choice
from secrets import token_hex

import pytest

from src.ablt_python_api.schemas import BotSchema
from tests.test_data import ensured_bots, KEY_LENGTH


@pytest.mark.sync
def test_sync_bots_get_bots(api):
    """
    This method tests for  bots: get bots.

    :param api: api fixture
    """
    bots = [BotSchema.model_validate(bot_dict) for bot_dict in api.get_bots()]
    assert len(bots) > 0


@pytest.mark.sync
def test_sync_bots_find_bot_by_uid(api):
    """
    This method tests for  bots: find bot by uid.

    :param api: api fixture
    """
    bots = [BotSchema.model_validate(bot_dict) for bot_dict in api.get_bots()]
    any_bot = choice(bots)
    bot_by_uid = api.find_bot_by_uid(bot_uid=any_bot.uid)
    assert BotSchema.model_validate(bot_by_uid)
    assert bot_by_uid == dict(any_bot)


@pytest.mark.sync
def test_sync_bots_find_bot_by_slug(api):
    """
    This method tests for  bots: find bot by slug.

    :param api: api fixture
    """
    bots = [BotSchema.model_validate(bot_dict) for bot_dict in api.get_bots()]
    any_bot = choice(bots)
    bot_by_slug = api.find_bot_by_slug(bot_slug=any_bot.slug)
    assert BotSchema.model_validate(bot_by_slug)
    assert bot_by_slug == dict(any_bot)


@pytest.mark.sync
def test_sync_bots_find_bot_by_name(api):
    """
    This method tests for  bots: find bot by name.

    :param api: api fixture
    """
    bots = [BotSchema.model_validate(bot_dict) for bot_dict in api.get_bots()]
    any_bot = choice(bots)
    bot_by_name = api.find_bot_by_name(bot_name=any_bot.name)
    assert BotSchema.model_validate(bot_by_name)
    assert bot_by_name == dict(any_bot)


@pytest.mark.sync
def test_sync_bots_ensure_content(api):
    """
    This method tests for  bots: ensure content.

    :param api: api fixture
    """
    any_bot = choice(ensured_bots)
    action = choice((0, 1, 2, 4))
    if action == 0:
        bot_data = api.find_bot_by_uid(bot_uid=any_bot["uid"])
    elif action == 1:
        bot_data = api.find_bot_by_slug(bot_slug=any_bot["slug"])
    elif action == 2:
        bot_data = api.find_bot_by_name(bot_name=any_bot["name"])
    else:
        bot_data = next((bot for bot in api.get_bots() if bot["uid"] == any_bot["uid"]), None)
    assert any_bot == bot_data


@pytest.mark.sync
def test_sync_bots_uid_not_exist(api):
    """
    This method tests for  bots: uid not exist.

    :param api: api fixture
    """
    bot_by_uid = api.find_bot_by_uid(bot_uid=choice(("", token_hex(KEY_LENGTH))))
    assert bot_by_uid is None


@pytest.mark.sync
def test_sync_bots_slug_not_exist(api):
    """
    This method tests for  bots: slug not exist.

    :param api: api fixture
    """
    bot_by_slug = api.find_bot_by_slug(bot_slug=choice(("", token_hex(KEY_LENGTH))))
    assert bot_by_slug is None


@pytest.mark.sync
def test_sync_bots_name_not_exist(api):
    """
    This method tests for  bots: name not exist.

    :param api: api fixture
    """
    bot_by_name = api.find_bot_by_name(bot_name=choice(("", token_hex(KEY_LENGTH))))
    assert bot_by_name is None
