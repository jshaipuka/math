def solve2(golden_bar_count, max_weight, golden_bar_weights, call = False, saved = dict()):
  if not call:
    call = True
    saved = dict()
  if (max_weight, golden_bar_count) in saved:
    pass
  elif golden_bar_count == 0:
    saved[(max_weight, golden_bar_count)] = 0
  elif max_weight == 0:
    saved[(max_weight, golden_bar_count)] = 0
  elif golden_bar_weights[golden_bar_count-1] > max_weight:
    saved[(max_weight, golden_bar_count)] = solve2(golden_bar_count-1,max_weight, golden_bar_weights, call, saved)
  else:
    cur_element_weight = golden_bar_weights[golden_bar_count-1]

    # cennostj menjatj zdesj
    saved[(max_weight, golden_bar_count)] = max(solve2(golden_bar_count-1, max_weight, golden_bar_weights, call, saved), solve2(golden_bar_count-1, max_weight - cur_element_weight, golden_bar_weights, call, saved) + cur_element_weight)
  return saved[(max_weight, golden_bar_count)]

N, M = [int(el) for el in input().split()]
golden_bar_weights = [int(el) for el in input().split()]
golden_bar_weights = list(map(int, input().split()))
print(solve2(N, M, golden_bar_weights))



print(solve2(2, 3195, [38, 41]), ' Should be 79')
print(solve2(5, 15, [1, 1, 2, 4, 12]), ' Should be 15')
print(solve2(4, 15, [5, 5, 5, 6]), ' Should be 15')


#O(n*min(W, сумма weights)/min(weights))
#O(n*W)