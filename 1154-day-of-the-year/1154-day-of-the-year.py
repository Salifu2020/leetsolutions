class Solution:
    def dayOfYear(self, date: str) -> int:
        str_date = date.split('-')

        months = {
            '01': 31,
            '02': 28,
            '03': 31,
            '04': 30,
            '05': 31,
            '06': 30,
            '07': 31,
            '08': 31,
            '09': 30,
            '10': 31,
            '11': 30,
            '12': 31,
        }
        if int(str_date[0]) % 4 == 0 and int(str_date[0]) % 100 != 0:
            months['02'] += 1
        elif int(str_date[0]) % 400 == 0 and int(str_date[0]) % 100 == 0:
            months['02'] += 1

        lst = [keys for keys in months.keys()]

        final_list = []
        for month in lst:
            if month < str_date[1]:
                final_list.append(month)

        total = 0
        for m in final_list:
            total += months[m]

        return total + int(str_date[2])

