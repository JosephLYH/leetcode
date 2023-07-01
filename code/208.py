class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for letter in word:
            if letter not in trie:
                trie[letter] = {}
            trie = trie[letter]

        trie[""] = {}

    def search(self, word: str) -> bool:
        trie = self.trie
        for letter in word:
            if letter not in trie:
                return False
            trie = trie[letter]

        return "" in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for letter in prefix:
            if letter not in trie:
                return False
            trie = trie[letter]

        return True
