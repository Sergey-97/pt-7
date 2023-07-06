# 3) Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.

# Для сравнения первого и второго измерений можно воспользоваться парным t-тестом.
# Для этого можно использовать функцию ttest_rel из библиотеки scipy.stats.
from scipy.stats import ttest_rel
before = [150, 160, 165, 145, 155]
after_10min = [140, 155, 150, 130, 135]

statistic, p_value = ttest_rel(before, after_10min)
print("Статистика:", statistic)
print("p-значение:", p_value)
