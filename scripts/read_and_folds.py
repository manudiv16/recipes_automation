#!/usr/bin/env python3
import os
import re
import typing

class DocumentTag():

    def __searchtag(self, text: str) -> str :
        pattern = re.compile(r'tags: `(\w*)`')
        matches = pattern.findall(text)
        return matches[-1] if len(matches) > 0 else str(None)

    def tag_read(self, src:str=None, text:str=None) -> str:
        if text != None:
            return self.__searchtag(text)
        file_exist = os.path.isfile(src)
        if file_exist:
            with open(src, 'r') as file:
                return self.__searchtag(file.read())
        return "None"
