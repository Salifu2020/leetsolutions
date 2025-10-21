class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        new_para = re.findall(r"\w+|[^\w\s]", paragraph)
        char_to_be_removed = "'!,.?`:;"

        lst = [word.lower() for word in new_para if word not in char_to_be_removed]

        final = [words for words in lst if words not in banned]

        counts = Counter(final)

        return max(counts, key=counts.get)

        