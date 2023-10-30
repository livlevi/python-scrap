import re

file_name = "input.txt"
total_lit_count = 0
total_mem_count = 0
total_encode_count = 0
# slash = "\\"
# pattern1 = r'\\[xX][0-9a-fA-F]+' # hex characters
# pattern2 = r'(\\\\)+' # double backslash
# pattern3 = r'(\\")+' # escaped quotation marks
slash_count = 0
non_slash_count = 0

def strlitCount(item):
    count = 0
    for c in item:
        count = count + 1
    return count

def strmemCount(item):
    length = len(item)  
    i = 1
    count = 0
    while i < length -1:
        if item[i] == "\\":
            i += 4 if item[i + 1] == "x" else 2
        else:
            i += 1
        count += 1
    return count

def encode(s):
    result = ['"']
    for c in s:
        if c == '"':
            result.append('\\\"')
        elif c == '\\':
            result.append("\\\\")
        else:
            result.append(c)
    result.append('"')
    strresult = ''.join(result)
    return strresult

with open (file_name, "r") as file:
    for line in file:
        total_lit_count += strlitCount(line.strip())
        total_mem_count += strmemCount(line.strip())
        total_encode_count += strlitCount(encode(line.strip()))

print(total_mem_count)
print(total_lit_count)
print("Part 1 Answer: ", total_lit_count - total_mem_count)
print("******************")
print(total_encode_count)
print("Part 2 Answer: ", total_encode_count - total_lit_count)