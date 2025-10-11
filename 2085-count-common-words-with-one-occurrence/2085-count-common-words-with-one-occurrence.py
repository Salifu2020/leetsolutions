class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter = Counter(words1)
        counts = Counter(words2)
        lst1 = []
        for item in range(len(words1)):
            if counter[words1[item]] == 1:
                lst1.append(words1[item])

        lst2 = []
        for ch in range(len(words2)):
            if counts[words2[ch]] == 1:
                lst2.append(words2[ch])

        final_ans = set(lst1).intersection(set(lst2))

        return len(final_ans)
        