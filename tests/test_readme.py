import unittest


class ImportTests(unittest.TestCase):

    def test_usage_1(self):
        from japanese_verb_conjugator_v2 import VerbClass, generate_japanese_verb_by_str

        self.assertEqual(
            generate_japanese_verb_by_str("飲む", VerbClass.GODAN, "pla"), "飲む"
        )
        self.assertEqual(
            generate_japanese_verb_by_str(
                "飲む", VerbClass.GODAN, "pla", "past", "neg"
            ),
            "飲まなかった",
        )
        self.assertEqual(
            generate_japanese_verb_by_str(
                "飲む", VerbClass.GODAN, "pass", "pol", "neg"
            ),
            "飲まれません",
        )

    def test_usage_2(self):
        from japanese_verb_conjugator_v2 import Formality
        from japanese_verb_conjugator_v2 import JapaneseVerbFormGenerator as jvfg
        from japanese_verb_conjugator_v2 import Polarity, Tense, VerbClass

        self.assertEqual(
            jvfg.generate_plain_form(
                "飲む", VerbClass.GODAN, Tense.NONPAST, Polarity.POSITIVE
            ),
            "飲む",
        )
        self.assertEqual(
            jvfg.generate_plain_form(
                "飲む", VerbClass.GODAN, Tense.NONPAST, Polarity.NEGATIVE
            ),
            "飲まない",
        )

    def test_copula_1(self):
        from japanese_verb_conjugator_v2 import generate_japanese_copula_by_str

        self.assertEqual(generate_japanese_copula_by_str("pla"), "だ")
        self.assertEqual(
            generate_japanese_copula_by_str("pres", "pol", "neg"), "ではないでしょう"
        )

    def test_copula_2(self):
        from japanese_verb_conjugator_v2 import Formality
        from japanese_verb_conjugator_v2 import JapaneseVerbFormGenerator as jvfg
        from japanese_verb_conjugator_v2 import Polarity, Tense, VerbClass

        self.assertEqual(
            jvfg.copula.generate_plain_form(Tense.NONPAST, Polarity.POSITIVE), "だ"
        )
        self.assertEqual(
            jvfg.copula.generate_presumptive_form(Formality.POLITE, Polarity.NEGATIVE),
            "ではないでしょう",
        )
