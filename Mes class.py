from abc import ABC

"""Class Abstrait"""
class Fichier(ABC):
    def __init__(self,image=None,video=None,audion=None,text=None,word=None,pdf=None):
        self.__image = image
        self.__video = video
        self.__audion = audion
        self.__text = text
        self.__word = word
        self.__pdf = pdf

        


       