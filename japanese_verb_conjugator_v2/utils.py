from .constants.enumerated_types import *
from .constants.irregular_verb_forms import get_irregular_conjugation
from .constants.irregular_verb_groups import *
from .constants.particle_constants import *
from .constants.verb_ending_constants import *


# ---------------------------------------------------------- #
#                UTIL VERB GENERATOR FUNCTIONS               #
# ---------------------------------------------------------- #
def splice_verb(verb, verb_class):
    """Split Japanese verb between stem and ending particle(s). The number of ending
    particles returned depends on the verb class (i.e. godan / ichidan will return one
    particle while irregular verbs will return two particles)

    Args:
        verb (str): Japanese verb in kanji and/or kana
        verb_class (enum): VerbClass enum representing the Japanese verb class

    Returns:
        tuple: Verb stem and particle ending
    """
    num_ending_particles = 1
    if verb_class == VerbClass.IRREGULAR:
        num_ending_particles = 2
    return verb[: -1 * num_ending_particles], verb[-1 * num_ending_particles :]


def get_verb_stem(verb, verb_class):
    """Split Japanese verb between stem and ending particle(s). The number of ending
    particles returned depends on the verb class (i.e. godan / ichidan will return one
    particle while irregular verbs will return two particles)

    Args:
        verb (str): Japanese verb in kanji and/or kana
        verb_class (enum): VerbClass enum representing the Japanese verb class

    Returns:
        str: Verb stem
    """
    return splice_verb(verb, verb_class)[0]


def get_ending_particle(verb, verb_class):
    """Split Japanese verb between stem and ending particle(s). The number of ending
    particles returned depends on the verb class (i.e. godan / ichidan will return one
    particle while irregular verbs will return two particles)

    Args:
        verb (str): Japanese verb in kanji and/or kana
        verb_class (enum): VerbClass enum representing the Japanese verb class

    Returns:
        tuple: Particle ending
    """
    return splice_verb(verb, verb_class)[1]


def handle_irregular_verb(
    verb: str,
    base_form: BaseForm,
    formality: Formality = Formality.PLAIN,
    tense: Tense = Tense.NONPAST,
    polarity: Polarity = Polarity.POSITIVE,
):
    """Handles irregular verb conjugations depending on suru or kuru verb type.
    Isolates logic of irregular verbs.

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        base_form (enum): BaseForm enum, representing which form is requested
        formality (enum, optional): Formality enum, determining the formality
        tense (enum, optional): Tense enum, determining the tense
        polarity (enum, optional): Polarity enum, determining the polarity

    Returns:
        str: irregular verb with appropriate particles and ending attached depending
            on verb conjugation
    """
    verb_stem, particle_ending = splice_verb(verb, VerbClass.IRREGULAR)
    ending = get_irregular_conjugation(
        particle_ending, base_form, formality, tense, polarity
    )
    return f"{verb_stem}{ending}"


def generate_negative_stem(verb, verb_class: VerbClass):
    """Generates the negative stem of a Japanese verb

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        verb_class (enum): VerbClass Enum representing the verb class
            to which the verb belongs

    Returns:
        str: negative stem of the verb
    """
    if verb == ARU:
        return ""
    if verb_class == VerbClass.GODAN:
        return map_dictionary_to_a_ending(verb)
    else:
        return get_verb_stem(verb, verb_class)


def base_te_ta_form(
    verb, verb_class: VerbClass, regular_ending: str, dakuten_ending: str
):
    """Handle the formation of the -te / -ta form for verbs belonging to
    any verb class. Logic for both forms follows similar logic but differs
    between (-te, -de) and (-ta, -da) based on the last particle of a Godan
    verb.

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        verb_class (enum): VerbClass Enum representing the verb class
            to which the verb belongs
        regular_ending (str): ending without dakuten
        dakuten_ending (str): ending with dakuten

        TODO... reformat this logic for endings

    Returns:
        str: The verb stem plus the -te / -ta particle depending on the
        verb class.
    """
    verb_stem, particle_ending = splice_verb(verb, verb_class)
    if verb_class == VerbClass.ICHIDAN:
        verb_ending = regular_ending
    else:
        if (
            particle_ending in [RU_PARTICLE, TSU_PARTICLE, U_PARTICLE]
            or verb in IKU_GROUP
        ):
            verb_ending = f"{CHISAI_TSU_PARTICLE}{regular_ending}"
        elif particle_ending in [BU_PARTICLE, MU_PARTICLE, NU_PARTICLE]:
            verb_ending = f"{N_PARTICLE}{dakuten_ending}"
        elif particle_ending in [KU_PARTICLE]:
            verb_ending = f"{I_PARTICLE}{regular_ending}"
        elif particle_ending in [GU_PARTICLE]:
            verb_ending = f"{I_PARTICLE}{dakuten_ending}"
        else:
            verb_ending = f"{SHI_PARTICLE}{regular_ending}"
    return f"{verb_stem}{verb_ending}"


def map_dictionary_to_a_ending(verb):
    """Generates Godan verb stem with corresponding -a particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -a particle attached (Godan verbs only)
    """
    return map_dict_form_to_different_ending(verb, A_PARTICLE)


def map_dictionary_to_e_ending(verb):
    """Generates Godan verb stem with corresponding -e particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -e particle attached (Godan verbs only)
    """
    return map_dict_form_to_different_ending(verb, E_PARTICLE)


def map_dictionary_to_i_ending(verb):
    """Generates Godan verb stem with corresponding -i particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -i particle attached (Godan verbs only)
    """
    return map_dict_form_to_different_ending(verb, I_PARTICLE)


def map_dictionary_to_o_ending(verb):
    """Generates Godan verb stem with corresponding -o particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -o particle attached (Godan verbs only)
    """
    return map_dict_form_to_different_ending(verb, O_PARTICLE)


def map_dict_form_to_different_ending(verb, desired_ending):
    """Generates Godan verb stem and computes the correct particle to attach based on the
    verb's last kana

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        desired_ending (str): target base_particle

    Returns:
        str: verb stem with the correct particle attached depending on the last kana particle
    of the Godan verb
    """
    verb_stem, particle_ending = splice_verb(verb, VerbClass.GODAN)

    return f"{verb_stem}{ENDING_DICT[particle_ending][desired_ending]}"


def convert_args(base_form: BaseForm, *args):
    return_kwargs = {
        "formality": Formality.PLAIN,
        "tense": Tense.NONPAST,
        "polarity": Polarity.POSITIVE,
    }
    for arg in args:
        for arg_type in ArgumentType:
            if arg in [arg_t.value for arg_t in arg_type.value]:
                return_kwargs[arg_type.value.__name__.lower()] = arg_type.value(arg)
                continue
    if base_form in [BaseForm.PLAIN, BaseForm.POLITE]:
        del return_kwargs[ArgumentType.FORMALITY.value.__name__.lower()]
    else:
        del return_kwargs[ArgumentType.TENSE.value.__name__.lower()]
    return return_kwargs


def convert_copula_args(copula_form: CopulaForm, *args):
    return_kwargs = {
        "formality": Formality.PLAIN,
        "tense": Tense.NONPAST,
        "polarity": Polarity.POSITIVE,
    }
    for arg in args:
        for arg_type in ArgumentType:
            if arg in [arg_t.value for arg_t in arg_type.value]:
                return_kwargs[arg_type.value.__name__.lower()] = arg_type.value(arg)
                continue
    if copula_form in [CopulaForm.PLAIN, CopulaForm.POLITE]:
        del return_kwargs["formality"]
    elif copula_form == CopulaForm.PRESUMPTIVE:
        del return_kwargs["tense"]
    elif copula_form in [CopulaForm.TE, CopulaForm.TARA]:
        del return_kwargs["tense"]
        del return_kwargs["polarity"]
    else:
        return {}
    return return_kwargs
