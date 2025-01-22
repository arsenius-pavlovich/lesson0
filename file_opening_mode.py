class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read().strip()

    def add(self, *products):
        existing_products = {}

        # Считываем текущие товары из файла
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    product_data = line.strip().split(', ')
                    key = (product_data[0], product_data[2])
                    if key not in existing_products:
                        existing_products[key] = float(product_data[1])
        except FileNotFoundError:
            pass

        # Сбор информации о новых продуктах для вывода
        messages = []

        # Обрабатываем добавление новых товаров
        with open(self.__file_name, 'a') as file:
            for product in products:
                key = (product.name, product.category)

                if key in existing_products:
                    existing_products[key] += product.weight
                    messages.append(
                        f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {existing_products[key]}')
                else:
                    existing_products[key] = product.weight
                    file.write(str(product) + '\n')

        # Сначала выводим продукты, затем сообщения
        print(self.get_products())
        for message in messages:
            print(message)


# Создаем объект магазина
s1 = Shop()

# Создаем несколько продуктов
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Добавляем продукты в магазин
s1.add(p1, p2, p3)
