class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        max_element = 0
        for elem in input_list:
            if elem > max_element:
                max_element = elem
        return [max_element if elem > 0 else elem for elem in input_list]

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        def binary_search(start: int, end: int) -> int:
            if start > end:
                return -1
            middle = (start + end) // 2
            if input_list[middle] == query:
                return middle
            elif query < input_list[middle]:
                return binary_search(start, middle - 1)
            else:
                return binary_search(middle + 1, end)

        return binary_search(0, len(input_list) - 1)
