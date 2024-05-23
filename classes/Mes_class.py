import os
import shutil
from abc import ABC, abstractmethod

class FileOrganizer(ABC):
    @abstractmethod
    def organiser(self, dossierFile):
        pass
