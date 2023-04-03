"""Your task has been made easy, as the encryption key consists of three lower case characters.
Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes,
and the knowledge that the plain text must contain common English words, decrypt the message and find the sum
of the ASCII values in the original text."""
from string import ascii_lowercase as alphabet


def solve(filepath: str = "p059_cipher.txt") -> int:
    STOPWORDS = ["the", "be", "to", "and", "a", "of", "in", "that", "for", "not", "on"]
    with open(filepath, "r") as f:
        numbers = list(map(int, f.read().strip().split(",")))
    nb_letters = len(alphabet)
    text_len = len(numbers)
    candidates = []
    for i in range(nb_letters):
        for j in range(nb_letters):
            for k in range(nb_letters):
                pat = ord(alphabet[i]), ord(alphabet[j]), ord(alphabet[k])
                # apply XOR
                decrypted = "".join(
                    map(chr, [pat[c % 3] ^ numbers[c] for c in range(text_len)])
                )
                nb_stopwords_in = sum(w in decrypted.lower() for w in STOPWORDS)
                if nb_stopwords_in:
                    candidates.append((nb_stopwords_in, decrypted, pat))
    candidates.sort(reverse=True)
    if not candidates:
        raise Exception("No clear text found, review the list of stopwords")
    best = candidates[0][1]  # venturing a guess that it's the one with most matches
    print(best)
    ans = sum(map(ord, best))
    print(ans)
    return ans


if __name__ == "__main__":
    solve()
