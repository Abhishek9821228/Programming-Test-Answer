# Answer 1 ------------------------

def calculate(n):
    total = 0
    for i in range(1, n, 3):
        total += (i * (i + 1)) / (i + 2)
    return int(total)

result = calculate(30000)
print(result)



# Answer 2 ------------------------

def calculate(n, times):
    for _ in range(times):
        n = int(n * 0.8)
    return n

value = calculate(387420489, 42)
print(value)



# Answer 3 ------------------------

def main():
    x = 0
    n = 1
    cnt = 0

    while x <= 3.1413:
        x += 8 / (n * (n + 2))
        n += 4
        cnt += 1

    print(x)
    print(cnt)

if __name__ == "__main__":
    main()



# Answer 4 ------------------------

def common_pair(sequence):
    pairs = [sequence[i:i+2] for i in range(len(sequence)-1)]
    pair_counts = {}
    
    for pair in pairs:
        if pair in pair_counts:
            pair_counts[pair] += 1
        else:
            pair_counts[pair] = 1
    
    most_common_pair = max(pair_counts, key=pair_counts.get)
    return most_common_pair

sequence = "14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912"

most_common = common_pair(sequence)
print(most_common)



# Answer 5 ------------------------

def truck_count(total_boxes, max_capacity):
    weights = list(range(1, total_boxes + 1))  #
    
    truck_count = 0
    current_weight = 0

    for weight in reversed(weights):
        if current_weight + weight <= max_capacity:
            current_weight += weight
        else:
            truck_count += 1
            current_weight = weight

    return truck_count + (current_weight > 0)  


boxes = 800
max_capacity = 5000

trucks_needed = truck_count(boxes, max_capacity)
print(trucks_needed)



# Answer 6 ------------------------

count = 0

for num in range(1, 1000001):
    temp = num
    for _ in range(4):
        digits = [int(digit) for digit in str(temp)]
        product = 1
        for digit in digits:
            product *= digit
        temp = product
        if temp < 10:
            break
    if temp < 10 and _ == 3:
        count += 1

print(count)



# Answer 7 ------------------------

def int_to_roman(n):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ''
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_numeral += syms[i]
            n -= val[i]
        i += 1
    return roman_numeral

def count_roman_numbers():
    total_sum = 0
    for num in range(1, 1001):
        roman_numeral = int_to_roman(num)
        if len(roman_numeral) == 9:
            total_sum += num
    return total_sum

result = count_roman_numbers()
print(result)

