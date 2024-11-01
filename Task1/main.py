import heapq

def min_connection_cost(cables):
    # Ініціалізуємо мін-купу зі списком кабелів
    heapq.heapify(cables)
    total_cost = 0

    # Поки в купі більше ніж один елемент
    while len(cables) > 1:
        # Виймаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Обчислюємо вартість з'єднання і додаємо до загальної вартості
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальна вартість об'єднання кабелів:", min_connection_cost(cables))