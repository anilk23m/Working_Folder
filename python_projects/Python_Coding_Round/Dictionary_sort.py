# here write a python code to sort the dictionary using either value/key
# below code uses bubble sort and key as the parameter to sort the dictionary
def bubble_sort(elements, key = None):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1):
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if swapped == False:
            break

if __name__ == '__main__':
    elements = [
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google-pixel"},
        {"name": "kathy", "transaction_amount": 200, "device":"vivo"},
        {"name": "aamir", "transaction_amount": 800.,"device": "iphone-8"}
    ]
    bubble_sort(elements, 'transaction_amount')
    print(elements)