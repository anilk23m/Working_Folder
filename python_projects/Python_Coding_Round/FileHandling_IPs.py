def remove_duplicate_ips(input_file, output_file):
    with open(input_file, "r") as f:
        ip_list = f.readlines()

    unique_ips = set(ip.strip() for ip in ip_list)

    with open(output_file, "w") as f:
        for ip in sorted(unique_ips):
            f.write(ip + "\n")
    print(f"Removed duplicates. {len(unique_ips)} unique IPs written to {output_file}")

remove_duplicate_ips("inputIp.txt", "UniqueIp.txt")