#StopIteration
#Stop after 20 th  iterations ?


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
      if self.a <= 20:
        x = self.a
        self.a += 1
        return x
      else:
          raise StopIteration

myobject = MyNumbers()
myiter = iter(myobject)

for x in myiter:
    print(x)
