def palindrome(word):
    """Return True if word reads the same forwards and backwards."""
    text = ''.join(c.lower() for c in word if c.isalpha())
    return text == text[::-1]


def pangram(word):
    """Return True if word contains every letter of the alphabet."""
    text = set(c.lower() for c in word if c.isalpha())
    return len(text) == 26


def tautogram(word):
    """Return True if every word starts with the same letter."""
    words = word.lower().split()

    if not words:
        return False

    first_letter = words[0][0]
    return all(w[0] == first_letter for w in words)


def isogram(word):
    """Return True if no letter occurs more than once."""
    letters = [c.lower() for c in word if c.isalpha()]
    return len(letters) == len(set(letters))


def abedecerian(word):
    """Return True if the letters appear in alphabetical order."""
    letters = [c.lower() for c in word if c.isalpha()]
    return letters == sorted(letters)


def dobloon(word):
    """Return True if every letter occurs exactly twice."""
    letters = [c.lower() for c in word if c.isalpha()]
    counts = {}

    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1

    return bool(letters) and all(count == 2 for count in counts.values())

