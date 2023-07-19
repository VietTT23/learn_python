class Foo:
    __name = "Foo"

    def __getName(self):
        print(self.__name)

    def get(self):
        self.__getName()


# print(Foo().__name)  # error
# Foo().__getName()  # error
Foo().get()

# TÍNH KẾ THỪA


