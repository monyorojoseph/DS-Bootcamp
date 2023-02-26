def add_elements(elements):
    total = 0
    for element in elements:
        total += int(element)
    return total


if __name__ == "__main__":
    elements = input("Type a list of numbers separated by commas: ").split(',')
    print(add_elements(elements))