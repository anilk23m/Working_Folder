#while loop
#loop will repeat until condition is false

count = 1
while count <= 5:
    print(f"Attempt {count}")
    count+=1

#control statement - break uses to exit the loop immediately.
for i in range(1,11):
    if i == 5:
        print("found 5 - stopping")
        break
    else:
        print(i)

results = ["pass", "pass", "fail", "pass", "fail"]
for i, result in enumerate(results):
    if result == "fail":
        print(f"{i}: {result}")
        break

#continue - skip the current iteration
for i in range(1,6):
    if i == 3:
        continue
    print(i)