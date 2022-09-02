try:
    print("-----------------------------------------------------------------------------------------------\n"
          "Программа находит позицию элемента в отсортированном списке, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.\n"
          "-----------------------------------------------------------------------------------------------\n")
    some_list = list(map(int, input("Что бы создать список, введите диджиты через пробел:\n").split())) #водим, разбиваем на список
    def buble(array): #Сортировка пузырьком
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array
    sor_list = buble(some_list)
    digit = int(input("А так же введите еще один диджит:\n")) #водим нужное значение
    if digit <= sor_list[0]: #проверяем, что число не меньше минимального, потому что тогда не выполнить условия
        print("Диджит меньше минимального в списке, либо равен ему - не годится")
        digit = int(input("Попробуйте ввести другой диджит:\n"))
except ValueError: #пишем понятное, дружелюбное пояснение, если ввод был некоректный
    print("Ты вводишь не диджиты, друг!")
else:
    def binary_search(array, element, left, right):
        if element in array: #стандартное поведение, если элемент есть в списке
            if left > right:
                return False
            middle = (right + left) // 2
            if array[middle] == element:
                return middle
            elif element < array[middle]:
                return binary_search(array, element, left, middle - 1)
            else:
                return binary_search(array, element, middle + 1, right)

    def find_closest(array, element, left, right):
            if min(array, key=lambda x: abs(x - element)) <= element: #ищем  ближайший элемент в списке, если он меньше или равен, значит он удовлетворяет нашим условиям
                return binary_search(array, min(array, key=lambda x: abs(x - element)), left, right)
            else: #если нет, значит будем искать ближайший меньший, удаляя все ближайшие бОльшие
                copy_array = list(array) #делаем копию, что бы не портить входные данные, кроме того, делаем изменяемый тип, даже если был неизменяемый
                while min(copy_array, key=lambda x: abs(x - element)) > element:
                    copy_array.remove(min(copy_array, key=lambda x: abs(x - element))) #удаляем из списка элементы, ближайшие по значению, но больше искомого
                return binary_search(copy_array, min(copy_array, key=lambda x: abs(x - element)),0, right=len(copy_array)) #взвращаем функцию, где ближайший по значению элемент будет меньше искомого
    num_index = find_closest(sor_list, digit, 0, len(sor_list))
    a = sor_list[num_index]
    k = 0
    try:
        while sor_list[num_index + k] == a:
            k += 1
        print(list(enumerate(sor_list)))
        print("Сдвиг по индекссам:", k - 1)
        print(f"---------------------\n"
              f"Номер позиции элемента (c 0):  {num_index}\n")

    except:
        k = 0
        print(list(enumerate(sor_list)))
        print("Сдвиг по индекссам:", k - 1)
        print(f"---------------------\n"
              f"Номер позиции элемента (c 0):  {num_index}\n")



