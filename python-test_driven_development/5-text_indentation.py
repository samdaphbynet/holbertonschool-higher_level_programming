#!/usr/bin/python3
"""
This module print text with indentation.
Module: text_indentation
Function: text_indentation
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punctuation_marks = ['.', '?', ':']
    lines = []
    result = ''

    for char in text:
        result += char
        if char in punctuation_marks:
            lines.append(result.strip())
            result = ''
    lines.append(result.strip())

    for i, line in enumerate(lines):
        print(line, end='')
        if i < len(lines) - 1:
            print()
            print()
