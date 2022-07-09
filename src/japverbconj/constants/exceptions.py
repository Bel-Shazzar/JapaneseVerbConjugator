class InvalidJapaneseVerbLengthError(Exception):
    pass


class InvalidJapaneseVerbEndingError(Exception):
    pass


class NonJapaneseCharacterError(Exception):
    pass


class NonIrregularVerbError(Exception):
    pass


class UnsupportedBaseFormError(Exception):
    pass


class UnsupportedCopulaFormError(Exception):
    pass
