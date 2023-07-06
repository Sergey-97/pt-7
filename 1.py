# 1)  Даны две  независимые выборки. Не соблюдается условие нормальности
#     x1  380, 420, 290
#     y1 140, 360, 200, 900
#     Сделайте вывод по результатам, полученным с помощью функции


# Для проверки наличия различий между выборками можно воспользоваться непараметрическим критерием Манна-Уитни.
# Для этого можно использовать функцию mannwhitneyu из библиотеки scipy.stats.(необходимо установить модуль)

from scipy.stats import mannwhitneyu

x1 = [380, 420, 290]
y1 = [140, 360, 200, 900]

statistic, p_value = mannwhitneyu(x1, y1)
print("Статистика:", statistic)
print("p-значение:", p_value)