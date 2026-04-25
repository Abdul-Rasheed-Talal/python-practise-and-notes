def outerFunc(num):
    def innerFunc(x):
        return x**num
    return innerFunc

f = outerFunc(3)
g = outerFunc(4)

print(f(3))
print(g(3))