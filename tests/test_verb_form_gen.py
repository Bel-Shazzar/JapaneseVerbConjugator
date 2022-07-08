import unittest
from xmlrpc.client import UNSUPPORTED_ENCODING

from parameterized import parameterized
from src.japverbconj.constants.enumerated_types import (
    BaseForm,
    CopulaForm,
    Formality,
    Polarity,
    Tense,
)
from src.japverbconj.constants.irregular_verb_forms import NoConjugationError
from src.japverbconj.exceptions import (
    UnsupportedBaseFormError,
    UnsupportedCopulaFormError,
)
from src.japverbconj.verb_form_gen import (
    JapaneseVerbFormGenerator as jvfg,
    generate_japanese_copula_form,
)
from src.japverbconj.verb_form_gen import generate_japanese_verb_form

from tests.constants import COPULA_FORM_PARAMETERS, VERB_FORM_PARAMETERS, CopulaDa


class TestAllVerbForms(unittest.TestCase):
    @parameterized.expand(VERB_FORM_PARAMETERS)
    def test(self, _, verb, base_form: BaseForm, *args):
        attribute_name = "_".join(
            [base_form.name.lower(), *[arg.name.lower() for arg in args]]
        )
        try:
            result = generate_japanese_verb_form(
                verb.plain_nonpast_positive, verb.verb_class, base_form, *args
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


class TestCopula(unittest.TestCase):
    @parameterized.expand(COPULA_FORM_PARAMETERS)
    def test(self, _, copula_form: CopulaForm, *args):
        attribute_name = "_".join(
            [copula_form.name.lower(), *[arg.name.lower() for arg in args]]
        )
        try:
            result = generate_japanese_copula_form(copula_form, *args)
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

    # @parameterized.expand(
    #     [
    #         ("pos", Tense.NONPAST, Polarity.POSITIVE, CopulaDa.plain_positive),
    #         ("pos past", Tense.PAST, Polarity.POSITIVE, CopulaDa.plain_past),
    #         ("neg", Tense.NONPAST, Polarity.NEGATIVE, CopulaDa.plain_negative),
    #         ("neg past", Tense.PAST, Polarity.NEGATIVE, CopulaDa.plain_past_negative),
    #     ]
    # )
    # def test_copula_plain(self, _, tense, polarity, expected_copula):
    #     self.assertEqual(
    #         generate_japanese_copula_form(CopulaForm.PLAIN, tense, polarity),
    #         expected_copula,
    #     )

    # @parameterized.expand(
    #     [
    #         ("pos", Tense.NONPAST, Polarity.POSITIVE, CopulaDa.polite_positive),
    #         ("pos past", Tense.PAST, Polarity.POSITIVE, CopulaDa.polite_past),
    #         ("neg", Tense.NONPAST, Polarity.NEGATIVE, CopulaDa.polite_negative),
    #         ("neg past", Tense.PAST, Polarity.NEGATIVE, CopulaDa.polite_past_negative),
    #     ]
    # )
    # def test_copula_polite(self, _, tense, polarity, expected_copula):
    #     self.assertEqual(
    #         generate_japanese_copula_form(CopulaForm.POLITE, tense, polarity),
    #         expected_copula,
    #     )

    # def test_copula_conditional(self):
    #     self.assertEqual(
    #         generate_japanese_copula_form(CopulaForm.CONDITIONAL), CopulaDa.conditional
    #     )

    # @parameterized.expand(
    #     [
    #         ("pla pos", Formality.PLAIN, Polarity.POSITIVE, CopulaDa.presumptive_plain),
    #         (
    #             "pol pos",
    #             Formality.POLITE,
    #             Polarity.POSITIVE,
    #             CopulaDa.presumptive_polite,
    #         ),
    #         (
    #             "pla neg",
    #             Formality.PLAIN,
    #             Polarity.NEGATIVE,
    #             CopulaDa.presumptive_plain_negative,
    #         ),
    #         (
    #             "pol neg",
    #             Formality.POLITE,
    #             Polarity.NEGATIVE,
    #             CopulaDa.presumptive_polite_negative,
    #         ),
    #     ]
    # )
    # def test_copula_presumptive(self, _, formality, polarity, expected_copula):
    #     self.assertEqual(
    #         generate_japanese_copula_form(CopulaForm.PRESUMPTIVE, formality, polarity),
    #         expected_copula,
    #     )

    # @parameterized.expand(
    #     [
    #         ("pla", Formality.PLAIN, CopulaDa.te_plain),
    #         ("pol", Formality.POLITE, CopulaDa.te_polite),
    #     ]
    # )
    # def test_copula_te_form(self, _, formality, expected_copula):
    #     self.assertEqual(
    #         generate_japanese_copula_form(CopulaForm.TE, formality), expected_copula
    #     )

    # @parameterized.expand(
    #     [
    #         ("pla", Formality.PLAIN, CopulaDa.tara_plain),
    #         ("pol", Formality.POLITE, CopulaDa.tara_polite),
    #     ]
    # )
    # def test_copula_tara_form(self, _, formality, expected_copula):
    #     self.assertEqual(
    #         generate_japanese_copula_form(CopulaForm.TARA, formality), expected_copula
    #     )

    def test_unsupported_copula_form(self):
        with self.assertRaises(UnsupportedCopulaFormError):
            generate_japanese_copula_form(-1)


if __name__ == "__main__":
    unittest.main()
