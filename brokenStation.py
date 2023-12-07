def bsp_value(L, m):
    def max_min_distance(low, high, L, m):
        while low < high:
            mid = (low + high) // 2
            if is_possible(mid, L, m):
                low = mid + 1
            else:
                high = mid
        return low - 1

    def is_possible(distance, L, m):
        count, last = 0, L[0]
        for i in range(1, len(L)):
            if L[i] - last < distance:
                count += 1
                if count > m:
                    return False
            else:
                last = L[i]
        return True
    return max_min_distance(0, L[-1] - L[0] + 1, L, m)

def bsp_solution(L, m):
    max_distance = bsp_value(L, m)
    solution, last = [L[0]], L[0]
    
    for i in range(1, len(L)):
        if L[i] - last >= max_distance:
            solution.append(L[i])
            last = L[i]
        elif len(L) - i - 1 <= m:
            solution.extend(L[i + 1:])
            break
        else:
            m -= 1

    return solution

L = [2, 4, 6, 7, 10, 14]
m = 2

bsp_value_result = bsp_value(L, m)
bsp_solution_result = bsp_solution(L, m)

print(bsp_value_result, bsp_solution_result)

