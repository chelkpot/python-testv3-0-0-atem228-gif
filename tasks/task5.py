# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    n = int(input().strip())
    n %= 24 * 3600
    h = n // 3600
    m = (n % 3600) // 60
    s = n % 60
    print(f"{h}:{m:02d}:{s:02d}")
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()