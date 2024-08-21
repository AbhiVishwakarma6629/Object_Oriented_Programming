"""
two Strings are a good pair if the letters in them are same
ex :- list = ["Good", "God", "yarn", "bca", "abcd"]
good, god are good pairs bcoz -> g o d is in both strings
bca, abcd are good pairs bcoz -> b c a is in both strings
"""
from collections import defaultdict


class Cut:
    def count_good_pairs(self, lst):
        char_set_count = defaultdict(int)
        for s in lst:
            char_set = tuple(sorted(set(s)))
            char_set_count[char_set] += 1
        num_pairs = 0
        for count in char_set_count.values():
            if count > 1:
                num_pairs += count * (count - 1) // 2

        return num_pairs
obj1 = Cut()
print(obj1.count_good_pairs(["good", "god", "yarn", "bac", "aabc"]))


