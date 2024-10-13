#a
def sequence_a(n):
  if n == 1:
    return 1
  else:
    return sequence_a(n - 1) + 1

#b
def sequence_b(n):
  if n == 1:
    return 0
  else:
    return sequence_b(n - 1) + 5

#c
def sequence_c(n):
  if n == 1:
    return 1
  else:
    return sequence_c(n - 1)

#d
def sequence_d(n):
  if n == 1:
    return 1
  else:
    return -sequence_d(n - 1)

#e
def sequence_e(n):
  if n == 1:
    return 1
  else:
    return -sequence_e(n - 1) + 2 * n - 1

#f
def sequence_f(n):
  if n == 1:
    return 2
  else:
    return 2 * sequence_f(n - 1)

#g
def sequence_g(n):
  if n == 1:
    return 2
  else:
    return sequence_g(n - 1) ** 2

#h
def sequence_h(n):
  return (n - 1) % 4

#i
def sequence_i(n):
  if n == 1:
    return 1
  else:
    return (2 * n - 1) * sequence_i(n - 1)

print(sequence_a(5))