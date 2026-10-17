import timeit
import random

from merge_sort import merge_sort
from insertion_sort import insertion_sort

if __name__ == "__main__":
    data_small = [random.randint(0, 100) for _ in range(100)]
    data_medium = [random.randint(0, 1_000) for _ in range(1_000)]
    data_large = [random.randint(0, 10_000) for _ in range(10_000)]
    
    time_small_merge = timeit.timeit(lambda: merge_sort(data_small), number=10)
    time_small_insertion = timeit.timeit(lambda: insertion_sort(data_small), number=10)
    time_small_tim = timeit.timeit(lambda: sorted(data_small), number=10)
    time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium), number=10)
    time_medium_insertion = timeit.timeit(lambda: insertion_sort(data_medium), number=10)
    time_medium_tim = timeit.timeit(lambda: sorted(data_medium), number=10)
    time_large_merge = timeit.timeit(lambda: merge_sort(data_large), number=10)
    time_large_insertion = timeit.timeit(lambda: insertion_sort(data_large), number=10)
    time_large_tim = timeit.timeit(lambda: sorted(data_large), number=10)

    print(f"{'Algorithm': <20} {'Small': <10} {'Medium': <10} {'Large': <10}")
    print(f"{ 'Merge Sort': <20} {time_small_merge: <10.6f} {time_medium_merge: <10.6f} {time_large_merge: <10.6f}")
    print(f"{ 'Insertion Sort': <20} {time_small_insertion: <10.6f} {time_medium_insertion: <10.6f} {time_large_insertion: <10.6f}")
    print(f"{ 'Timsort': <20} {time_small_tim: <10.6f} {time_medium_tim: <10.6f} {time_large_tim: <10.6f}")
