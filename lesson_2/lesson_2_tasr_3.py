def square(side):
    area = side * side
    # Если площадь не целое число, округляем вверх
    if area != int(area):
        area = int(area) + 1
    return area

# Пример использования
print(square(5.5))  # Ожидаемый результат: 31