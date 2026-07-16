import secrets
import math
from typing import List, Optional
from .constants import (
    LOWERCASE, UPPERCASE, DIGITS, SPECIAL,
    UNAMBIGUOUS_LOWERCASE, UNAMBIGUOUS_UPPERCASE,
    UNAMBIGUOUS_DIGITS, UNAMBIGUOUS_SPECIAL, WORD_LIST
)


class PasswordGenerator:
    def __init__(
        self,
        length: int = 16,
        use_lower: bool = True,
        use_upper: bool = True,
        use_digits: bool = True,
        use_special: bool = True,
        ambiguous: bool = True,
    ):
        self.length = length
        self.use_lower = use_lower
        self.use_upper = use_upper
        self.use_digits = use_digits
        self.use_special = use_special
        self.ambiguous = ambiguous

    def _char_pool(self) -> str:
        pool = ""
        if self.use_lower:
            pool += LOWERCASE if self.ambiguous else UNAMBIGUOUS_LOWERCASE
        if self.use_upper:
            pool += UPPERCASE if self.ambiguous else UNAMBIGUOUS_UPPERCASE
        if self.use_digits:
            pool += DIGITS if self.ambiguous else UNAMBIGUOUS_DIGITS
        if self.use_special:
            pool += SPECIAL if self.ambiguous else UNAMBIGUOUS_SPECIAL
        if not pool:
            raise ValueError("Не выбран ни один набор символов")
        return pool

    def generate(self) -> str:
        pool = self._char_pool()
        return ''.join(secrets.choice(pool) for _ in range(self.length))

    def generate_phrase(
        self,
        words: int = 4,
        separator: str = "-",
        add_digits: bool = True,
        digit_count: int = 2,
        capitalize: bool = True,
    ) -> str:
        if words < 1:
            raise ValueError("Количество слов должно быть >= 1")
        selected = [secrets.choice(WORD_LIST) for _ in range(words)]
        if capitalize:
            selected = [w.capitalize() for w in selected]
        phrase = separator.join(selected)
        if add_digits and digit_count > 0:
            digits = ''.join(secrets.choice(DIGITS) for _ in range(digit_count))
            phrase = f"{phrase}{separator}{digits}"
        return phrase

    def entropy(self, password: str) -> float:
        pool_size = len(set(password))
        return len(password) * math.log2(pool_size) if pool_size > 0 else 0.0

    @staticmethod
    def strength_label(entropy: float) -> str:
        if entropy < 28:
            return "Очень слабый"
        elif entropy < 36:
            return "Слабый"
        elif entropy < 60:
            return "Хороший"
        elif entropy < 80:
            return "Сильный"
        else:
            return "Очень сильный"
