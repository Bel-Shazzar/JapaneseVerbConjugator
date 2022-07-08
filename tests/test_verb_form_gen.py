import unittest

from parameterized import parameterized
from src.japverbconj.constants.enumerated_types import BaseForm, CopulaForm
from src.japverbconj.constants.irregular_verb_forms import NoConjugationError
from src.japverbconj.exceptions import (
    UnsupportedBaseFormError,
    UnsupportedCopulaFormError,
)
from src.japverbconj.verb_form_gen import (
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

    def test_unsupported_base_form_error(self):
        with self.assertRaises(UnsupportedBaseFormError):
            generate_japanese_verb_form("", None, -1)

    def test_unsupported_base_form_str_error(self):
        with self.assertRaises(UnsupportedBaseFormError):
            generate_japanese_verb_by_str("", None, "no")


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

    def test_unsupported_copula_form_error(self):
        with self.assertRaises(UnsupportedCopulaFormError):
            generate_japanese_copula_form(-1)

    def test_unsupported_copula_str_error(self):
        with self.assertRaises(UnsupportedCopulaFormError):
            generate_japanese_copula_by_str("no")


if __name__ == "__main__":
    unittest.main()
