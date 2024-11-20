def beauty_degree(n, colors):
    current_min = 1
    segment_count = 0
    segment_min = float('inf')

    for color in colors:
        segment_min = min(segment_min, color)

        if segment_min == current_min:
            segment_count += 1
            current_min += 1
            segment_min = float('inf')
    if current_min - 1 == segment_count:
        return segment_count
    else:
        return 0

n = int(input())
colors = list(map(int, input().split()))
result = beauty_degree(n, colors)

print(result)
