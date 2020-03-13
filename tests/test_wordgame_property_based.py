# -*- coding: utf-8 -*-
"""Demonstration of property based testing.

Property based testing is based on the idea of testing invariants
i.e. things which should always be true.
The testing library (here we use `hypothesis`) then tries to generate the simplest
test case which violates the invariant.

For example consider the function `reverse` which reverses the ordering of a `list`.
Performing `reverse` twice should always recover the original ordering:

    original = list(some_list)
    some_list.reverse()
    some_list.reverse()
    assert original == some_list

This is our invariant.

See `Hypothesis <https://hypothesis.readthedocs.io/en/latest/>` for the details
of the `hypothesis` library used in these tests
(as well as more information on property based testing in general).
"""
import random

import hypothesis.strategies as st
from hypothesis import given, example

import wordgame


@given(word=st.from_regex(r"[A-Za-z]+"))
@example("albatross")
def test_score_indepent_of_order(word):
    # Given
    shuffled_text = list(word)
    random.shuffle(shuffled_text)
    shuffled_text = "".join(shuffled_text)

    # When
    text_score = wordgame.score(word)
    shuffled_score = wordgame.score(shuffled_text)

    # Then
    assert text_score == shuffled_score


@given(letter=st.from_regex(r"[A-Za-z]", fullmatch=True),
       repeat=st.integers(min_value=1, max_value=100))
def test_repeated_letters_multiplies_score(letter, repeat):
    # Given
    word = letter * repeat

    # When
    letter_score = wordgame.score(letter)
    word_score = wordgame.score(word)

    # Then
    assert letter_score * repeat == word_score
