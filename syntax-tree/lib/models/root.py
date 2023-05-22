from base import BaseNode, Type
from file import File
from dir import Dir

import os

class Root(BaseNode):
    type: Type.ROOT = Type.ROOT # root node
    children: list[BaseNode] = [] 
    parent: BaseNode = None # root node has no parent

    def __init__(self, path: str):
        """When creating a root node, we need to pass the path of the root directory of the tree.

        Args:
            path (str): path to the root directory of the tree
        """
        
        if os.path.isdir(path) :
            self.children.append(File(path=path, parent=self))
        else :
            self.children.append(Dir(path=path, parent=self))     
        
