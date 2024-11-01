import heapq


def merge_k_lists(lists):
    # Мін-купа для зберігання поточних мінімальних елементів із кожного списку
    min_heap = []

    # Ініціалізуємо купу першим елементом з кожного списку
    for i, lst in enumerate(lists):
        if lst:  # Перевірка, що список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента в списку)

    # Результуючий список
    result = []

    # Поки купа не порожня
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        result.append(value)  # Додаємо найменший елемент до результату

        # Додаємо наступний елемент із того ж списку, якщо він існує
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return result


# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)