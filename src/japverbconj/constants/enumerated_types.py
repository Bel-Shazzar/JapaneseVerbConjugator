from enum import Enum, auto


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


class CopulaForm(Enum):
    PLAIN = BaseForm.PLAIN.value
    POLITE = BaseForm.POLITE.value
    TE = BaseForm.TE.value
    CONDITIONAL = BaseForm.CONDITIONAL.value
    TARA = auto()
    PRESUMPTIVE = auto()


class Formality(Enum):
    PLAIN = BaseForm.PLAIN.value
    POLITE = BaseForm.POLITE.value


class Polarity(Enum):
    POSITIVE = auto()
    NEGATIVE = auto()


class Tense(Enum):
    PAST = auto()
    NONPAST = auto()


class VerbClass(Enum):
    GODAN = auto()
    ICHIDAN = auto()
    IRREGULAR = auto()


class IrregularVerb(Enum):
    SURU = "する"
    KURU = "くる"
    KURU_KANJI = "来る"


if __name__ == "__main__":
    for element in CopulaForm:
        print(element.name, element.value)
