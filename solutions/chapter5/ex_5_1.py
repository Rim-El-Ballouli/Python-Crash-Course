numbers = range(1, 20)


print("\nIs 21 in my list? I predict False.")
print(21 in numbers)

print("\nIs 0 in my list? I predict False.")
print(0 in numbers)

print("\nIs the first element 0 in my list? I predict False.")
print(numbers[0] == 0)

print("\nDoes the list have 5 elements? I predict False.")
print(len(numbers) == 5)

print("\nis the last number greater than 8? I predict False.")
print(numbers[-1] > 25)





print("\nIs 4 in my list? I predict True.")
print(4 in numbers)

print("\nIs 1 in my list? I predict True.")
print(1 in numbers)

print("\nIs the first element 1 in my list? I predict True.")
print(numbers[0] == 1)

print("\nDoes the list have 19 elements? I predict True.")
print(len(numbers) == 19)

print("\nis the last number greater than 8? I predict True.")
print(numbers[-1] > 18)
