# The Fibonacci Sequence is the series of numbers:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# The next number is found by adding up the two numbers before it.

# Написать рекурсивную функцию подсчета числа Фибоначчи, чтобы можно было посчитать 60ое число за 1 секунду

import time

def fibonacci_sequence(previous, current, count, until):
  if count == until:
    return current
  elif current == 0 and previous == 0:
    return fibonacci_sequence(0, 1, count + 1, until)
  elif current == 1 and previous == 0:
    return fibonacci_sequence(1, 1, count + 1, until)
  else:
    return fibonacci_sequence(current, previous + current, count + 1, until)

def generate_fibonacci_sequence(until):
  num = fibonacci_sequence(0, 0, 1, until) if until > 0 else 0

  print('Fibonacci number at position ', until, ' is ', num)


start_time = time.time()

generate_fibonacci_sequence(60)

print('--- %s seconds ---' % (time.time() - start_time))

# Fibonacci number at position  60  is  956722026041
# --- 0.0034837722778320312 seconds ---
