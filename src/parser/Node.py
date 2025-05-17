from dataclasses import dataclass, field
from typing import Union

@dataclass
class Node:
    parent: Union['Node', None] = field(default=None)
    tokens: list[set] = field(default_factory=list)
    childs: list['Node'] = field(default_factory=list)

