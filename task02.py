# 2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

class A:
    def __init__(self):
        self.mas = []

    def append_element(self, element):
        self.mas.append(element)

    def get_element(self):
        out = self.mas[0]
        del self.mas[0]
        print out
        return out

    def print_list(self):
        print out
        type(self.mas)


a = A()
a.append_element(5)
a.append_element("a")
a.get_element()
a.get_element()
a.print_list()


