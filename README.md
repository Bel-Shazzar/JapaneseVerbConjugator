# Japanese Verb Conjugator

Japanese Verb Conjugator is a Python library for conjugating Japanese verbs. 
This fork overhauled most of the base package at this point.
Changes are recorded in CHANGELOG.md.

### What forms will Japanese Verb Conjugator conjugate?

Japanese Verb Conjugator conjugates the following verb forms:

* plain form
* polite form
* ~te form
* ~ta form
* ~tari form
* ~tara form
* conditional form
* volitional form
* potential form
* imperative form
* provisional form
* causative form
* passive form

Japanese Verb Conjugator conjugates verbs based on `verb class`, `tense`, `formality`, and `polarity` parameters. Depending on the conjugation and [verb class](https://wtawa.people.amherst.edu/jvrules/index.php?form=groups), the parameters for conjugation methods may vary. 

**Example**

`generate_plain_form` requires `verb class`, `tense`, and `formality` parameters.

`generate_volitional_form` requires `verb class`, `tense`, and `polarity` parameters.

Similarily the conjugations of the copula だ/です can be generated.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `japanese-verb-conjugator-v2`. If you want to install `japanese-verb-conjugator-v2` and its dependencies in a virtual environment, first create and activiate a virtual environment. If you want to change the virtual environment name to someting other than `venv`, replace the second `venv` with your desired name. Use that same name to replace `venv` in the second command.

```python
python3 -m venv venv
source venv/bin/activate
```

If you run into trouble, see the [Python Virtual Environment tutorial](https://docs.python.org/3/tutorial/venv.html). 

### Method 1: Pypi
After installing and activating the virtual environment, run the following commands to install `japanese-verb-conjugator-v2` and its dependencies.

```bash
pip install japanese-verb-conjugator-v2
```

You should be good to go! See the **Usage** section on how to get started using the library.

### Method 2: Clone this repository

Go to the directory you want to clone this repository and run the following command.

```bash
git clone https://github.com/Bel-Shazzar/JapaneseVerbConjugator.git
```

To install the Library use the following command

```bash
pip intall poetry
poetry install [--with dev,test]
```

You should be good to go! See the **Usage** section on how to get started using the library.

## Usage

The easiest to use method is the following:

```python
from japanese_verb_conjugator_v2 import VerbClass, generate_japanese_verb_by_str

generate_japanese_verb_by_str("飲む", VerbClass.GODAN, "pla") # returns '飲む
generate_japanese_verb_by_str("飲む", VerbClass.GODAN, "pla", "past", "neg") # returns '飲まなかった'
generate_japanese_verb_by_str("飲む", VerbClass.GODAN, "pass", "pol", "neg") # returns '飲まれません'
```
The strings after the VerbClass are built like this:

The first string is required and must determine the desired BaseForm from the following.
```python
BaseForm.PLAIN = "pla"
BaseForm.POLITE = "pol"
BaseForm.TE = "te"
BaseForm.TA = "ta"
BaseForm.TARI = "tari"
BaseForm.TARI = "tari"
BaseForm.CONDITIONAL = "cond"
BaseForm.VOLITIONAL = "vol"
BaseForm.POTENTIAL = "pot"
BaseForm.IMPERATIVE = "imp"
BaseForm.PROVISIONAL = "prov"
BaseForm.CAUSATIVE = "caus"
BaseForm.PASSIVE = "pass"
```

The following arguments determine the specific conjugation, based on Formality, Tense and Polarity.
```python
Formality.PLAIN = "pla"
Formality.POLITE = "pol"

Tense.NONPAST = "nonpast"
Tense.PAST = "past"

Polarity.POSITIVE = "pos"
Polarity.NEGATIVE = "neg"
```

* if an argument is left out, the first choice in the list above is assumed
* the order of the arguments does not matter
* it is not possible to give arguments that are not present in the corresponding BaseForm, see following table for details

| BaseForm | Possible arguments |
| - | - |
| BaseForm.PLAIN<br>BaseForm.POLITE | Tense, Polarity |
| BaseForm.TE<br>BaseForm.TA<br>BaseForm.TARI<br>BaseForm.TARA<br>BaseForm.CONDITIONAL<br>BaseForm.VOLITIONAL<br>BaseForm.POTENTIAL<br>BaseForm.IMPERATIVE<br>BaseForm.PROVISIONAL<br>BaseForm.CAUSATIVE<br>BaseForm.PASSIVE | Formality, Polarity |

If you prefer the more rigorous earlier version of calling individual methods for each form, you can still use that like this.
```python
from japanese_verb_conjugator_v2 import Formality, Polarity, Tense, VerbClass, JapaneseVerbFormGenerator as jvfg

jvfg.generate_plain_form("飲む", VerbClass.GODAN, Tense.NONPAST, Polarity.POSITIVE) # returns '飲む'
jvfg.generate_plain_form("飲む", VerbClass.GODAN, Tense.NONPAST, Polarity.NEGATIVE) # returns '飲まない'
```

The library will try to help validate the correctness of the verb by checking for invalid verb lengths, non-Japanese characters, and invalid verb endings. **Limitation**: this library cannot identify Chinese words with valid Japanese particle endings or nonexistent Japanese verbs.

### Copula

Generation of copula forms works similarly:

```python
from japanese_verb_conjugator_v2 import generate_japanese_copula_by_str

generate_japanese_copula_by_str("pla") # returns 'だ'
generate_japanese_copula_by_str("pres", "pol", "neg") # returns 'ではないでしょう'
```

The first argument is required and has to be one of the strings:

```python
CopulaForm.PLAIN = "pla"
CopulaForm.POLITE = "pol"
CopulaForm.TE = "te"
CopulaForm.CONDITIONAL = "cond"
CopulaForm.TARA = "tara"
CopulaForm.PRESUMPTIVE = "pres"
```

The following strings can be of the corresponding arguments

| CopulaForm | Possible arguments |
| - | - |
| CopulaForm.PLAIN<br>CopulaForm.POLITE | Tense, Polarity |
| CopulaForm.TE<br>CopulaForm.TARA | Formality |
| CopulaForm.CONDITIONAL | |
| CopulaForm.PRESUMPTIVE | Formality, Polarity |

The original way of calling individual methods also remains.

```python 
from japanese_verb_conjugator_v2 import Formality, Polarity, Tense, VerbClass, JapaneseVerbFormGenerator as jvfg

jvfg.copula.generate_plain_form(Tense.NONPAST, Polarity.POSITIVE) # returns 'だ'
jvfg.copula.generate_presumptive_form(Formality.POLITE, Polarity.NEGATIVE) # returns 'ではないでしょう'
```


## Tests
The coverage package is used to run the unittests. The configuration is defined in `.coveragerc`
To run the tests, first install the testing requirements

```bash
poetry install --with test
```

### Run tests
You can run the tests like this

```bash
poetry run coverage run -m unittest
```

#### View coverage report
After running the tests with coverage you can show the coverage report like this

```bash
poetry run coverage report
```

Alternatively you can generate an html representation like this

```bash
poetry run coverage html
```

You can open the html in a browser like this

```bash
open htmlcov/index.html
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project is licensed under the [BSD](https://choosealicense.com/licenses/bsd/) license.