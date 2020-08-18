# !/usr/bin/python
# coding=utf-8
import re
from compress import symbols

def decompress(compressed_content):

    compressed_content = compressed_content.replace(symbols["implementation"], "implementation")
    compressed_content = compressed_content.replace(symbols["practicality"], "practicality")
    compressed_content = compressed_content.replace(symbols["better"], "better")
    compressed_content = compressed_content.replace(symbols["than"], "than")
    compressed_content = compressed_content.replace(symbols["Although"], "Although")

    print(compressed_content)
    return compressed_content
    