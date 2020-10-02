class Pizza:
    """Класс который описывает экземпляр пиццы(в одном параметре - название,описание,цена)
    Пиццу можно заказать - заказать в список
    пиццу можно указать из списка покупок
    и можно оформить заказ, указав сумму клиента"""
    pizza_30sm = {"Куриная":380,"Шашлычная":290,"Фрикасе":390}
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def pizza_list(self):
        self.kind = []


    def order(self,pizza):
        self.kind.append(pizza)

    def __repr__(self):
        return f'Пицца {self.name}'

    def delete(self):
        self.name.pop()


    def to_price(self,money):
        if money > self.price:
            result = money - self.price
            return result + "Заказ принят"
        return "Недостаточно средств"


pizza = Pizza("Шашлычная",450)
print(pizza.order())
print(pizza.pizza_list())
print(pizza.to_price(450))
