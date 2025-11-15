# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    n = int(input().strip())
    count = 0
    for coin in (100, 20, 10, 5, 1):
        if n == 0:
            break
        take = n // coin
        count += take
        n -= take * coin
    print(count)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()