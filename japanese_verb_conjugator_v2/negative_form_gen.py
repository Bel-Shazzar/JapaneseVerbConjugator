from .constants.enumerated_types import Formality, Tense, VerbClass
from .constants.irregular_verb_groups import *
from .constants.particle_constants import *
from .constants.verb_ending_constants import *
from .utils import (
    generate_negative_stem,
    get_verb_stem,
    map_dictionary_to_a_ending,
    map_dictionary_to_e_ending,
    map_dictionary_to_i_ending,
)


# ---------------------------------------------------------- #
#                       Negative Verb Forms                  #
# ---------------------------------------------------------- #
class NegativeVerbForms:
    @classmethod
    def generate_plain_form(cls, verb: str, verb_class: VerbClass, tense: Tense):
        """Generate the negative plain form of the verb depending
        on the tense.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb

        Returns:
            str: negative plain form of the verb based on the tense
        parameter
        """
        negative_stem = generate_negative_stem(verb, verb_class)
        if tense == Tense.NONPAST:
            return f"{negative_stem}{NAI_ENDING}"
        else:
            return f"{negative_stem}{NAKATTA_ENDING}"

    @classmethod
    def generate_polite_form(cls, verb: str, verb_class: VerbClass, tense: Tense):
        """Generate the negative polite form of the verb depending
        on the tense.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb

        Returns:
            str: negative polite form of the verb based on the tense
        parameter
        """
        if tense == Tense.NONPAST:
            ending = MASU_NEGATIVE_NONPAST
        else:
            ending = MASU_NEGATIVE_PAST
        if verb_class == VerbClass.GODAN:
            if verb in NASARU_GROUP:
                verb_stem = f"{get_verb_stem(verb, verb_class)}{I_PARTICLE}"
            else:
                verb_stem = map_dictionary_to_i_ending(verb)
        else:
            verb_stem = get_verb_stem(verb, verb_class)
        return f"{verb_stem}{ending}"

    @classmethod
    def generate_te_form(cls, verb: str, verb_class: VerbClass, formality: Formality):
        """Generate the negative te form of the verb.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality for the conjugated verb

        Returns:
            str: negative te form of the verb
        parameter
        """
        if formality == Formality.PLAIN:
            return f"{generate_negative_stem(verb,verb_class)}{TE_FORM_PLAIN_NEGATIVE_ENDING}"
        else:
            return (
                cls.generate_polite_form(verb, verb_class, Tense.PAST)[:-1]
                + TE_PARTICLE
            )

    @classmethod
    def generate_tari_form(cls, verb: str, verb_class: VerbClass, formality: Formality):
        """Generate the negative tari form of the verb.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality for the conjugated verb

        Returns:
            str: negative tari form of the verb
        parameter
        """
        if formality == Formality.PLAIN:
            return f"{generate_negative_stem(verb, verb_class)}{TARI_FORM_PLAIN_NEGATIVE_ENDING}"
        else:
            return cls.generate_polite_form(verb, verb_class, Tense.PAST) + RI_PARTICLE

    @classmethod
    def generate_conditional_form(
        cls, verb: str, verb_class: VerbClass, formality: Formality
    ):
        """Generate the negative conditional form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative conditional form of the verb based on the formality
        parameter
        """
        if formality == Formality.PLAIN:
            verb = cls.generate_plain_form(verb, verb_class, Tense.PAST)
        else:
            verb = cls.generate_polite_form(verb, verb_class, Tense.PAST)
        return f"{verb}{RA_PARTICLE}"

    @classmethod
    def generate_volitional_form(
        cls, verb: str, verb_class: VerbClass, formality: Formality
    ):
        """Generate the negative volitional form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative volitional form of the verb based on the formality
        parameter
        """
        negative_stem = generate_negative_stem(verb, verb_class)
        if formality == Formality.PLAIN:
            return f"{negative_stem}{NAI_ENDING}{VOLITIONAL_PLAIN_COPULA}"
        else:
            return f"{negative_stem}{NAI_ENDING}{VOLITIONAL_POLITE_COPULA}"

    @classmethod
    def generate_potential_form(
        cls, verb: str, verb_class: VerbClass, formality: Formality
    ):
        """Generate the negative potential form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative potential form of the verb based on the formality
        parameter
        """
        if verb_class == VerbClass.GODAN:
            verb_stem = map_dictionary_to_e_ending(verb)
        else:
            verb_stem = f"{get_verb_stem(verb, verb_class)}{RA_PARTICLE}{RE_PARTICLE}"
        if formality == Formality.PLAIN:
            return f"{verb_stem}{NAI_ENDING}"
        else:
            return f"{verb_stem}{MASU_NEGATIVE_NONPAST}"

    @classmethod
    def generate_imperative_form(
        cls, verb: str, verb_class: VerbClass, formality: Formality
    ):
        """Generate the negative imperative form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative imperative form of the verb based on the formality
        parameter
        """
        if formality == Formality.PLAIN:
            return f"{verb}{NA_PARTICLE}"
        else:
            negative_stem = generate_negative_stem(verb, verb_class)
            return f"{negative_stem}{NAI_ENDING}{DE_PARTICLE}{KUDASAI}"

    @classmethod
    def generate_provisional_form(
        cls, verb: str, verb_class: VerbClass, formality: Formality
    ):
        """Generate the negative provisional form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative provisional form of the verb based on the formality
        parameter
        """
        negative_stem = generate_negative_stem(verb, verb_class)
        return f"{negative_stem}{PROVISIONAL_ICHIDAN_PLAIN_NEGATIVE_ENDING}"

    @classmethod
    def generate_causative_form(
        cls, verb: str, verb_class: VerbClass, formality: Formality
    ):
        """Generate the negative causative form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative causative form of the verb based on the formality
        parameter
        """
        if verb_class == VerbClass.GODAN:
            verb_stem = f"{map_dictionary_to_a_ending(verb)}{SE_PARTICLE}"
        else:
            verb_stem = f"{get_verb_stem(verb, verb_class)}{SA_PARTICLE}{SE_PARTICLE}"
        if formality == Formality.PLAIN:
            return f"{verb_stem}{NAI_ENDING}"
        else:
            return f"{verb_stem}{MASU_NEGATIVE_NONPAST}"

    @classmethod
    def generate_passive_form(
        cls, verb: str, verb_class: VerbClass, formality: Formality
    ):
        """Generate the negative passive form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative passive form of the verb based on the formality
        parameter
        """
        if verb_class == VerbClass.GODAN:
            verb_stem = f"{map_dictionary_to_a_ending(verb)}{RE_PARTICLE}"
        else:
            verb_stem = f"{get_verb_stem(verb, verb_class)}{RA_PARTICLE}{RE_PARTICLE}"
        if formality == Formality.PLAIN:
            return f"{verb_stem}{NAI_ENDING}"
        else:
            return f"{verb_stem}{MASU_NEGATIVE_NONPAST}"
