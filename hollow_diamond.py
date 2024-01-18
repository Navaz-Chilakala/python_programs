n = int(input())
x = n
for i in range(n):
  a = '*' * x
  b = ' ' * (2 * i)
  print(a + b + a)
  x = x - 1
for j in range(n):
  c = '*' * (((2 * j) + 2) // 2)
  d = ' ' * (2 * n - (2 * j + 2))
  print(c + d + c)
