test_list = [1,2,3,4]
test_list.append(5)

odd_list = [num for num in test_list if num%2 != 0]

print(test_list)
print(odd_list)

for num in test_list:
    print(num)
