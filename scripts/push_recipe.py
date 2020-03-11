import os
import sys
import time
import logging
import typing
from read_and_folds import DocumentTag
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):

    def __move_file(self, src: str, new_folder: str) -> None:
        os.rename(src, new_folder)
        docu = DocumentTag()
        print(docu.tag_read(new_folder))

    def __genertor_filename(self):
        for filename in os.listdir(foldr_to_observe):
            yield filename
        yield None

    def run(self,file_generator):
        filename = next(file_generator)
        if filename != None: 
            exist = self.__exist_file(filename)
            self.__naming_and_move(exist, filename, self.__move_file)
            self.run(file_generator)
        else:
            pass            

    def on_modified(self, event) -> None:
        self.run(self.__genertor_filename())

    def __naming_and_move(self, exist, filename: str, foo) -> None:
        src = foldr_to_observe + "/" + filename
        new_folder = foldr_destination + "/" + exist
        foo(src, new_folder)

    def __exist_file(self, filename: str, i: int = 0) -> str:
        exist = os.path.isfile(foldr_destination+"/" + filename)
        if exist:
            i += 1
            return self.__exist_file(filename[:-3]+"("+str(i)+")"+filename[-3:], i)
        return filename


if __name__ == "__main__":
    event_heandler = MyHandler()
    observer = Observer()
    foldr_to_observe = "../drop"
    foldr_destination = "../docs"
    observer.schedule(event_heandler, foldr_to_observe, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
