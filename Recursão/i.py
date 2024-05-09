def func(n):
    if (n <= 0):
        return # não faz nada
    print(n)
    func(n-1)

func(1.5)