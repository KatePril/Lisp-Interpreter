"""This module provides Node class for parsing"""

from dataclasses import dataclass, field
from typing import Union


@dataclass
class Node:
    """
    This class holds the parsed data
    """
    parent: Union['Node', None] = field(default=None)
    tokens: list[str] = field(default_factory=list)
    children: list['Node'] = field(default_factory=list)
