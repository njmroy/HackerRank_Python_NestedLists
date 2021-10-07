def lambda_sort(sublist):
    # key is set to sort using second element of
    # sublist using lambda
    sublist.sort(key=lambda x: x[1])
    return sublist

if __name__ == '__main__':
    group = []
    for _ in range(int(input())):
        person = []
        person.extend([input(), float(input())])
        group.append(person)

    sorted_group = lambda_sort(group)

    if len(sorted_group) <= 1:
        print(sorted_group[0][1])

    elif len(sorted_group) > 2:

        first = sorted_group[0][1]

        for elem in range(0, len(sorted_group)):
            for i in sorted_group:
                for item in i:
                    if item == first:
                        sorted_group.remove(i)

        second_lowest = sorted_group[0][1]

        final = []
        for person in sorted_group:
            if person[1] == second_lowest:
                final.append(person[0])

        final.sort()
        for i in final:
            print(i)
