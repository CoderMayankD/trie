import data_warehouse

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end_of_word = True

#     def search_prefix(self, prefix):
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return []
#             node = node.children[char]
#         return self._words_with_prefix(prefix, node)

#     def _words_with_prefix(self, prefix, node):
#         words = []
#         if node.is_end_of_word:
#             words.append(prefix)
#         for char, next_node in node.children.items():
#             words.extend(self._words_with_prefix(prefix + char, next_node))
#         return words

# # Initialize the Trie with some words
# trie = Trie()

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._words_with_prefix(prefix, node)

    def _words_with_prefix(self, prefix, node):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            words.extend(self._words_with_prefix(prefix + char, next_node))
        return words

# Initialize the Trie with some words
trie = Trie()

combined_data=tuple(data_warehouse.search_list+data_warehouse.full_list)
for word in combined_data:
    trie.insert(word)
