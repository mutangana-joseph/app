import random, string

all_chars = list(string.ascii_letters + string.digits)

result_list = random.choices(all_chars, k=6)
code ="".join(result_list).upper()

print(code)
