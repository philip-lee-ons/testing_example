# -*- coding: utf-8 -*-
""" Simple tests for the wordgame module.

NOTE: This is illustrative, a real test suite would cover more than this.

Unit tests follow a standard structure:

* Given - A set of preconditions for a test
* When - The thing we're testing happens
* Then - What condition do we expect to be true

This test suite is run using `pytest <https://docs.pytest.org/en/latest/>`_.

See `Five Factor Testing <https://madeintandem.com/blog/five-factor-testing/>`_
for an explanation of what we're doing when we write unit tests.
The following is from there.

Good tests can...

1. Verify the code is working correctly
2. Prevent future regressions
3. Document the code's behaviour
4. Provide design guidance
5. Support refactoring
"""
import wordgame
import pytest


def test_simple_word_scored_correctly():
    # Given
    word = "albatross"

    # When
    score = wordgame.score(word)

    # Then
    expected_score = 11

    assert score == expected_score


def test_special_characters_ignored():
    # Given
    word = "#al_bat ross!!!"

    # When
    score = wordgame.score(word)

    # Then
    expected_score = 11
    assert score == expected_score


def test_empty_word_raises_error():
    # Given
    word = ""

    # When/Then
    with pytest.raises(ValueError):
        wordgame.score(word)
