import random

def modulo(base, exponent, mod):
  x = 1
  y = base
  while exponent > 0:
    if exponent % 2 == 1:
      x = (x * y) % mod
    y = (y * y) % mod
    exponent //= 2
  return x % mod

def calculate_jacobian(a, n):
  """
  Calculates the Jacobi symbol of a and n.
  """
  if a == 0:
    return 0
  ans = 1
  if a < 0:
    a = -a
    if n % 4 == 3:
      ans = -ans
  if a == 1:
    return ans
  while a:
    if a < 0:
      a = -a
      if n % 4 == 3:
        ans = -ans
    while a % 2 == 0:
      a //= 2
      if n % 8 == 3 or n % 8 == 5:
        ans = -ans
    a, n = n, a
    if a % 4 == 3 and n % 4 == 3:
      ans = -ans
    a %= n
    if a > n // 2:
      a -= n
  if n == 1:
    return ans
  return 0

def solovay_strassen(p, iterations):

  if p < 2:
    return False
  if p != 2 and p % 2 == 0:
    return False
  for _ in range(iterations):
    a = random.randrange(1, p)
    jacobian = (p + calculate_jacobian(a, p)) % p
    mod = modulo(a, (p - 1) // 2, p)
    if jacobian == 0 or mod != jacobian:
      return False
  return True

# Get input from the user
iterations = int(input("Enter the number of iterations: "))
num1 = int(input("Enter the first number to test: "))
num2 = int(input("Enter the second number to test: "))


if solovay_strassen(num1, iterations):
  print(num1, "is prime")
else:
  print(num1, "is composite")

if solovay_strassen(num2, iterations):
  print(num2, "is prime")
else:
  print(num2, "is composite")