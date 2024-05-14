

class Product:

    def __init__(self, product_id, name, description, image, price, category, reviews, available_item_count, account):

        self.__product_id = product_id
        self.__name = name
        self.__description = description
        self.__image = image
        self.__price = price
        self.__category = category  # Refers to an instance of the ProductCategory class
        self.__reviews = reviews  # Refers to the list of the ProductReview instances
        self.__available_item_count = available_item_count
        self.__account = account  # Refers to an instance of the Account class

    def get_available_count(self):
        pass

    def update_available_count(self):
        pass

    def update_price(self):
        pass


class ProductCategory:

    def __init__(self, name, description, products):
        self.__name = name
        self.__description = description
        self.__products = products # Refers to the list of products


class ProductReview:

    def __init__(self, rating, review, image, user):
        self.__rating = rating
        self.__review = review
        self.__image = image
        self.__user = user  # Refers to an instance of the AuthenticatedUser class