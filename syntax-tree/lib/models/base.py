from pydantic import BaseModel
from enum import Enum

class Type(str, Enum):
    ROOT = "root"
    FILE = "file"
    DIR = "dir"
    

class BaseNode(BaseModel):
    type: Type   # type of node
    children: list[BaseModel] = []  # children of node
    parent: BaseModel   # parent of node

    