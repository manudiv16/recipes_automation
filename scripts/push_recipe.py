import os
import sys
import time
import logging
from read_and_folds import DocumentTag
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    i = 0

    def on_modified(self, event):
        for filename in os.listdir(foldr_to_observe):
            exist = self.__exist_file(filename)
            self.__naming_and_move(exist, filename)

    def __naming_and_move(self, exist, filename):
        src = foldr_to_observe + "/" + filename
        new_folder = foldr_destination + "/" + exist
        self.__move_file(src, new_folder)

    def __exist_file(self, filename):
        exist = os.path.isfile(foldr_destination+"/" + filename)
        if exist:
            self.i += 1
            return self.__exist_file(filename[:-3]+"("+str(self.i)+")"+filename[-3:])
        return filename

    def __move_file(self, src, new_folder):
        os.rename(src, new_folder)
        docu = DocumentTag()
        print(docu.tag_read(new_folder))


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
