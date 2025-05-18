from dataclasses import dataclass, field
from typing import Union

@dataclass
class Node:
    parent: Union['Node', None] = field(default=None)
    tokens: list[str] = field(default_factory=list)
    children: list['Node'] = field(default_factory=list)
