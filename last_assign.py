#!/usr/bin/env python3
# Created by Marc Coffi
# Created in June 2022
# This program alternate the elements
# of two inputed lists
# also divide in two
# a list inputed by the user
# the user has the option to
# choose between the two problems

# Defining the function that alternates elements
def alternating_elements(sentence1, sentence2):
    new_list = []
    substractor = 0
    max_elements = len(sentence1) + len(sentence2)
    sent1 = 0
    sent2 = 1
    index = 0
    while len(new_list) < max_elements:
        try:
            new_list.append(sentence1[index])
            new_list.append(sentence2[index])
            index += 1
        except:
            continue
    return new_list


# Defining the function that divide a list in 2
def list_in_2(sentence):
    new_list = []
    new_list2 = []
    size = len(sentence) / 2
    new_size = int(size)
    try:
        for counter in range(new_size):
            new_list.append(sentence[counter])
            sentence.pop(counter)
        for counter in range(len(sentence)):
            new_list2.append(sentence[counter])
        print(new_list)
        print(new_list2)
    except:
        print(new_list)
        print(new_list2)
        exit()


def main():
    # Getting user first list and splitting it
    print("Enter two list of elements seperated by a comma.")
    user_input = input("Enter the first list of elements: ")
    first_list = user_input.split(",")

    # Getting user second list and splitting it
    user_input2 = input("Enter the second list of elements: ")
    second_list = user_input2.split(",")

    # Calling the function
    new_list = alternating_elements(first_list, second_list)

    print(new_list)

    # Getting user list and splitting it
    print("Enter a list seperated by a comma.")
    user_input = input("Enter a list that will be divided in 2: ")
    first_list = user_input.split(",")

    # Calling the function
    list_in_2(first_list)


if __name__ == "__main__":
    main()
