"Count a number of planks"


class Cut:
    def wood_fencing(self, woods):
        longest_plank = max(woods)
        count_longest_plank = 0
        for i in woods:
            if i == longest_plank:
                count_longest_plank += 1
        woods.sort()
        woods = woods[:longest_plank]
        dict_plank = {}
        count_other = 0
        for i, wood in enumerate(woods):
            compliment = longest_plank - wood
            if compliment in dict_plank:
                count_other += 1
            dict_plank[wood] = i

        return count_longest_plank + count_other


obj1 = Cut()
print(obj1.wood_fencing([8, 13, 7, 13, 5, 13, 4, 13, 6, 13]))
