from collections.abc import Callable

# ==============================================================================
# TRAP 1: Mutable Default Argument
# ==============================================================================


def f(x: list[int] = []) -> list[int]:  # noqa: B006
    x.append(1)
    return x


print(f())  # Output: [1]
print(f())  # Surprising Output: [1, 1] (Expected: [1])

# Explanation:
# Python evaluates default arguments once at function definition time,
# not at runtime. Since a list is mutable, every subsequent call reuses
# and modifies that exact same list object.


# ==============================================================================
# TRAP 2: Late-binding Closures
# ==============================================================================

# Using noqa: B023 inline directly where the lambda variable is evaluated
multipliers: list[Callable[[int], int]] = [
    lambda x: x * i  # noqa: B023
    for i in range(3)
]

print([func(2) for func in multipliers])  # Surprising Output: [4, 4, 4]

# Explanation:
# Python closures look up variables using late binding, meaning they read
# the value of 'i' when called. By the time the functions run, the loop
# has finished and 'i' remains 2 for all of them.


# ==============================================================================
# TRAP 3: 'is' on Small Integers
# ==============================================================================

a, b = 256, 256
print(a is b)  # Output: True

x, y = 257, 257
print(x is y)  # Surprising Output: False (Even though x == y is True)

# Explanation:
# To optimize performance, Python pre-allocates and caches integer objects
# between -5 and 256. Numbers within this range share the same memory
# address, while larger numbers create distinct objects.


# ==============================================================================
# TRAP 4: Mutating a List While Iterating Over It
# ==============================================================================

numbers: list[int] = [1, 2, 3, 4]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)  # Surprising Output: [1, 3, 4] (Expected: [1, 3])

# Explanation:
# The loop uses an internal index that advances by 1 on every iteration.
# Removing an item shifts remaining items left, causing the index to skip
# the next immediate element.


# ==============================================================================
# TRAP 5: '==' vs 'is' on Strings (String Interning)
# ==============================================================================

str1, str2 = "hello_world", "hello_world"
print(str1 is str2)  # Output: True

str3, str4 = "hello world!", "hello world!"
print(str3 is str4)  # Surprising Output: False (Even though str3 == str4)

# Explanation:
# Python automatically "interns" string literals that resemble valid
# identifiers (no spaces/symbols). Standard strings reuse the same memory
# location, while complex strings create distinct object addresses.
