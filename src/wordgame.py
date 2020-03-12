# -*- coding: utf-8 -*-
"""Provides scoring functionality for a simple word game.

Each letter in the input word is assigned a score.
The sum of the scores for the letters is the score for the word.

See the following for more information on code style:

* `PEP-8 <https://www.python.org/dev/peps/pep-0008/>`_
* `Google Python Style Guide <https://github.com/google/styleguide/blob/gh-pages/pyguide.md>`_
* `black <https://github.com/psf/black>`_ the uncompromising Python code formatter

    Usage:

    word = 'bacon'
    score = wordgame.score(word)
"""
_LETTER_SCORES = {
    **dict.fromkeys(["E", "A", "I", "O", "N", "R", "T", "L", "S", "U"], 1),
    **dict.fromkeys(["D", "G"], 2),
    **dict.fromkeys(["B", "C", "M", "P"], 3),
    **dict.fromkeys(["F", "H", "V", "W", "Y"], 4),
    **dict.fromkeys(["K"], 5),
    **dict.fromkeys(["J", "X"], 8),
    **dict.fromkeys(["Q", "Z"], 10),
}


def _score_letter(letter: str) -> int:
    return _LETTER_SCORES.get(letter, 0)


def score(word: str) -> int:
    """Calculates the score for a word.

    Takes the input word and calculates the sum of the scores for the individual
    letter.

    Args:
        word: word to be scored
            Case insensitive, special/numeric/non-ASCII characters ignored

    Returns:
        int: Score for the word

    Raises:
        ValueError
    """
    if word == "":
        raise ValueError("Can't score an empty word")

    word = word.upper()
    return sum(map(_score_letter, word))
