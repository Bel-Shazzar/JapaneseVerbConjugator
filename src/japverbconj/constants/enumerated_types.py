from enum import Enum, auto


class BaseForm(Enum):
    PLAIN = "pla"
    POLITE = "pol"
    TE = "te"
    TA = "ta"
    TARA = "tara"
    TARI = "tari"
    CONDITIONAL = "cond"
    VOLITIONAL = "vol"
    POTENTIAL = "pot"
    IMPERATIVE = "imp"
    PROVISIONAL = "prov"
    CAUSATIVE = "caus"
    PASSIVE = "pass"


class CopulaForm(Enum):
    PLAIN = BaseForm.PLAIN.value
    POLITE = BaseForm.POLITE.value
    TE = BaseForm.TE.value
    CONDITIONAL = BaseForm.CONDITIONAL.value
    TARA = BaseForm.TARA.value
    PRESUMPTIVE = "pres"


class Formality(Enum):
    PLAIN = BaseForm.PLAIN.value
    POLITE = BaseForm.POLITE.value


class Polarity(Enum):
    POSITIVE = "pos"
    NEGATIVE = "neg"


class Tense(Enum):
    NONPAST = "nonpast"
    PAST = "past"


class VerbClass(Enum):
    GODAN = auto()
    ICHIDAN = auto()
    IRREGULAR = auto()


class IrregularVerb(Enum):
    SURU = "する"
    KURU = "くる"
    KURU_KANJI = "来る"


class ArgumentType(Enum):
    FORMALITY = Formality
    TENSE = Tense
    POLARITY = Polarity


if __name__ == "__main__":
    for element in CopulaForm:
        print(element.name, element.value)
