def print_separator(title):
    """Helper function to format terminal output beautifully."""
    print(f"\n{'-' * 15} {title} {'-' * 15}")


# ===== Exercise 1: Variables and Data Types =====
print_separator("Exercise 1: Variables & Data Types")
width = 640
height = 480
image_name = "sample.png"
is_color = True

print(f"Variable 'width'      : {width}         \t| Type: {type(width)}")
print(f"Variable 'height'     : {height}        \t| Type: {type(height)}")
print(f"Variable 'image_name' : {image_name}    \t| Type: {type(image_name)}")
print(f"Variable 'is_color'   : {is_color}      \t| Type: {type(is_color)}")

total_pixels = width * height
print(f"\nTotal calculated pixels (width * height): {total_pixels}")


# ===== Exercise 2: if, elif, and else =====
print_separator("Exercise 2: if, elif, and else")
test_intensities = [-1, 0, 127, 128, 255, 256]

for intensity in test_intensities:
    if intensity < 0 or intensity > 255:
        label = "Invalid"
    elif intensity >= 128:
        label = "Bright pixel"
    else:
        label = "Dark pixel"
    print(f"Intensity {intensity:3} : {label}")


# ===== Exercise 3: for and while Loops =====
print_separator("Exercise 3: for and while Loops")
# for loop: visit each value in the list
print("For loop (threshold = 128):")
for value in [20, 130, 255]:
    if value >= 128:
        print(f"  Value {value:3} : Bright pixel")
    else:
        print(f"  Value {value:3} : Dark pixel")

# while loop: runs until counter reaches 3
print("\nWhile loop (counts 0 to 2):")
counter = 0
while counter < 3:
    print(f"  Counter : {counter}")
    counter += 1  # update the counter so the loop stops


# ===== Exercise 4: Functions =====
print_separator("Exercise 4: Functions")


def is_bright(pixel, threshold=128):
    """Return True if pixel is at least the threshold, otherwise False."""
    return pixel >= threshold


print(f"is_bright(127)      : {is_bright(127)}")
print(f"is_bright(128)      : {is_bright(128)}")
print(f"is_bright(200, 210) : {is_bright(200, 210)}")


# ===== Exercise 5: Lists and Tuples =====
print_separator("Exercise 5: Lists and Tuples")
# List operations
pixels = [0, 128, 255]
print(f"Original list       : {pixels}")
print(f"First item          : {pixels[0]}")

pixels[1] = 150
pixels.append(64)
print(f"Modified list       : {pixels}")
print(f"Total list length   : {len(pixels)}")

# Tuple operations
size = (640, 480)
width, height = size
print(f"\nUnpacked Tuple      : Width = {width}, Height = {height}")

# Explanation: A list is mutable, meaning its items can be reassigned, added, or removed.
# A tuple is immutable, meaning its structure and items are permanently fixed upon creation.


# ===== Exercise 6: Dictionaries and Sets =====
print_separator("Exercise 6: Dictionaries and Sets")
# Dictionary operations
image = {"width": 640, "height": 480}
print(f"Original dictionary : {image}")

image["mode"] = "RGB"
print(f"Modified dictionary : {image}")
print(f"Width (by key)      : {image['width']}")
print(f"Mode (by key)       : {image['mode']}")

# Set operations
label_list = ["cat", "dog", "cat", "bird"]
labels = set(label_list)
print(f"\nOriginal list       : {label_list}")
print(f"Unique labels count : {len(labels)}")
# Note: a set removes duplicates, and its display order may vary.