from enum import Enum, auto


class Formality(Enum):
    PLAIN = 1
    POLITE = 2


class Polarity(Enum):
    POSITIVE = 1
    NEGATIVE = 2


class Tense(Enum):
    PAST = 1
    NONPAST = 2


class VerbClass(Enum):
    GODAN = 1
    ICHIDAN = 2
    IRREGULAR = 3
    NONIRREGULAR = 4


class BaseForm(Enum):
    PLAIN = auto()
    POLITE = auto()
    TE = auto()
    CONDITIONAL = auto()
    VOLITIONAL = auto()
    POTENTIAL = auto()
    IMPERATIVE = auto()
    PROVISIONAL = auto()
    CAUSATIVE = auto()
    PASSIVE = auto()


class IrregularVerb(Enum):
    SURU = "する"
    KURU = "くる"
    KURU_KANJI = "来る"
