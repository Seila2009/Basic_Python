class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in a]) for a in self.my_list]))

    def __add__(self, other):
        for val in range(len(self.my_list)):
            for val_2 in range(len(other.my_list[val])):
                self.my_list[val][val_2] = self.my_list[val][val_2] + other.my_list[val][val_2]
        return Matrix.__str__(self)


matrix = Matrix([[0, 1, 2], [2, 1, 0], [0, 2, 1], [1, 1, 0]])
new_matrix = Matrix([[5, 3, 15], [6, 6, 36], [7, 8, 48], [5, 5, 25]])
print(new_matrix.__add__(new_matrix))