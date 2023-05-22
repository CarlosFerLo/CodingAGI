from base import BaseNode, Type
from file import File

import os

class Dir(BaseNode):
    type: Type.DIR = Type.DIR # dir node
    parent: BaseNode # parent of node
    children: list[Type.FILE | Type.DIR] = [] # dir node has children
    
    paht: str # path of dir
    name: str # name of dir
    
    def __init__ (self, path: str, parent: BaseNode):
        """When creating a dir node, we need to pass the path of the dir.

        Args:
            path (str): path to the dir
        """
        self.path = path
        self.name = path.split("/")[-1]
        self.parent = parent
        
        for path in os.listdir(path):
            if os.path.isdir(path):
                self.children.append(Dir(path=path, parent=self))
            else:
                self.children.append(File(path=path, parent=self))