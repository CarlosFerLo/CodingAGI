from base import BaseNode, Type

from enum import Enum
from typing import Union, Any
import json

class FileType(str, Enum):
    PYTHON = "py"
    TEXT = "txt"
    JSON = "json"
    ENV = "env"
    
JSON = dict[str, Any] # json file content
ENV = dict[str, str] # env file content
TEXT = str # text file content
    
Content = Union[JSON, ENV, TEXT] # content of file


class File(BaseNode):
    type: Type.FILE = Type.FILE # file node
    parent: BaseNode # parent of node
    children: list[BaseNode] = [] # file node has no children
    
    name: str # name of file
    path: str # path of file
    raw_content: str # content of file
    file_type: str # type of file
    
    content: Content = None # content of file (only for non-code files)
    
    def __init__ (self, path: str, parent: BaseNode):
        """When creating a file node, we need to pass the path of the file.

        Args:
            path (str): path to the file
        """
        self.path = path
        self.name = path.split("/")[-1]
        self.file_type = self.name.split(".")[-1]
        self.parent = parent
        
        with open(path, "r") as f: # read file content (only for text files no support for binary files)
            self.raw_content = f.read()
            
        self._parse_raw_content() # parse raw content to get children nodes or other information
    
    def _parse_raw_content(self) :
        """Parse raw content to get children nodes or other information
        """
        if self.file_type == FileType.PYTHON:
            self._parse_python_file()
        elif self.file_type == FileType.JSON:
            self._parse_json_file()
        elif self.file_type == FileType.ENV:
            self._parse_env_file()
        else:
            self._parse_text_file()
    
    def _parse_python_file(self): # TODO: implement
        pass 
    
    def _parse_json_file(self):    
        self.content = json.loads(self.raw_content)

    def _parse_env_file(self):
        self.content = dict()
        for line in self.raw_content.split("\n"):
            if line:
                key, value = line.split("=")
                self.content[key] = value
    
    def _parse_text_file(self):
        self.content = self.raw_content
        