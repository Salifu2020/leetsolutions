class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letter = letters.copy()
        letters.append(target)

        return letters[letters.index(target) + 1] if target in letter else letter[0]
        