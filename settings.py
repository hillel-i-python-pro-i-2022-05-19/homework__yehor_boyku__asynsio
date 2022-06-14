import string
from typing import Final

CHARACTERS: Final[str] = ''.join([
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.digits,
])
