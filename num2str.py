

class Number(object):
    def __init__(self, number, language="En"):
        self.number = number
        self.language = language

    def num2str(self):
        language_map = {"En": self.num2en}
        return language_map.get(self.language, "En")()

    def num2en(self):
        num_map = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                   9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
                   16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
                   40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",90: "ninety", 100: "hundred",
                   1000: "thousand", 1000000: "million", 1000000000: "billion", 1000000000000: "trillion"}

        num = self.split_number(str(self.number))
        phrase = []
        for i, x in enumerate(num):
            if phrase:
                if phrase[-1] == "and" and x > 100:
                    del phrase[-1]
                if num[i - 1] > 100 and all(n < 100 for n in num[i:]):
                    phrase.append("and")

            phrase.append(num_map.get(x, "XXX"))
            if x == 100 and i + 1 != len(num):
                phrase.append("and")
        return " ".join(phrase)

    @staticmethod
    def split_number(num):
        split_num = []

        for i in range(len(num)):
            ii = len(num) - (i + 1)

            if ii % 3 == 0 and i > 0:
                sub_num = int(num[i - 1: i + 1])
                if sub_num in range(10, 20):
                    del split_num[-1]
                    split_num.append(sub_num)
                    if ii > 0:
                        split_num.append(10 ** ii)
                    continue

            powered_num = int(num[i]) * 10 ** (ii % 3)
            if powered_num >= 100 and powered_num / 100 < 10:
                split_num.append(int(powered_num / 100))
                split_num.append(100)
            elif powered_num != 0:
                split_num.append(powered_num)
            if ii % 3 == 0 and ii > 0:
                split_num.append(10 ** ii)
        print(split_num if split_num else [0])
        return split_num if split_num else [0]

    def __repr__(self):
        return self.num2str()


if __name__ == "__main__":
    while True:
        x = input("Enter a whole number:")
        try:
            print(Number(int(x)))
        except:
            print("Ending!")
            break

