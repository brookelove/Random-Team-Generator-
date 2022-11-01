import random
import sys
# this is a random generator for my students it will either in take the students name from a list and then generate the expected teams
# asks for the number of people that needs to be in a group
# takes that number and generates a random group


def random_groups(names, number_of_groups):
    # need to shuffle the names
    random.shuffle(names)
    # create a new aray with teh list of lists of groups to create
    new_groups = []
    # if (names <= number_of_groups):
    #     # if the name is less than the number of groups exit the system
    #     print("please make sure your names are moer than the students")
    #     sys.exit()
    # the number in the for loop will be looped as many times as the group input
    for index in range(number_of_groups):
        # the index is the current group and will loop at the range in the number of group
        group = names[index::number_of_groups]
        # will append the current group to the new groups made
        new_groups.append(group)
    # run through groups and create a new group
    for index, group in enumerate(new_groups):
        print(f"Group {index + 1} : {' , '.join(group)}\n")


group_num = input("How many groups do you need for your team?\n")

random_groups(student_names, int(group_num))
