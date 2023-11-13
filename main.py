def sequential_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return comparisons
    return comparisons


def binary_search(arr, target):
    comparisons = 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return comparisons


def interpolation_search(arr, target):
    comparisons = 0
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return comparisons


def main():
    # Чтение массива из файла
    with open("input.txt", "r") as file:
        arr = list(map(int, file.read().split()))

    n = len(arr)
    total_seq_comparisons = 0
    total_bin_comparisons = 0
    total_int_comparisons = 0

    # Поиск для каждого элемента от 1 до N
    for i in range(1, n+1):
        seq_comparisons = sequential_search(arr, i)
        bin_comparisons = binary_search(arr, i)
        int_comparisons = interpolation_search(arr, i)

        total_seq_comparisons += seq_comparisons
        total_bin_comparisons += bin_comparisons
        total_int_comparisons += int_comparisons

    # Вычисление среднего числа сравнений
    avg_seq_comparisons = total_seq_comparisons / n
    avg_bin_comparisons = total_bin_comparisons / n
    avg_int_comparisons = total_int_comparisons / n

    # Запись среднего числа сравнений в файл
    with open("output.txt", "w") as file:
        file.write(f"Среднее число сравнений для последовательного поиска: {avg_seq_comparisons}\n")
        file.write(f"Среднее число сравнений для двоичного поиска: {avg_bin_comparisons}\n")
        file.write(f"Среднее число сравнений для интерполяционного поиска: {avg_int_comparisons}\n")


if __name__ == '__main__':
    main()