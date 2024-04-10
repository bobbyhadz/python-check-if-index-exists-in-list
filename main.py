# Check if an index exists in a List in Python

my_list = ['bobby', 'hadz', 'com']

index = 2

if index < len(my_list):
    # 👇️ this runs
    print('The index exists in the list', my_list[index])
else:
    print('The index does NOT exist in the list')


print(2 < len(my_list))  # 👉️ True
print(3 < len(my_list))  # 👉️ False