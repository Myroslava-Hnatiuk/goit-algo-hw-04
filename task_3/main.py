import timeit
import random

from merge_sort import merge_sort
from insertion_sort import insertion_sort

if __name__ == "__main__":
    data_small = [random.randint(0, 1000) for _ in range(1_000)]
    data_medium = [random.randint(0, 10_000) for _ in range(10_000)]
    data_large = [random.randint(0, 100_000) for _ in range(100_000)]
    
    time_small_merge = timeit.timeit(lambda: merge_sort(data_small), number=10)
    time_small_insertion = timeit.timeit(lambda: insertion_sort(data_small), number=10)
    time_small_tim = timeit.timeit(lambda: sorted(data_small), number=10)
    time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium), number=10)
    time_medium_insertion = timeit.timeit(lambda: insertion_sort(data_medium), number=10)
    time_medium_tim = timeit.timeit(lambda: sorted(data_medium), number=10)
    time_large_merge = timeit.timeit(lambda: merge_sort(data_large), number=10)
    time_large_insertion = timeit.timeit(lambda: insertion_sort(data_large), number=10)
    time_large_tim = timeit.timeit(lambda: sorted(data_large), number=10)

    print(f"Algorithm\tSmall\tMedium\tLarge")
    print(f"Merge Sort\t{time_small_merge}\t{time_medium_merge}\t{time_large_merge}")
    print(f"Insertion Sort\t{time_small_insertion}\t{time_medium_insertion}\t{time_large_insertion}")
    print(f"Tim Sort\t{time_small_tim}\t{time_medium_tim}\t{time_large_tim}")
