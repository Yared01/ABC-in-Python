import random as rand
import source as flower
class Quick(flower.Nectar):
    def __init__(self, data):
        self.src = data

    def psort2(self, start, end):
        pivot_value = self.src[int(round(start + end)/2)].get_probability()
        left_mark = start
        right_mark = end

        while left_mark <= right_mark:
            while self.src[left_mark].get_probability() < pivot_value:
                left_mark += 1

            while self.src[right_mark].get_probability() > pivot_value:
                right_mark -= 1

            if (left_mark <= right_mark):
                temp = self.src[left_mark]
                self.src[left_mark] = self.src[right_mark]
                self.src[right_mark] = temp
                right_mark -= 1
                left_mark += 1

        if start < right_mark:
            self.psort2(start, right_mark)

        if left_mark < end:
            self.psort2(left_mark, end)

        return self.src
