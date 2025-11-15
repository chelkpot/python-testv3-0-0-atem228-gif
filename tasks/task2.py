# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    n = int(input().strip())
    n %= 1440
    h = n // 60
    m = n % 60
    print(h, m)
   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()