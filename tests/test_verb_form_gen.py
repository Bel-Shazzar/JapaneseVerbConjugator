import unittest

import romkan
from parameterized import parameterized

from japanese_verb_conjugator_v2.constants.enumerated_types import (
    BaseForm,
    CopulaForm,
    Formality,
    IrregularVerb,
)
from japanese_verb_conjugator_v2.constants.exceptions import (
    UnsupportedBaseFormError,
    UnsupportedCopulaFormError,
)
from japanese_verb_conjugator_v2.constants.irregular_verb_forms import (
    NoConjugationError,
    get_irregular_conjugation,
)
from japanese_verb_conjugator_v2.verb_form_gen import (
    generate_japanese_copula_by_str,
    generate_japanese_copula_form,
    generate_japanese_verb_by_str,
    generate_japanese_verb_form,
)

from .constants import COPULA_FORM_PARAMETERS, VERB_FORM_PARAMETERS, CopulaDa


class TestAllVerbForms(unittest.TestCase):
    @parameterized.expand(VERB_FORM_PARAMETERS)
    def test(self, _, verb, base_form: BaseForm, *args):
        attribute_name = "_".join(
            [base_form.name.lower(), *[arg.name.lower() for arg in args]]
        )
        try:
            result = generate_japanese_verb_by_str(
                verb.plain_nonpast_positive,
                verb.verb_class,
                base_form.value,
                *[arg.value for arg in args],
            )
        except NoConjugationError:
            if hasattr(verb, attribute_name):
                self.fail(
                    f"verb {verb.romaji} has attribute {attribute_name} -> {getattr(verb, attribute_name)}"
                )
            else:
                self.skipTest(f"verb {verb.romaji} has not attribute {attribute_name}")
        else:
            self.assertTrue(
                hasattr(verb, attribute_name),
                f"verb {verb} should have attribute {attribute_name} -> {result}",
            )
            self.assertEqual(result, getattr(verb, attribute_name))
            self.assertEqual(
                result,
                generate_japanese_verb_by_str(
                    verb.plain_nonpast_positive,
                    verb.verb_class,
                    base_form.value,
                    *[arg.value for arg in reversed(args)],
                ),
            )

    def test_unsupported_base_form_error(self):
        with self.assertRaises(UnsupportedBaseFormError):
            generate_japanese_verb_form("", None, -1)

    def test_unsupported_base_form_str_error(self):
        with self.assertRaises(UnsupportedBaseFormError):
            generate_japanese_verb_by_str("", None, "no")

    @parameterized.expand([(verb.name.lower(), verb.value) for verb in IrregularVerb])
    def test_no_irregular_conjugation_error(self, _, verb):
        with self.assertRaises(
            NoConjugationError,
        ):
            get_irregular_conjugation(
                verb, base_form=BaseForm.PLAIN, formality=Formality.POLITE
            )


class TestCopula(unittest.TestCase):
    @parameterized.expand(COPULA_FORM_PARAMETERS)
    def test(self, _, copula_form: CopulaForm, *args):
        attribute_name = "_".join(
            [copula_form.name.lower(), *[arg.name.lower() for arg in args]]
        )
        try:
            result = generate_japanese_copula_by_str(
                copula_form.value, *[arg.value for arg in args]
            )
        except NoConjugationError:
            if hasattr(CopulaDa, attribute_name):
                self.fail(
                    f"da has attribute {attribute_name} -> {getattr(CopulaDa, attribute_name)}"
                )
            else:
                self.skipTest(f"da has not attribute {attribute_name}")
        else:
            self.assertTrue(
                hasattr(CopulaDa, attribute_name),
                f"da should have attribute {attribute_name} -> {result}",
            )
            self.assertEqual(result, getattr(CopulaDa, attribute_name))

    @parameterized.expand(COPULA_FORM_PARAMETERS)
    def test_reversed(self, _, copula_form: CopulaForm, *args):
        attribute_name = "_".join(
            [copula_form.name.lower(), *[arg.name.lower() for arg in args]]
        )
        if hasattr(CopulaDa, attribute_name):
            result = generate_japanese_copula_by_str(
                copula_form.value,
                *[arg.value for arg in reversed(args)],
            )
            self.assertEqual(result, getattr(CopulaDa, attribute_name))

    def test_unsupported_copula_form_error(self):
        with self.assertRaises(UnsupportedCopulaFormError):
            generate_japanese_copula_form(-1)

    def test_unsupported_copula_str_error(self):
        with self.assertRaises(UnsupportedCopulaFormError):
            generate_japanese_copula_by_str("no")


if __name__ == "__main__":
    unittest.main()
