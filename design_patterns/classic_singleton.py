

class ClassicSingleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ClassicSingleton, cls).__new__(cls)
        return cls.instance


if __name__ == "__main__":
    singleton = ClassicSingleton()
    new_singleton = ClassicSingleton()

    print(singleton is new_singleton)

    singleton.singl_variable = "Singleton Variable"
    print(new_singleton.singl_variable)