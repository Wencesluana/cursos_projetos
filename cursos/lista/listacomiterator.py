class MyList:
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, value):
        self._data[self._index] = value
        self._index += 1

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        return self._data[index]
    
    def __inter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
    
        value = self._data[self._next_index]
        self._next_index += 1
        return value

if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Luiz')
    for item in lista:
        print(item)
    print('---')
    for item in lista:
        print(item)
