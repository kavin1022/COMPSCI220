"""
Pinghang Fan, pfan450. 748224962
avl_trees.py
"""
import sys

def find_popular(n, k, adj_list):
    pop_dict = dict()
    for num in range(n):
        pop_dict[num] = 0
    for array in adj_list:
        for j in array:
                pop_dict[j] += 1
    pop_dict = {k: v for k, v in sorted(pop_dict.items(), key=lambda item: item[1])}
    pop_list = [[k, v] for k, v in pop_dict.items()]
    pop_list.reverse()

    

    i = 0
    while i < len(pop_list) - 1:
        curr = pop_list[i][1]
        next = pop_list[i+1][1]

        temp_list = list()
        inner_count = 1
        while next == curr:
            if len(temp_list) == 0:
                temp_list.append(pop_list[i])
            temp_list.append(pop_list[i+ inner_count])
            curr = next
            inner_count = inner_count + 1
            if i + inner_count == len(pop_list):
                break
            next = pop_list[i+inner_count][1]

        if inner_count != 1:
            temp_list.sort()
            pop_list[i:i + inner_count] = temp_list
            i = i + inner_count
        if inner_count == 1:
            i = i + 1

    return pop_list[k-1][0]

def main():
    total_list = list()
    adj_list = list()
    """Getting inputs"""
    for line in sys.stdin:
        if line == None or line == "None\n":
            break
        total_list.append([int(n) for n in line.rstrip("\n").split()])
    
    
    index = 0
    """Iterating through inputs by n nodes"""
    while index < len(total_list) - 1:
        node_count = int(total_list[index][0])
        
        adj_list = total_list[index: index + node_count + 1]
        k = int(adj_list[0][1])
        pop_dict = find_popular(node_count, k, adj_list[1:])
        print(pop_dict)

        index = index + node_count + 1

main()