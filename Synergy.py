
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def printList(my_list):
    numbers = list(my_list)
    if len(numbers) != 0:
        print(numbers[0])
        del numbers[0]
        printList(numbers)
    else:
        print('Конец списка')

printList(my_list)