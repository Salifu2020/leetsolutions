class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        my_dict = dict(zip(indices, s))
        my_dict = sorted(my_dict.items(), key=lambda x: x[0])
        lst = []
        for k, v in my_dict:
            lst.insert(k, v)



        return ''.join(lst)