#!/usr/bin/python3
"""Module to create a function to print square"""


def text_indentation(text):
    """
    Method that indent a text by adding two newlines after those
    specific characters: '.', '?' and ':'
    :param text: str - the given text to properly indent
    :raises TypeError: if str is not a string
    :Returns: None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
        
    to_print = result.rstrip()
    print("{}".format(to_print))
