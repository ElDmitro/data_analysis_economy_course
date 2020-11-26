def bin_search(asc_array, item):
    l, r = 0, len(asc_array)
    while (r - l) > 1:
        pivot = (l + r) // 2
        if asc_array[pivot] < item:
            l = pivot
        else:
            r = pivot
    return l


def get_basement(blocks_dists, bench_length):
    left_bound = bin_search(blocks_dists, bench_length / 2)
    left_value = blocks_dists[left_bound]
    if (bench_length / 2 - (left_value + 0.5)) < 0.5:
        return blocks_dists[left_bound:left_bound + 1]
    return blocks_dists[left_bound:left_bound + 2]


bench_length, nblocks = [int(value) for value in input().split()]
blocks_dists = [int(value) for value in input().split()]

print(*get_basement(blocks_dists, bench_length), sep=' ')
