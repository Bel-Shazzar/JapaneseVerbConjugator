from itertools import product

from japanese_verb_conjugator_v2.constants.enumerated_types import (
    BaseForm,
    CopulaForm,
    Formality,
    Polarity,
    Tense,
    VerbClass,
)

korean_with_japanese = "한국어처리기む"
english_with_japanese = "Heloむ"
verb_incorrect_particle_ending = "飲ま"


class GodanVerbNomu:
    # http://www.japaneseverbconjugator.com/VerbDetails.asp?txtVerb=%E9%A3%B2%E3%82%80
    romaji = "nomu"
    verb_class = VerbClass.GODAN

    # Plain Verb Forms
    plain_nonpast_positive = "飲む"
    plain_nonpast_negative = "飲まない"
    plain_past_positive = "飲んだ"
    plain_past_negative = "飲まなかった"

    # Formal Verb Forms
    polite_nonpast_positive = "飲みます"
    polite_nonpast_negative = "飲みません"
    polite_past_positive = "飲みました"
    polite_past_negative = "飲みませんでした"

    # Te form (gerund)
    te_plain_positive = "飲んで"
    te_plain_negative = "飲まなくて"
    te_polite_positive = "飲みまして"
    te_polite_negative = "飲みませんでして"

    # Ta Forms
    ta_plain_positive = plain_past_positive
    ta_plain_negative = plain_past_negative
    ta_polite_positive = polite_past_positive
    ta_polite_negative = polite_past_negative

    # Tari form
    tari_plain_positive = "飲んだり"
    tari_plain_negative = "飲まなかったり"
    tari_polite_positive = "飲みましたり"
    tari_polite_negative = "飲みませんでしたり"

    # Conditional Verb Forms
    conditional_plain_positive = "飲んだら"
    conditional_plain_negative = "飲まなかったら"
    conditional_polite_positive = "飲みましたら"
    conditional_polite_negative = "飲みませんでしたら"

    # Tara form
    tara_plain_positive = conditional_plain_positive
    tara_plain_negative = conditional_plain_negative
    tara_polite_positive = conditional_polite_positive
    tara_polite_negative = conditional_polite_negative

    # Volitional Verb Forms
    volitional_plain_positive = "飲もう"
    volitional_plain_negative = "飲まないだろう"
    volitional_polite_positive = "飲みましょう"
    volitional_polite_negative = "飲まないでしょう"

    # Potential Verb Forms
    potential_plain_positive = "飲める"
    potential_plain_negative = "飲めない"
    potential_polite_positive = "飲めます"
    potential_polite_negative = "飲めません"

    # Imperative Verb Forms
    imperative_plain_positive = "飲め"
    imperative_plain_negative = "飲むな"
    imperative_polite_positive = "飲んでください"
    imperative_polite_negative = "飲まないでください"

    # Causative Verb Forms
    causative_plain_positive = "飲ませる"
    causative_plain_negative = "飲ませない"
    causative_polite_positive = "飲ませます"
    causative_polite_negative = "飲ませません"

    # Passive Verb Forms
    passive_plain_positive = "飲まれる"
    passive_plain_negative = "飲まれない"
    passive_polite_positive = "飲まれます"
    passive_polite_negative = "飲まれません"

    # Provisional Verb Forms
    provisional_plain_positive = "飲めば"
    provisional_plain_negative = "飲まなければ"
    provisional_polite_positive = "飲めば"
    provisional_polite_negative = "飲まなければ"


class GodanVerbAru:
    # https://www.japandict.com/%E6%9C%89%E3%82%8B?lang=eng#entry-1296400
    romaji = "aru"
    verb_class = VerbClass.GODAN

    # Plain Verb Forms
    plain_nonpast_positive = "ある"
    plain_nonpast_negative = "ない"
    plain_past_positive = "あった"
    plain_past_negative = "なかった"

    # Formal Verb Forms
    polite_nonpast_positive = "あります"
    polite_nonpast_negative = "ありません"
    polite_past_positive = "ありました"
    polite_past_negative = "ありませんでした"

    # Te form (gerund)
    te_plain_positive = "あって"
    te_plain_negative = "なくて"
    te_polite_positive = "ありまして"
    te_polite_negative = "ありませんでして"

    # Ta Forms
    ta_plain_positive = plain_past_positive
    ta_plain_negative = plain_past_negative
    ta_polite_positive = polite_past_positive
    ta_polite_negative = polite_past_negative

    # Tari form
    tari_plain_positive = "あったり"
    tari_plain_negative = "なかったり"
    tari_polite_positive = "ありましたり"
    tari_polite_negative = "ありませんでしたり"

    # Conditional Verb Forms
    conditional_plain_positive = "あったら"
    conditional_plain_negative = "なかったら"
    conditional_polite_positive = "ありましたら"
    conditional_polite_negative = "ありませんでしたら"

    # Tara form
    tara_plain_positive = conditional_plain_positive
    tara_plain_negative = conditional_plain_negative
    tara_polite_positive = conditional_polite_positive
    tara_polite_negative = conditional_polite_negative

    # Volitional Verb Forms
    volitional_plain_positive = "あろう"
    volitional_plain_negative = "ないだろう"
    volitional_polite_positive = "ありましょう"
    volitional_polite_negative = "ないでしょう"

    # Potential Verb Forms
    potential_plain_positive = "あれる"
    potential_plain_negative = "あれない"
    potential_polite_positive = "あれます"
    potential_polite_negative = "あれません"

    # Imperative Verb Forms
    imperative_plain_positive = "あれ"
    imperative_plain_negative = "あるな"
    imperative_polite_positive = "あってください"
    imperative_polite_negative = "ないでください"

    # Causative Verb Forms
    causative_plain_positive = "あらせる"
    causative_plain_negative = "あらせない"
    causative_polite_positive = "あらせます"
    causative_polite_negative = "あらせません"

    # Passive Verb Forms
    passive_plain_positive = "あられる"
    passive_plain_negative = "あられない"
    passive_polite_positive = "あられます"
    passive_polite_negative = "あられません"

    # Provisional Verb Forms
    provisional_plain_positive = "あれば"
    provisional_plain_negative = "なければ"
    provisional_polite_positive = "あれば"
    provisional_polite_negative = "なければ"


class GodanVerbIku:
    romaji = "iku"
    verb_class = VerbClass.GODAN

    # Plain Verb Forms
    plain_nonpast_positive = "行く"
    plain_nonpast_negative = "行かない"
    plain_past_positive = "行った"
    plain_past_negative = "行かなかった"

    # Formal Verb Forms
    polite_nonpast_positive = "行きます"
    polite_nonpast_negative = "行きません"
    polite_past_positive = "行きました"
    polite_past_negative = "行きませんでした"

    # Te form (gerund)
    te_plain_positive = "行って"
    te_plain_negative = "行かなくて"
    te_polite_positive = "行きまして"
    te_polite_negative = "行きませんでして"

    # Ta Forms
    ta_plain_positive = plain_past_positive
    ta_plain_negative = plain_past_negative
    ta_polite_positive = polite_past_positive
    ta_polite_negative = polite_past_negative

    # Tari form
    tari_plain_positive = "行ったり"
    tari_plain_negative = "行かなかったり"
    tari_polite_positive = "行きましたり"
    tari_polite_negative = "行きませんでしたり"

    # Conditional Verb Forms
    conditional_plain_positive = "行ったら"
    conditional_plain_negative = "行かなかったら"
    conditional_polite_positive = "行きましたら"
    conditional_polite_negative = "行きませんでしたら"

    # Tara form
    tara_plain_positive = conditional_plain_positive
    tara_plain_negative = conditional_plain_negative
    tara_polite_positive = conditional_polite_positive
    tara_polite_negative = conditional_polite_negative

    # Volitional Verb Forms
    volitional_plain_positive = "行こう"
    volitional_plain_negative = "行かないだろう"
    volitional_polite_positive = "行きましょう"
    volitional_polite_negative = "行かないでしょう"

    # Potential Verb Forms
    potential_plain_positive = "行ける"
    potential_plain_negative = "行けない"
    potential_polite_positive = "行けます"
    potential_polite_negative = "行けません"

    # Imperative Verb Forms
    imperative_plain_positive = "行け"
    imperative_plain_negative = "行くな"
    imperative_polite_positive = "行ってください"
    imperative_polite_negative = "行かないでください"

    # Causative Verb Forms
    causative_plain_positive = "行かせる"
    causative_plain_negative = "行かせない"
    causative_polite_positive = "行かせます"
    causative_polite_negative = "行かせません"

    # Passive Verb Forms
    passive_plain_positive = "行かれる"
    passive_plain_negative = "行かれない"
    passive_polite_positive = "行かれます"
    passive_polite_negative = "行かれません"

    # Provisional Verb Forms
    provisional_plain_positive = "行けば"
    provisional_plain_negative = "行かなければ"
    provisional_polite_positive = "行けば"
    provisional_polite_negative = "行かなければ"


class GodanVerbKudasaru:
    romaji = "kudasaru"
    verb_class = VerbClass.GODAN

    # Plain Verb Forms
    plain_nonpast_positive = "くださる"
    plain_nonpast_negative = "くださらない"
    plain_past_positive = "くださった"
    plain_past_negative = "くださらなかった"

    # Formal Verb Forms
    polite_nonpast_positive = "くださいます"
    polite_nonpast_negative = "くださいません"
    polite_past_positive = "くださいました"
    polite_past_negative = "くださいませんでした"

    # Te form (gerund)
    te_plain_positive = "くださって"
    te_plain_negative = "くださらなくて"
    te_polite_positive = "くださいまして"
    te_polite_negative = "くださいませんでして"

    # Ta Forms
    ta_plain_positive = plain_past_positive
    ta_plain_negative = plain_past_negative
    ta_polite_positive = polite_past_positive
    ta_polite_negative = polite_past_negative

    # Tari form
    tari_plain_positive = "くださったり"
    tari_plain_negative = "くださらなかったり"
    tari_polite_positive = "くださいましたり"
    tari_polite_negative = "くださいませんでしたり"

    # Conditional Verb Forms
    conditional_plain_positive = "くださったら"
    conditional_plain_negative = "くださらなかったら"
    conditional_polite_positive = "くださいましたら"
    conditional_polite_negative = "くださいませんでしたら"

    # Tara form
    tara_plain_positive = conditional_plain_positive
    tara_plain_negative = conditional_plain_negative
    tara_polite_positive = conditional_polite_positive
    tara_polite_negative = conditional_polite_negative

    # Volitional Verb Forms
    volitional_plain_positive = "くださろう"
    volitional_plain_negative = "くださらないだろう"
    volitional_polite_positive = "くださいましょう"
    volitional_polite_negative = "くださらないでしょう"

    # Potential Verb Forms
    potential_plain_positive = "くだされる"
    potential_plain_negative = "くだされない"
    potential_polite_positive = "くだされます"
    potential_polite_negative = "くだされません"

    # Imperative Verb Forms
    imperative_plain_positive = "ください"
    imperative_plain_negative = "くださるな"
    imperative_polite_positive = "くださってください"
    imperative_polite_negative = "くださらないでください"

    # Causative Verb Forms
    causative_plain_positive = "くださらせる"
    causative_plain_negative = "くださらせない"
    causative_polite_positive = "くださらせます"
    causative_polite_negative = "くださらせません"

    # Passive Verb Forms
    passive_plain_positive = "くださられる"
    passive_plain_negative = "くださられない"
    passive_polite_positive = "くださられます"
    passive_polite_negative = "くださられません"

    # Provisional Verb Forms
    provisional_plain_positive = "くだされば"
    provisional_plain_negative = "くださらなければ"
    provisional_polite_positive = "くだされば"
    provisional_polite_negative = "くださらなければ"


class IchidanVerbTaberu:
    # http://www.japaneseverbconjugator.com/VerbDetails.asp?txtVerb=%E9%A3%9F%E3%81%B9%E3%82%8B
    romaji = "taberu"
    verb_class = VerbClass.ICHIDAN

    # Plain Verb Forms
    plain_nonpast_positive = "食べる"
    plain_nonpast_negative = "食べない"
    plain_past_positive = "食べた"
    plain_past_negative = "食べなかった"

    # Formal Verb Forms
    polite_nonpast_positive = "食べます"
    polite_nonpast_negative = "食べません"
    polite_past_positive = "食べました"
    polite_past_negative = "食べませんでした"

    # Te form (gerund)
    te_plain_positive = "食べて"
    te_plain_negative = "食べなくて"
    te_polite_positive = "食べまして"
    te_polite_negative = "食べませんでして"

    # Ta Forms
    ta_plain_positive = plain_past_positive
    ta_plain_negative = plain_past_negative
    ta_polite_positive = polite_past_positive
    ta_polite_negative = polite_past_negative

    # Tari form
    tari_plain_positive = "食べたり"
    tari_plain_negative = "食べなかったり"
    tari_polite_positive = "食べましたり"
    tari_polite_negative = "食べませんでしたり"

    # Conditional Verb Forms
    conditional_plain_positive = "食べたら"
    conditional_plain_negative = "食べなかったら"
    conditional_polite_positive = "食べましたら"
    conditional_polite_negative = "食べませんでしたら"

    # Tara form
    tara_plain_positive = conditional_plain_positive
    tara_plain_negative = conditional_plain_negative
    tara_polite_positive = conditional_polite_positive
    tara_polite_negative = conditional_polite_negative

    # Volitional Verb Forms
    volitional_plain_positive = "食べよう"
    volitional_plain_negative = "食べないだろう"
    volitional_polite_positive = "食べましょう"
    volitional_polite_negative = "食べないでしょう"

    # Potential Verb Forms
    potential_plain_positive = "食べられる"
    potential_plain_negative = "食べられない"
    potential_polite_positive = "食べられます"
    potential_polite_negative = "食べられません"

    # Imperative Verb Forms
    imperative_plain_positive = "食べろ"
    imperative_plain_negative = "食べるな"
    imperative_polite_positive = "食べてください"
    imperative_polite_negative = "食べないでください"

    # Causative Verb Forms
    causative_plain_positive = "食べさせる"
    causative_plain_negative = "食べさせない"
    causative_polite_positive = "食べさせます"
    causative_polite_negative = "食べさせません"

    # Passive Verb Forms
    passive_plain_positive = "食べられる"
    passive_plain_negative = "食べられない"
    passive_polite_positive = "食べられます"
    passive_polite_negative = "食べられません"

    # Provisional Verb Forms
    provisional_plain_positive = "食べれば"
    provisional_plain_negative = "食べなければ"
    provisional_polite_positive = "食べれば"
    provisional_polite_negative = "食べなければ"


class IrregularVerbSuru:
    # http://www.japaneseverbconjugator.com/Suru.asp
    romaji = "benkyousuru"
    verb_class = VerbClass.IRREGULAR

    # Plain Verb Forms
    plain_nonpast_positive = "勉強する"
    plain_nonpast_negative = "勉強しない"
    plain_past_positive = "勉強した"
    plain_past_negative = "勉強しなかった"

    # Formal Verb Forms
    polite_nonpast_positive = "勉強します"
    polite_nonpast_negative = "勉強しません"
    polite_past_positive = "勉強しました"
    polite_past_negative = "勉強しませんでした"

    # Te form (gerund)
    te_plain_positive = "勉強して"
    te_plain_negative = "勉強しなくて"
    te_polite_positive = "勉強しまして"
    te_polite_negative = "勉強しませんでして"

    # Ta Forms
    ta_plain_positive = plain_past_positive
    ta_plain_negative = plain_past_negative
    ta_polite_positive = polite_past_positive
    ta_polite_negative = polite_past_negative

    # Tari form
    tari_plain_positive = "勉強したり"
    tari_plain_negative = "勉強しなかったり"
    tari_polite_positive = "勉強しましたり"
    tari_polite_negative = "勉強しませんでしたり"

    # Conditional Verb Forms
    conditional_plain_positive = "勉強したら"
    conditional_plain_negative = "勉強しなかったら"
    conditional_polite_positive = "勉強しましたら"
    conditional_polite_negative = "勉強しませんでしたら"

    # Tara form
    tara_plain_positive = conditional_plain_positive
    tara_plain_negative = conditional_plain_negative
    tara_polite_positive = conditional_polite_positive
    tara_polite_negative = conditional_polite_negative

    # Volitional Verb Forms
    volitional_plain_positive = "勉強しよう"
    volitional_polite_positive = "勉強しましょう"
    volitional_plain_negative = "勉強しないだろう"
    volitional_polite_negative = "勉強しないでしょう"

    # Potential Verb Forms
    potential_plain_positive = "勉強出来る"
    potential_plain_negative = "勉強出来ない"
    potential_polite_positive = "勉強出来ます"
    potential_polite_negative = "勉強出来ません"

    # Imperative Verb Forms
    imperative_plain_positive = "勉強しろ"
    imperative_plain_negative = "勉強するな"
    imperative_polite_positive = "勉強してください"
    imperative_polite_negative = "勉強しないでください"

    # Causative Verb Forms
    causative_plain_positive = "勉強させる"
    causative_plain_negative = "勉強ささない"
    causative_polite_positive = "勉強させます"
    causative_polite_negative = "勉強させません"

    # Passive Verb Forms
    passive_plain_positive = "勉強される"
    passive_plain_negative = "勉強されない"
    passive_polite_positive = "勉強されます"
    passive_polite_negative = "勉強されません"

    # Provisional Verb Forms
    provisional_plain_positive = "勉強すれば"
    provisional_plain_negative = "勉強しなければ"
    provisional_polite_positive = "勉強しませば"
    provisional_polite_negative = "勉強しませんなら"


class IrregularVerbKuru:
    # http://www.japaneseverbconjugator.com/Kuru.asp
    romaji = "kuru"
    verb_class = VerbClass.IRREGULAR

    # Plain Verb Forms
    plain_nonpast_positive = "くる"
    plain_nonpast_negative = "こない"
    plain_past_positive = "きた"
    plain_past_negative = "こなかった"

    # Formal Verb Forms
    polite_nonpast_positive = "きます"
    polite_nonpast_negative = "きません"
    polite_past_positive = "きました"
    polite_past_negative = "きませんでした"

    # Te form (gerund)
    te_plain_positive = "きて"
    te_plain_negative = "こなくて"
    te_polite_positive = "きまして"
    te_polite_negative = "きませんでして"

    # Ta Forms
    ta_plain_positive = plain_past_positive
    ta_plain_negative = plain_past_negative
    ta_polite_positive = polite_past_positive
    ta_polite_negative = polite_past_negative

    # Tari form
    tari_plain_positive = "きたり"
    tari_plain_negative = "こなかったり"
    tari_polite_positive = "きましたり"
    tari_polite_negative = "きませんでしたり"

    # Conditional Verb Forms
    conditional_plain_positive = "きたら"
    conditional_plain_negative = "こなかったら"
    conditional_polite_positive = "きましたら"
    conditional_polite_negative = "きませんでしたら"

    # Tara form
    tara_plain_positive = conditional_plain_positive
    tara_plain_negative = conditional_plain_negative
    tara_polite_positive = conditional_polite_positive
    tara_polite_negative = conditional_polite_negative

    # Volitional Verb Forms
    volitional_polite_positive = "きましょう"
    volitional_polite_negative = "こないでしょう"
    volitional_plain_positive = "こよう"
    volitional_plain_negative = "こないだろう"

    # Potential Verb Forms
    potential_plain_positive = "こられる"
    potential_plain_negative = "こられない"
    potential_polite_positive = "こられます"
    potential_polite_negative = "こられません"

    # Imperative Verb Forms
    imperative_plain_positive = "こい"
    imperative_plain_negative = "くるな"
    imperative_polite_positive = "きてください"
    imperative_polite_negative = "こないでください"

    # Causative Verb Forms
    causative_plain_positive = "こさせる"
    causative_plain_negative = "こさせない"
    causative_polite_positive = "こさせます"
    causative_polite_negative = "こさせません"

    # Passive Verb Forms
    passive_plain_positive = "こられる"
    passive_plain_negative = "こられない"
    passive_polite_positive = "こられます"
    passive_polite_negative = "こられません"

    # Provisional Verb Forms
    provisional_plain_positive = "くれば"
    provisional_plain_negative = "こなければ"
    provisional_polite_positive = "きませば"
    provisional_polite_negative = "きませんなら"


class IrregularVerbKuruKanji:
    # http://www.japaneseverbconjugator.com/Kuru.asp
    romaji = "kurukanji"
    verb_class = VerbClass.IRREGULAR

    # Plain Verb Forms
    plain_nonpast_positive = "来る"
    plain_nonpast_negative = "来ない"
    plain_past_positive = "来た"
    plain_past_negative = "来なかった"

    # Formal Verb Forms
    polite_nonpast_positive = "来ます"
    polite_nonpast_negative = "来ません"
    polite_past_positive = "来ました"
    polite_past_negative = "来ませんでした"

    # Te form (gerund)
    te_plain_positive = "来て"
    te_plain_negative = "来なくて"
    te_polite_positive = "来まして"
    te_polite_negative = "来ませんでして"

    # Ta Forms
    ta_plain_positive = plain_past_positive
    ta_plain_negative = plain_past_negative
    ta_polite_positive = polite_past_positive
    ta_polite_negative = polite_past_negative

    # Tari form
    tari_plain_positive = "来たり"
    tari_plain_negative = "来なかったり"
    tari_polite_positive = "来ましたり"
    tari_polite_negative = "来ませんでしたり"

    # Conditional Verb Forms
    conditional_plain_positive = "来たら"
    conditional_plain_negative = "来なかったら"
    conditional_polite_positive = "来ましたら"
    conditional_polite_negative = "来ませんでしたら"

    # Tara form
    tara_plain_positive = conditional_plain_positive
    tara_plain_negative = conditional_plain_negative
    tara_polite_positive = conditional_polite_positive
    tara_polite_negative = conditional_polite_negative

    # Volitional Verb Forms
    volitional_plain_positive = "来よう"
    volitional_plain_negative = "来ないだろう"
    volitional_polite_positive = "来ましょう"
    volitional_polite_negative = "来ないでしょう"

    # Potential Verb Forms
    potential_plain_positive = "来られる"
    potential_plain_negative = "来られない"
    potential_polite_positive = "来られます"
    potential_polite_negative = "来られません"

    # Imperative Verb Forms
    imperative_plain_positive = "来い"
    imperative_plain_negative = "来るな"
    imperative_polite_positive = "来てください"
    imperative_polite_negative = "来ないでください"

    # Causative Verb Forms
    causative_plain_positive = "来させる"
    causative_plain_negative = "来させない"
    causative_polite_positive = "来させます"
    causative_polite_negative = "来させません"

    # Passive Verb Forms
    passive_plain_positive = "来られる"
    passive_plain_negative = "来られない"
    passive_polite_positive = "来られます"
    passive_polite_negative = "来られません"

    # Provisional Verb Forms
    provisional_plain_positive = "来れば"
    provisional_plain_negative = "来なければ"
    provisional_polite_positive = "来ませば"
    provisional_polite_negative = "来ませんなら"


class CopulaDa:
    plain_nonpast_positive = "だ"
    plain_nonpast_negative = "ではない"
    plain_past_positive = "だった"
    plain_past_negative = "なかった"
    polite_nonpast_positive = "です"
    polite_nonpast_negative = "ではありません"
    polite_past_positive = "でした"
    polite_past_negative = "ではありませんでした"
    conditional = "なら"
    presumptive_plain_positive = "だろう"
    presumptive_plain_negative = "ではないだろう"
    presumptive_polite_positive = "でしょう"
    presumptive_polite_negative = "ではないでしょう"
    te_plain = "で"
    te_polite = "でして"
    tara_plain = "だったら"
    tara_polite = "でしたら"


VERB_LIST = [
    GodanVerbNomu,
    GodanVerbAru,
    GodanVerbIku,
    GodanVerbKudasaru,
    IchidanVerbTaberu,
    IrregularVerbSuru,
    IrregularVerbKuru,
    IrregularVerbKuruKanji,
]

VERB_FORM_PARAMETERS = [
    *[
        (
            f"{verb.romaji}_{form.name.lower()}_"
            + "_".join([arg.name.lower() for arg in args]),
            verb,
            form,
            *args,
        )
        for verb, form, *args in product(
            VERB_LIST, [BaseForm.PLAIN, BaseForm.POLITE], Tense, Polarity
        )
    ],
    *[
        (
            f"{verb.romaji}_{form.name.lower()}_"
            + "_".join([arg.name.lower() for arg in args]),
            verb,
            form,
            *args,
        )
        for verb, form, *args in product(
            VERB_LIST,
            [
                BaseForm.TE,
                BaseForm.TA,
                BaseForm.TARI,
                BaseForm.TARA,
                BaseForm.CONDITIONAL,
                BaseForm.VOLITIONAL,
                BaseForm.POTENTIAL,
                BaseForm.IMPERATIVE,
                BaseForm.PROVISIONAL,
                BaseForm.CAUSATIVE,
                BaseForm.PASSIVE,
            ],
            Formality,
            Polarity,
        )
    ],
]
COPULA_FORM_PARAMETERS = [
    *[
        (
            f"copula_{form.name.lower()}_"
            + "_".join([arg.name.lower() for arg in args]),
            form,
            *args,
        )
        for form, *args in product(
            [CopulaForm.PLAIN, CopulaForm.POLITE], Tense, Polarity
        )
    ],
    *[
        (
            f"copula_{form.name.lower()}_"
            + "_".join([arg.name.lower() for arg in args]),
            form,
            *args,
        )
        for form, *args in product([CopulaForm.PRESUMPTIVE], Formality, Polarity)
    ],
    *[
        (
            f"copula_{form.name.lower()}_"
            + "_".join([arg.name.lower() for arg in args]),
            form,
            *args,
        )
        for form, *args in product([CopulaForm.TE, CopulaForm.TARA], Formality)
    ],
    *[
        (
            f"copula_{form.name.lower()}_"
            + "_".join([arg.name.lower() for arg in args]),
            form,
            *args,
        )
        for form, *args in product([CopulaForm.CONDITIONAL])
    ],
]
