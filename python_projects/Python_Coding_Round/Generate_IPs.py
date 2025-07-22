import random

def generate_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

# Create a base list of 500 unique IPs
unique_ips = {generate_ip() for _ in range(500)}

# Add 500 more with duplicates randomly selected
ip_list = list(unique_ips)
while len(ip_list) < 1000:
    if random.choice([True, False]):
        # Add a duplicate
        ip_list.append(random.choice(ip_list))
    else:
        # Add a new unique IP
        ip_list.append(generate_ip())

# Shuffle the final list
random.shuffle(ip_list)

# Write to file
with open("inputIp.txt", "w") as f:
    for ip in ip_list:
        f.write(ip + "\n")

print("File 'ips.txt' created with 1000 IPs (including duplicates).")
