![saikoro screenshot](https://github.com/SaptakS/saikoro/blob/main/saikorosrc/resources/screenshot.png?raw=true)
# Saikoro: Easy to use GUI for diceware passphrases

Saikoro is a desktop application catered towards making diceware passphrase generation easy and accessible for non-tech savvy users as well. It uses the python package [diceware](https://diceware.readthedocs.io/en/stable/) that is commonly used by people comfortable with command line interface to generate passphrase.

All the features use diceware directly. So Saikoro is kind of a GUI wrapper for the command line application.

## Developer Install

- `git clone https://github.com/SaptakS/saikoro.git`
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `python3 -m pip install -r requirements.txt`
- `./scripts/dev.sh`

## Is it secure?

Refer to the [section in diceware readme](https://github.com/ulif/diceware#is-it-secure) to learn more about it. This GUI uses the [random.SystemRandom](https://docs.python.org/3.4/library/random.html#random.SystemRandom) and currently doesn't support other forms of randomness like real dice.

## Options

- **No. of words**: One can specify the number of words one wants in the passphrase
- **No. of special characters**: One can specify the number of special characters in the passphrase. The special characters are selected randomly and placed in random locations
- **Delimiter**: One can separate the words using a delimiter. It is empty string by default. It can be space, "-", "_" or any other character
