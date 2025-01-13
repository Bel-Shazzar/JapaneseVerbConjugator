from .enumerated_types import *
from .exceptions import NonIrregularVerbError
from .irregular_verb_groups import KURU_KANJI


class NoConjugationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def create_conjugation_dict():
    return {
        base_form: {
            formality: {
                tense: {polarity: None for polarity in Polarity} for tense in Tense
            }
            for formality in Formality
        }
        for base_form in BaseForm
    }


# SURU
SURU_CONJUGATION = create_conjugation_dict()

SURU_CONJUGATION[BaseForm.PLAIN][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "する"
SURU_CONJUGATION[BaseForm.PLAIN][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しない"
SURU_CONJUGATION[BaseForm.PLAIN][Formality.PLAIN][Tense.PAST][
    Polarity.POSITIVE
] = "した"
SURU_CONJUGATION[BaseForm.PLAIN][Formality.PLAIN][Tense.PAST][
    Polarity.NEGATIVE
] = "しなかった"
SURU_CONJUGATION[BaseForm.POLITE][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "します"
SURU_CONJUGATION[BaseForm.POLITE][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しません"
SURU_CONJUGATION[BaseForm.POLITE][Formality.POLITE][Tense.PAST][
    Polarity.POSITIVE
] = "しました"
SURU_CONJUGATION[BaseForm.POLITE][Formality.POLITE][Tense.PAST][
    Polarity.NEGATIVE
] = "しませんでした"

SURU_CONJUGATION[BaseForm.TE][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "して"
SURU_CONJUGATION[BaseForm.TE][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しなくて"
SURU_CONJUGATION[BaseForm.TE][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "しまして"
SURU_CONJUGATION[BaseForm.TE][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しませんでして"

SURU_CONJUGATION[BaseForm.TARI][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "したり"
SURU_CONJUGATION[BaseForm.TARI][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しなかったり"
SURU_CONJUGATION[BaseForm.TARI][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "しましたり"
SURU_CONJUGATION[BaseForm.TARI][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しませんでしたり"

SURU_CONJUGATION[BaseForm.CONDITIONAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "したら"
SURU_CONJUGATION[BaseForm.CONDITIONAL][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "しましたら"
SURU_CONJUGATION[BaseForm.CONDITIONAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しなかったら"
SURU_CONJUGATION[BaseForm.CONDITIONAL][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しませんでしたら"

SURU_CONJUGATION[BaseForm.VOLITIONAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "しよう"
SURU_CONJUGATION[BaseForm.VOLITIONAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しないだろう"
SURU_CONJUGATION[BaseForm.VOLITIONAL][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "しましょう"
SURU_CONJUGATION[BaseForm.VOLITIONAL][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しないでしょう"

SURU_CONJUGATION[BaseForm.POTENTIAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "できる"
SURU_CONJUGATION[BaseForm.POTENTIAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "できない"
SURU_CONJUGATION[BaseForm.POTENTIAL][Formality.PLAIN][Tense.PAST][
    Polarity.POSITIVE
] = "できた"
SURU_CONJUGATION[BaseForm.POTENTIAL][Formality.PLAIN][Tense.PAST][
    Polarity.NEGATIVE
] = "できなかった"
SURU_CONJUGATION[BaseForm.POTENTIAL][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "できます"
SURU_CONJUGATION[BaseForm.POTENTIAL][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "できません"
SURU_CONJUGATION[BaseForm.POTENTIAL][Formality.POLITE][Tense.PAST][
    Polarity.POSITIVE
] = "できました"
SURU_CONJUGATION[BaseForm.POTENTIAL][Formality.POLITE][Tense.PAST][
    Polarity.NEGATIVE
] = "できませんでした"

SURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "させる"
SURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "ささない"
SURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.PLAIN][Tense.PAST][
    Polarity.POSITIVE
] = "させた"
SURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.PLAIN][Tense.PAST][
    Polarity.NEGATIVE
] = "させなかった"
SURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "させます"
SURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "させません"
SURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.POLITE][Tense.PAST][
    Polarity.POSITIVE
] = "させました"
SURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.POLITE][Tense.PAST][
    Polarity.NEGATIVE
] = "させませんでした"

SURU_CONJUGATION[BaseForm.IMPERATIVE][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "しろ"
SURU_CONJUGATION[BaseForm.IMPERATIVE][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "するな"
SURU_CONJUGATION[BaseForm.IMPERATIVE][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "してください"
SURU_CONJUGATION[BaseForm.IMPERATIVE][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しないでください"

SURU_CONJUGATION[BaseForm.PROVISIONAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "すれば"
SURU_CONJUGATION[BaseForm.PROVISIONAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しなければ"
SURU_CONJUGATION[BaseForm.PROVISIONAL][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "しませば"
SURU_CONJUGATION[BaseForm.PROVISIONAL][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "しませんなら"

SURU_CONJUGATION[BaseForm.PASSIVE][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "される"
SURU_CONJUGATION[BaseForm.PASSIVE][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "されない"
SURU_CONJUGATION[BaseForm.PASSIVE][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "されます"
SURU_CONJUGATION[BaseForm.PASSIVE][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "されません"

KURU_CONJUGATION = create_conjugation_dict()

KURU_CONJUGATION[BaseForm.PLAIN][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "くる"
KURU_CONJUGATION[BaseForm.PLAIN][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こない"
KURU_CONJUGATION[BaseForm.PLAIN][Formality.PLAIN][Tense.PAST][
    Polarity.POSITIVE
] = "きた"
KURU_CONJUGATION[BaseForm.PLAIN][Formality.PLAIN][Tense.PAST][
    Polarity.NEGATIVE
] = "こなかった"

KURU_CONJUGATION[BaseForm.POLITE][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "きます"
KURU_CONJUGATION[BaseForm.POLITE][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "きません"
KURU_CONJUGATION[BaseForm.POLITE][Formality.POLITE][Tense.PAST][
    Polarity.POSITIVE
] = "きました"
KURU_CONJUGATION[BaseForm.POLITE][Formality.POLITE][Tense.PAST][
    Polarity.NEGATIVE
] = "きませんでした"

KURU_CONJUGATION[BaseForm.TE][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "きて"
KURU_CONJUGATION[BaseForm.TE][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こなくて"
KURU_CONJUGATION[BaseForm.TE][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "きまして"
KURU_CONJUGATION[BaseForm.TE][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "きませんでして"

KURU_CONJUGATION[BaseForm.TARI][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "きたり"
KURU_CONJUGATION[BaseForm.TARI][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こなかったり"
KURU_CONJUGATION[BaseForm.TARI][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "きましたり"
KURU_CONJUGATION[BaseForm.TARI][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "きませんでしたり"

KURU_CONJUGATION[BaseForm.CONDITIONAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "きたら"
KURU_CONJUGATION[BaseForm.CONDITIONAL][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "きましたら"
KURU_CONJUGATION[BaseForm.CONDITIONAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こなかったら"
KURU_CONJUGATION[BaseForm.CONDITIONAL][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "きませんでしたら"

KURU_CONJUGATION[BaseForm.VOLITIONAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "こよう"
KURU_CONJUGATION[BaseForm.VOLITIONAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こないだろう"
KURU_CONJUGATION[BaseForm.VOLITIONAL][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "きましょう"
KURU_CONJUGATION[BaseForm.VOLITIONAL][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こないでしょう"

KURU_CONJUGATION[BaseForm.POTENTIAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "こられる"
KURU_CONJUGATION[BaseForm.POTENTIAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こられない"
KURU_CONJUGATION[BaseForm.POTENTIAL][Formality.PLAIN][Tense.PAST][
    Polarity.POSITIVE
] = ""
KURU_CONJUGATION[BaseForm.POTENTIAL][Formality.PLAIN][Tense.PAST][
    Polarity.NEGATIVE
] = ""
KURU_CONJUGATION[BaseForm.POTENTIAL][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "こられます"
KURU_CONJUGATION[BaseForm.POTENTIAL][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こられません"
KURU_CONJUGATION[BaseForm.POTENTIAL][Formality.POLITE][Tense.PAST][
    Polarity.POSITIVE
] = ""
KURU_CONJUGATION[BaseForm.POTENTIAL][Formality.POLITE][Tense.PAST][
    Polarity.NEGATIVE
] = ""

KURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "こさせる"
KURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こさせない"
KURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.PLAIN][Tense.PAST][
    Polarity.POSITIVE
] = ""
KURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.PLAIN][Tense.PAST][
    Polarity.NEGATIVE
] = ""
KURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "こさせます"
KURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こさせません"
KURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.POLITE][Tense.PAST][
    Polarity.POSITIVE
] = ""
KURU_CONJUGATION[BaseForm.CAUSATIVE][Formality.POLITE][Tense.PAST][
    Polarity.NEGATIVE
] = ""

KURU_CONJUGATION[BaseForm.IMPERATIVE][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "こい"
KURU_CONJUGATION[BaseForm.IMPERATIVE][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "くるな"
KURU_CONJUGATION[BaseForm.IMPERATIVE][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "きてください"
KURU_CONJUGATION[BaseForm.IMPERATIVE][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こないでください"

KURU_CONJUGATION[BaseForm.PROVISIONAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "くれば"
KURU_CONJUGATION[BaseForm.PROVISIONAL][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こなければ"
KURU_CONJUGATION[BaseForm.PROVISIONAL][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "きませば"
KURU_CONJUGATION[BaseForm.PROVISIONAL][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "きませんなら"

KURU_CONJUGATION[BaseForm.PASSIVE][Formality.PLAIN][Tense.NONPAST][
    Polarity.POSITIVE
] = "こられる"
KURU_CONJUGATION[BaseForm.PASSIVE][Formality.PLAIN][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こられない"
KURU_CONJUGATION[BaseForm.PASSIVE][Formality.POLITE][Tense.NONPAST][
    Polarity.POSITIVE
] = "こられます"
KURU_CONJUGATION[BaseForm.PASSIVE][Formality.POLITE][Tense.NONPAST][
    Polarity.NEGATIVE
] = "こられません"


def get_suru_conjugation(
    base_form: BaseForm, formality: Formality, tense: Tense, polarity: Polarity
):
    conjugated_verb = SURU_CONJUGATION[base_form][formality][tense][polarity]
    if conjugated_verb is None:
        raise NoConjugationError(
            f"Suru cannot be conjugated with ({base_form.name}, {formality.name}, {tense}, {polarity.name})"
        )
    return conjugated_verb


def get_kuru_conjugation(
    base_form: BaseForm, formality: Formality, tense: Tense, polarity: Polarity
):
    conjugated_verb = KURU_CONJUGATION[base_form][formality][tense][polarity]
    if conjugated_verb is None:
        raise NoConjugationError(
            f"Kuru cannot be conjugated with ({base_form.name}, {formality.name}, {tense}, {polarity.name})"
        )
    return conjugated_verb


def get_irregular_conjugation(
    verb: str,
    base_form: BaseForm,
    formality: Formality = Formality.PLAIN,
    tense: Tense = Tense.NONPAST,
    polarity: Polarity = Polarity.POSITIVE,
):

    if verb == IrregularVerb.SURU.value:
        return get_suru_conjugation(base_form, formality, tense, polarity)
    elif verb == IrregularVerb.KURU.value:
        return get_kuru_conjugation(base_form, formality, tense, polarity)
    elif verb == IrregularVerb.KURU_KANJI.value:
        return (
            KURU_KANJI + get_kuru_conjugation(base_form, formality, tense, polarity)[1:]
        )
    else:
        raise NonIrregularVerbError("Non-Irregular Verb Ending Found", verb)
