# Импортируем OneHotEncoder
from sklearn.preprocessing import OneHotEncoder

# Создаем экземпляр OneHotEncoder с параметром sparse=False, чтобы получить массив numpy вместо разреженной матрицы
enc = OneHotEncoder(sparse=False)

# Обучаем OneHotEncoder на столбце whoAmI
enc.fit(data[['whoAmI']])

# Преобразуем столбец whoAmI в one hot вид
one_hot = enc.transform(data[['whoAmI']])

# Создаем новый DataFrame с one hot столбцами
data_one_hot = pd.DataFrame(one_hot, columns=enc.get_feature_names(['whoAmI']))

# Выводим первые пять строк нового DataFrame
data_one_hot.head()
