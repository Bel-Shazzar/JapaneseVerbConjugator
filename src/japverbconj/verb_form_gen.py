from .constants.enumerated_types import (
    BaseForm,
    CopulaForm,
    Formality,
    Polarity,
    Tense,
    VerbClass,
)
from .constants.exceptions import UnsupportedBaseFormError, UnsupportedCopulaFormError
from .copula_gen import CopulaGenerator
from .decorators import validate_japanese_verb
from .negative_form_gen import NegativeVerbForms
from .positive_form_gen import PositiveVerbForms
from .utils import convert_args, convert_copula_args, handle_irregular_verb


def generate_japanese_verb_by_str(
    verb: str, verb_class: VerbClass, base_form_str: str, *args
):
    for base_form in BaseForm:
        if base_form_str.lower() == base_form.value:
            return generate_japanese_verb_form(
                verb, verb_class, base_form, **convert_args(base_form, *args)
            )
    raise UnsupportedBaseFormError(f"Unsupported BaseForm string {base_form_str}")


def generate_japanese_copula_by_str(copula_form_str: str, *args):
    for copula_form in CopulaForm:
        if copula_form_str.lower() == copula_form.value:
            return generate_japanese_copula_form(
                copula_form, **convert_copula_args(copula_form, *args)
            )
    raise UnsupportedCopulaFormError(f"Unsupported CopulaForm string {copula_form_str}")


def generate_japanese_verb_form(
    verb: str, verb_class: VerbClass, base_form: BaseForm, **kwargs
):
    if base_form == BaseForm.PLAIN:
        return JapaneseVerbFormGenerator.generate_plain_form(verb, verb_class, **kwargs)
    elif base_form == BaseForm.POLITE:
        return JapaneseVerbFormGenerator.generate_polite_form(
            verb, verb_class, **kwargs
        )
    elif base_form == BaseForm.TE:
        return JapaneseVerbFormGenerator.generate_te_form(verb, verb_class, **kwargs)
    elif base_form == BaseForm.TA:
        return JapaneseVerbFormGenerator.generate_ta_form(verb, verb_class, **kwargs)
    elif base_form == BaseForm.TARI:
        return JapaneseVerbFormGenerator.generate_tari_form(verb, verb_class, **kwargs)
    elif base_form == BaseForm.TARA:
        return JapaneseVerbFormGenerator.generate_tara_form(verb, verb_class, **kwargs)
    elif base_form == BaseForm.CONDITIONAL:
        return JapaneseVerbFormGenerator.generate_conditional_form(
            verb, verb_class, **kwargs
        )
    elif base_form == BaseForm.VOLITIONAL:
        return JapaneseVerbFormGenerator.generate_volitional_form(
            verb, verb_class, **kwargs
        )
    elif base_form == BaseForm.POTENTIAL:
        return JapaneseVerbFormGenerator.generate_potential_form(
            verb, verb_class, **kwargs
        )
    elif base_form == BaseForm.IMPERATIVE:
        return JapaneseVerbFormGenerator.generate_imperative_form(
            verb, verb_class, **kwargs
        )
    elif base_form == BaseForm.PROVISIONAL:
        return JapaneseVerbFormGenerator.generate_provisional_form(
            verb, verb_class, **kwargs
        )
    elif base_form == BaseForm.CAUSATIVE:
        return JapaneseVerbFormGenerator.generate_causative_form(
            verb, verb_class, **kwargs
        )
    elif base_form == BaseForm.PASSIVE:
        return JapaneseVerbFormGenerator.generate_passive_form(
            verb, verb_class, **kwargs
        )
    else:
        raise UnsupportedBaseFormError("This BaseForm is not supported.")


def generate_japanese_copula_form(copula_form: CopulaForm, **kwargs):
    if copula_form == CopulaForm.PLAIN:
        return JapaneseVerbFormGenerator.copula.generate_plain_form(**kwargs)
    elif copula_form == CopulaForm.POLITE:
        return JapaneseVerbFormGenerator.copula.generate_polite_form(**kwargs)
    elif copula_form == CopulaForm.CONDITIONAL:
        return JapaneseVerbFormGenerator.copula.generate_conditional_form(**kwargs)
    elif copula_form == CopulaForm.PRESUMPTIVE:
        return JapaneseVerbFormGenerator.copula.generate_presumptive_form(**kwargs)
    elif copula_form == CopulaForm.TE:
        return JapaneseVerbFormGenerator.copula.generate_te_form(**kwargs)
    elif copula_form == CopulaForm.TARA:
        return JapaneseVerbFormGenerator.copula.generate_tara_form(**kwargs)
    else:
        raise UnsupportedCopulaFormError("This CopulaForm is not supported.")


class JapaneseVerbFormGenerator:
    positive_verb_forms = PositiveVerbForms
    negative_verb_forms = NegativeVerbForms
    copula = CopulaGenerator

    @classmethod
    @validate_japanese_verb
    def generate_plain_form(cls, verb, verb_class, tense, polarity):
        """Generate the plain form of the verb depending on the tense and
        polarity.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb
            polarity (enum): Polarity Enum representing the polarity for the
                conjugated verb

        Returns:
            str: plain form of the verb based on the tense and polarity
        parameters
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb,
                BaseForm.PLAIN,
                formality=Formality.PLAIN,
                tense=tense,
                polarity=polarity,
            )
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_plain_form(verb, verb_class, tense)
        return cls.negative_verb_forms.generate_plain_form(verb, verb_class, tense)

    @classmethod
    @validate_japanese_verb
    def generate_polite_form(cls, verb, verb_class, tense, polarity):
        """Generate the polite form of the verb depending on the tense and
        polarity.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb
            polarity (enum): Polarity Enum representing the polarity for the
                conjugated verb

        Returns:
            str: polite form of the verb based on the tense and polarity
        parameters
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb,
                BaseForm.POLITE,
                formality=Formality.POLITE,
                tense=tense,
                polarity=polarity,
            )
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_polite_form(verb, verb_class, tense)
        return cls.negative_verb_forms.generate_polite_form(verb, verb_class, tense)

    @classmethod
    @validate_japanese_verb
    def generate_te_form(cls, verb, verb_class, formality, polarity):
        """Utilize base_te_ta_form function to generate the -te form
        of the verb

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs

        Returns:
            str: -te form of the verb
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb, BaseForm.TE, formality=formality, polarity=polarity
            )
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_te_form(verb, verb_class, formality)
        return cls.negative_verb_forms.generate_te_form(verb, verb_class, formality)

    @classmethod
    @validate_japanese_verb
    def generate_ta_form(cls, verb, verb_class, formality, polarity):
        """Convenience method for the past forms

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb
            polarity (enum): Polarity Enum representing the polarity for the
                conjugated verb

        Returns:
            str: -ta form of the verb
        """
        if formality == Formality.PLAIN:
            return cls.generate_plain_form(verb, verb_class, Tense.PAST, polarity)
        else:
            return cls.generate_polite_form(verb, verb_class, Tense.PAST, polarity)

    @classmethod
    @validate_japanese_verb
    def generate_tari_form(cls, verb, verb_class, formality, polarity):
        """Utilize base_te_ta_form function to generate the -tari form
        of the verb

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb
            polarity (enum): Polarity Enum representing the polarity for the
                conjugated verb

        Returns:
            str: -tari form of the verb
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb, BaseForm.TARI, formality=formality, polarity=polarity
            )
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_tari_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_tari_form(verb, verb_class, formality)

    @classmethod
    @validate_japanese_verb
    def generate_tara_form(cls, verb, verb_class, formality, polarity):
        """Utilize base_te_ta_form function to generate the -tara form
        of the verb

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb
            polarity (enum): Polarity Enum representing the polarity for the
                conjugated verb

        Returns:
            str: -tara form of the verb
        """
        return cls.generate_conditional_form(verb, verb_class, formality, polarity)

    @classmethod
    @validate_japanese_verb
    def generate_conditional_form(
        cls, verb, verb_class: VerbClass, formality: Formality, polarity: Polarity
    ):
        """Generate the conditional form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb
            polarity (enum): Polarity Enum representing the polarity for the
                conjugated verb

        Returns:
            str: conditional form of the verb based on the formality and polarity
        parameters
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb, BaseForm.CONDITIONAL, formality=formality, polarity=polarity
            )
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_conditional_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_conditional_form(
            verb, verb_class, formality
        )

    @classmethod
    @validate_japanese_verb
    def generate_volitional_form(cls, verb, verb_class, formality, polarity):
        """Generate the volitional form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb
            polarity (enum): Polarity Enum representing the polarity for the
                conjugated verb

        Returns:
            str: volitional form of the verb based on the formality and polarity
        parameters
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb, BaseForm.VOLITIONAL, formality=formality, polarity=polarity
            )
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_volitional_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_volitional_form(
            verb, verb_class, formality
        )

    @classmethod
    @validate_japanese_verb
    def generate_potential_form(cls, verb, verb_class, formality, polarity):
        """Generate the potential form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb
            polarity (enum): Polarity Enum representing the polarity for the
                conjugated verb

        Returns:
            str: potential form of the verb based on the formality and polarity
        parameters
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb, BaseForm.POTENTIAL, formality=formality, polarity=polarity
            )
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_potential_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_potential_form(
            verb, verb_class, formality
        )

    @classmethod
    @validate_japanese_verb
    def generate_imperative_form(cls, verb, verb_class, formality, polarity):
        """Generate the imperative form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb
            polarity (enum): Polarity Enum representing the polarity for the
                conjugated verb

        Returns:
            str: imperative form of the verb based on the formality and polarity
        parameters
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb, BaseForm.IMPERATIVE, formality=formality, polarity=polarity
            )
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_imperative_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_imperative_form(
            verb, verb_class, formality
        )

    @classmethod
    @validate_japanese_verb
    def generate_provisional_form(cls, verb, verb_class, formality, polarity):
        """Generate the provisional form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb
            polarity (enum): Polarity Enum representing the polarity for the
                conjugated verb

        Returns:
            str: provisional form of the verb based on the formality and polarity
        parameters
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb, BaseForm.PROVISIONAL, formality=formality, polarity=polarity
            )
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_provisional_form(verb, verb_class)
        return cls.negative_verb_forms.generate_provisional_form(
            verb, verb_class, formality
        )

    @classmethod
    @validate_japanese_verb
    def generate_causative_form(cls, verb, verb_class, formality, polarity):
        """Generate the causative form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb
            polarity (enum): Polarity Enum representing the polarity for the
                conjugated verb

        Returns:
            str: causative form of the verb based on the formality and polarity
        parameters
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb, BaseForm.CAUSATIVE, formality=formality, polarity=polarity
            )
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_causative_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_causative_form(
            verb, verb_class, formality
        )

    @classmethod
    @validate_japanese_verb
    def generate_passive_form(cls, verb, verb_class, formality, polarity):
        """Generate the passive form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb
            polarity (enum): Polarity Enum representing the polarity for the
                conjugated verb

        Returns:
            str: passive form of the verb based on the formality and polarity
        parameters
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb, BaseForm.PASSIVE, formality=formality, polarity=polarity
            )
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_passive_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_passive_form(
            verb, verb_class, formality
        )
