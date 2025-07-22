elements = [1,1,0,0,1,0,1]
#get the count of switch happening from 0->1 and 1->0

def find_switch_count(elements):
    count_one = elements.count(1)
    count_zero = elements.count(0)
    switch_count = 0
    for i in range(1, len(elements)):
        current_element = elements[i]
        prev_char = elements[i-1]
        if current_element != prev_char:
            switch_count += 1
    print(switch_count)
find_switch_count(elements)