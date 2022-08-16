# 2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

class A:
    def __init__(self):
        self.mas = []

    def append_element(self, el):
        self.mas.append(el)

    def get_element(self):
        if self.mas: out = self.mas.pop(0)
        else: out = None
        print out
        return out

    def print_list(self):
        print self.mas


a = A()
a.append_element(5)
a.append_element("a")
a.get_element()
a.get_element()
a.print_list()


