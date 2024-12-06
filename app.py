import random

def generate_pairs(names_list):
    # Check if the list has at least 2 people
    if len(names_list) < 2:
        print("There must be at least two people to create pairs!")
        return

    # Shuffle the list randomly
    random.shuffle(names_list)

    pairs = []
    for i in range(0, len(names_list), 2):
        # When the number of people is odd, the last person will be paired with the first
        if i + 1 < len(names_list):
            pairs.append((names_list[i], names_list[i + 1]))
        else:
            # If there is one person left without a pair, they will be paired with the first person
            pairs.append((names_list[i], names_list[0]))

    return pairs

# Main function
def main():
    # Get the names of people
    names_list = []
    print("Enter the names of the people. When you're done, type 'done'.")

    while True:
        name = input("Enter a name: ")
        if name.lower() == 'done':
            break
        names_list.append(name)

    # Generate the pairs
    pairs = generate_pairs(names_list)

    # Display the pairs
    print("\nThe gift pairs are:")
    for pair in pairs:
        print(f"{pair[0]} will give a gift to {pair[1]}")

if __name__ == "__main__":
    main()
