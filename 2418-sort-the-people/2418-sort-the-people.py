class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_dict = dict(zip(heights, names))
        sorted_names = []

        my_name_vals = list(name_dict.keys())
        my_name_vals.sort()
        name_vals = my_name_vals[::-1]

        for height in name_vals:
            for key, value in name_dict.items():
                if key == height:
                    sorted_names.append(value)

        return sorted_names
        