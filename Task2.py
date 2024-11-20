def min_distance_for_min_cost(n, m, costs):
    indexed_costs = [(costs[i], i) for i in range(n)]

    indexed_costs.sort()

    selected = indexed_costs[:m]


    min_index = selected[0][1]
    max_index = selected[-1][1]
    min_distance = max_index - min_index + 1

    return min_distance

n, m = map(int, input().split())
costs = list(map(int, input().split()))

result = min_distance_for_min_cost(n, m, costs)

print(result)