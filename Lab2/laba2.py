def calculate_rectangle_area(length, width):
  area = length * width
  return area

длина = float(input("Введите длину прямоугольника: "))
ширина = float(input("Введите ширину прямоугольника: "))

площадь = calculate_rectangle_area(длина, ширина)
print(f"Площадь прямоугольника: {площадь}")