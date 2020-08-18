# !/usr/bin/python
# coding=utf-8
import re

symbols = {
    #   key             :   symbols[key]
    "implementation":   "🤯",
    "practicality":   '🤩',
    "better":   '😅',
    "than":   '😘',
    "Although":   "🥺",
}


def compress(content):

    compressed_content = ''
    content = content.replace("implementation", symbols["implementation"])
    content = content.replace("practicality", symbols["practicality"])
    content = content.replace("better", symbols["better"])
    content = content.replace("than", symbols["than"])
    content = content.replace("Although", symbols["Although"])

    

    return content
