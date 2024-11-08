def pair_numbers(n):
    result = []

    for i in range(1, n // 2 + 1):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result.append(f"{i}{j}")

    return ''.join(result)


n = int(input())
print(pair_numbers(n))