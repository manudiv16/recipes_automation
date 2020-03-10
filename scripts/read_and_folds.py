#!/usr/bin/env python3
import os
import re


class DocumentTag():

    def __searchtag(self, text):
        pattern = re.compile(r'tags: `(\w*)`')
        matches = pattern.findall(text)
        return matches[-1] if len(matches) > 0 else None

    def tag_read(self, src=None, text=None):
        if text != None:
            return self.__searchtag(text)
        file_exist = os.path.isfile(src)
        if file_exist:
            with open(src, 'r') as file:
                return self.__searchtag(file.read())
        print("no hay fichero")
        pass
