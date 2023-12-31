# 5) Заявляется, что партия изготавливается со средним арифметическим 2, 5 см.
# Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения.
# Объем выборки 10, уровень статистической значимости 5 %

#     2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

# Для проверки гипотезы о среднем арифметическом можно воспользоваться одновыборочным t-тестом.
# Для этого можно использовать функцию ttest_1samp из библиотеки scipy.stats.

from scipy.stats import ttest_1samp

samples = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
mean_hypothesis = 2.5
statistic, p_value = ttest_1samp(samples, mean_hypothesis)
print("Статистика:", statistic)
print("p-значение:", p_value)
