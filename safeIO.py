"""
Safely write to files in Python even from multiple threads

© Anime no Sekai — 2020
"""

from time import sleep
from os.path import isfile
from json import load, dump
from threading import Thread, Lock

class TextFile():
    """
    A Text File object
    """
    def __init__(self, filepath, encoding="utf-8", blocking=True) -> None:
        self.filepath = str(filepath)
        self.encoding = str(encoding)
        self.blocking = blocking
        self._currentOperation = 1
        self._queueLength = 0
        self._Lock = Lock()
        
    def __repr__(self) -> str:
        return self.filepath

    def name(self, callback=None):
        """
        Returns the file name
        """
        self._Lock.acquire()
        def _name(callback=None):
            """
            Internal name() function
            """
            operationID = self._queueLength = self._queueLength + 1
            while operationID != self._queueLength:
                sleep(0.001)
            with open(self.filepath, "r", encoding=self.encoding) as readingFile:
                data = readingFile.name
            self._currentOperation += 1
            self._Lock.release()
            if callback is None:
                return data
            else:
                callback(data)

        if self.blocking:
            return _name()
        else:
            newThread = Thread(target=_name, args=[callback])
            newThread.daemon = True
            newThread.start()
            

    def read(self, position=0, callback=None):
        """
        Reads the entire file and returns its content
        """
        self._Lock.acquire()
        def _read(position=0, callback=None):
            operationID = self._queueLength = self._queueLength + 1
            while operationID != self._queueLength:
                sleep(0.001)
            with open(self.filepath, "r", encoding=self.encoding) as readingFile:
                readingFile.seek(int(position))
                data = readingFile.read()
            self._currentOperation += 1
            self._Lock.release()
            if callback is None:
                return data
            else:
                callback(data)
        
        if self.blocking:
            return _read(position)
        else:
            newThread = Thread(target=_read, args=[position, callback])
            newThread.daemon = True
            newThread.start()

    def write(self, data, position=0, callback=None):
        """
        Writes (or overwrites) to the file and returns the number of characters written
        """
        self._Lock.acquire()
        def _write(data, position=0, callback=None):
            operationID = self._queueLength = self._queueLength + 1
            while operationID != self._queueLength:
                sleep(0.001)
            with open(self.filepath, "w", encoding=self.encoding) as writingFile:
                writingFile.seek(int(position))
                data = writingFile.write(str(data))
            self._currentOperation += 1
            self._Lock.release()
            if callback is None:
                return data
            else:
                callback(data)
                
        if self.blocking:
            return _write(data, position)
        else:
            newThread = Thread(target=_write, args=[data, position, callback])
            newThread.daemon = True
            newThread.start()


    def append(self, data, callback=None):
        """
        Appends to the file and returns the number of characters written
        """
        self._Lock.acquire()
        def _append(data, callback=None):
            operationID = self._queueLength = self._queueLength + 1
            while operationID != self._queueLength:
                sleep(0.001)
            with open(self.filepath, "a", encoding=self.encoding) as writingFile:
                data = writingFile.write(str(data))
            self._currentOperation += 1
            self._Lock.release()
            if callback is None:
                return data
            else:
                callback(data)
                        
        if self.blocking:
            return _append(data)
        else:
            newThread = Thread(target=_append, args=[data, callback])
            newThread.daemon = True
            newThread.start()

    def readline(self, position=0, callback=None):
        """
        Returns the line of the current position (from the position to the linebreak)
        """
        self._Lock.acquire()
        def _readline(position=0, callback=None):
            operationID = self._queueLength = self._queueLength + 1
            while operationID != self._queueLength:
                sleep(0.001)
            with open(self.filepath, "r", encoding=self.encoding) as readingFile:
                readingFile.seek(int(position))
                data = readingFile.readline()
            self._currentOperation += 1
            self._Lock.release()
            if callback is None:
                return data
            else:
                callback(data)
        
        if self.blocking:
            return _readline(position)
        else:
            newThread = Thread(target=_readline, args=[position, callback])
            newThread.daemon = True
            newThread.start()

    def readlines(self, position=0, callback=None):
        """
        Reads the whole file and returns the lines (separated by a line break)
        """
        self._Lock.acquire()
        def _readlines(position=0, callback=None):
            operationID = self._queueLength = self._queueLength + 1
            while operationID != self._queueLength:
                sleep(0.001)
            with open(self.filepath, "r", encoding=self.encoding) as readingFile:
                readingFile.seek(position)
                data = readingFile.readlines()
            self._currentOperation += 1
            self._Lock.release()
            if callback is None:
                return data
            else:
                callback(data)
                
        if self.blocking:
            return _readlines(position)
        else:
            newThread = Thread(target=_readlines, args=[position, callback])
            newThread.daemon = True
            newThread.start()

    def fileno(self, callback=None):
        """
        Returns the file descriptor (int) used by Python to request I/O operations from the operating system.
        """
        self._Lock.acquire()
        def _fileno(callback=None):
            operationID = self._queueLength = self._queueLength + 1
            while operationID != self._queueLength:
                sleep(0.001)
            with open(self.filepath, "r", encoding=self.encoding) as readingFile:
                data = readingFile.fileno()
            self._currentOperation += 1
            self._Lock.release()
            if callback is None:
                return data
            else:
                callback(data)
                
        if self.blocking:
            return _fileno()
        else:
            newThread = Thread(target=_fileno, args=[callback])
            newThread.daemon = True
            newThread.start()


    def writelines(self, data, position=0, callback=None):
        """
        Writes (or overwrites) the given list of lines to the file
        """
        self._Lock.acquire()
        def _writelines(data, position=0, callback=None):
            operationID = self._queueLength = self._queueLength + 1
            while operationID != self._queueLength:
                sleep(0.001)
            with open(self.filepath, "w", encoding=self.encoding) as writingFile:
                writingFile.seek(position)
                writingFile.writelines((data.split("\n") if isinstance(data, str) else list(data)))
            self._currentOperation += 1
            self._Lock.release()
            if callback is None:
                return
            else:
                callback()

        if self.blocking:
            return _writelines(data, position)
        else:
            newThread = Thread(target=_writelines, args=[data, position, callback])
            newThread.daemon = True
            newThread.start()

    def appendlines(self, data, callback=None):
        """
        Appends the given list of lines to the file
        """
        self._Lock.acquire()
        def _appendlines(data, callback=None):
            operationID = self._queueLength = self._queueLength + 1
            while operationID != self._queueLength:
                sleep(0.001)
            with open(self.filepath, "a", encoding=self.encoding) as writingFile:
                writingFile.writelines((data.split("\n") if isinstance(data, str) else list(data)))
            self._currentOperation += 1
            self._Lock.release()
            if callback is None:
                return
            else:
                callback()
                
        if self.blocking:
            return _appendlines(data)
        else:
            newThread = Thread(target=_appendlines, args=[data, callback])
            newThread.daemon = True
            newThread.start()

    def detach(self, mode="r", callback=None):
        """
        Returns the opened IO (TextIOWrapper)

        Warning: Make sure to close the file correctly after using the file
        """
        self._Lock.acquire()
        def _detach(mode="r", callback=None):
            operationID = self._queueLength = self._queueLength + 1
            while operationID != self._queueLength:
                sleep(0.001)
            fileIO = open(self.filepath, mode, encoding=self.encoding)
            self._currentOperation += 1
            self._Lock.release()
            if callback is None:
                return fileIO
            else:
                callback(fileIO)

        if self.blocking:
            return _detach(mode)
        else:
            newThread = Thread(target=_detach, args=[mode, callback])
            newThread.daemon = True
            newThread.start()

class BinaryFile():
    pass
    

class JSONFile():
    pass
    