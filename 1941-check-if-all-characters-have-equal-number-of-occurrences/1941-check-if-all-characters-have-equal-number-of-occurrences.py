class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        lst = list(s)

        counts = Counter(lst)

        freq_ch = []
        for c in counts:
            freq_ch.append(counts[c])

        return len(set(freq_ch)) == 1
        