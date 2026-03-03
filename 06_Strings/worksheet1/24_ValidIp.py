"""
Generate All Valid IP Addresses from a String
Explanation: Given a string of digits, form all possible valid IP addresses.
Input: "25525511135"
Expected Output: ['255.255.11.135', '255.255.111.35']
"""
def restore_ip_addresses(s):
    result = []
    n = len(s)

    for i in range(1, 4):
        for j in range(i+1, i+4):
            for k in range(j+1, j+4):

                if k >= n:
                    continue

                part1 = s[:i]
                part2 = s[i:j]
                part3 = s[j:k]
                part4 = s[k:]

                parts = [part1, part2, part3, part4]

                if all(valid(part) for part in parts):
                    result.append(".".join(parts))

    return result


def valid(part):
    return (len(part) == 1 or part[0] != '0') and int(part) <= 255


s = "25525511135"
print(restore_ip_addresses(s))
