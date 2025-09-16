number = int(input("Enter a number: "))
number += 5  # This is equivalent to number = number + 5
print(f"Updated number after adding 5 is: {number}")

number *= 2  # This is equivalent to number = number * 2  #110=55*2
print(f"Updated number after multiplying by 2 is: {number}")

number -= 3  # This is equivalent to number = number - 3 #107=110-3
print(f"Updated number after subtracting 3 is: {number}")

number /= 4  # This is equivalent to number = number / 4 #26.75=107/4
print(f"Updated number after dividing by 4 is: {number}")

number %= 3  # This is equivalent to number = number % 3 #2.75=26.75%3
print(f"Updated number after modulus 3 is: {number}")

number **= 2  # This is equivalent to number = number ** 2 #7.5625=2.75**2
print(f"Updated number after raising to the power of 2 is: {number}")

number //= 5  # This is equivalent to number = number // 5 #1.0=7.5625//5
print(f"Updated number after floor division by 5 is: {number}")
