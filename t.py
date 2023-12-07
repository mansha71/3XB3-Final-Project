def find_min_max_gap(L):
    min_gap = 1000000
    for i in range(len(L)-1):
        diff = abs(L[i+1]-L[i])
        if diff<min_gap:
            min_gap = diff
    return min_gap

def bsp_value(L, m):
    min_gap = 1000000
    min_list= []
    for i in L:
        temp = [100000000]
        for j in L:
        # List of values to be removed
            values_to_remove = [i,j]
            # New list with values removed
            new_list = [item for item in L if item not in values_to_remove]
            gap = find_min_max_gap(new_list)
            #print(gap)
            
            if min(temp) > min_gap:
                #print("ff")
                min_gap = gap
                temp.append(min_gap)
                min_list = new_list
            
    return min_gap


def bsp_solution(L, m):
    max_gap = bsp_value(L, m)

    # Construct the solution
    solution = [L[0]]
    last_added = L[0]
    for i in range(1, len(L)):
        if L[i] - last_added > max_gap or len(L) - i <= m:
            solution.append(L[i])
            last_added = L[i]
            m -= 1
    return solution

# Test the functions
print(bsp_value([2, 4, 6, 7, 10, 14], 2))  # Output: 4
print(bsp_solution([2, 4, 6, 7, 10, 14], 2))  # Output: [2, 6, 10, 14]
