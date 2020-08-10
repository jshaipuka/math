# Дано N золотых слитков массой m1, …, mN. Ими наполняют рюкзак, который выдерживает вес не более M. Какую наибольшую массу золота можно унести в таком рюкзаке?

# Входные данные
# В первой строке вводится натуральное число N, не превышающее 100 и натуральное число M, не превышающее 10000.

# Во второй строке вводятся N натуральных чисел mi, не превышающих 100.

# Выходные данные
# Выведите одно целое число - наибольшую возможную массу золота, которую можно унести в данном рюкзаке.


def solve(golden_bar_count, max_weight, golden_bar_weights):
  most_gold_weight = 0

  golden_bar_weights.sort(reverse=True)

  for weight in golden_bar_weights:
    if most_gold_weight == max_weight:
      break

    if weight < max_weight and most_gold_weight < max_weight:
      most_gold_weight += weight

  return most_gold_weight


print(solve(2, 3195, [38, 41]), ' Should be 79')
print(solve(5, 15, [1, 1, 2, 4, 12]), ' Should be 15')
print(solve(4, 15, [5, 5, 5, 6]), ' Should be 15')


def solve(golden_bar_count, max_weight, golden_bar_weights):
  most_gold_weight = 0

  bag_slots = [0] * golden_bar_count

  for i in range(golden_bar_count):
    for weight in golden_bar_weights:
      if bag_slots[i] + weight <= max_weight:
        bag_slots[i] = bag_slots[i] + weight

  most_gold_weight = max(bag_slots)
  return most_gold_weight




print(solve2(2, 3195, [38, 41]), ' Should be 79')
print(solve2(5, 15, [1, 1, 2, 4, 12]), ' Should be 15')
print(solve2(4, 15, [5, 5, 5, 6]), ' Should be 15')
