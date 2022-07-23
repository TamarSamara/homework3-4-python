import statistics


# Returns a dictionary for the organs in which the "sex" field is equal to "male"
# and a dictionary for the organs in which the "sex" field is equal to "female"
def split_male_female(data_set):
    dict_female, dict_male = {}, {}
    for x, y in data_set.items():
        if y.get("sex") == "female":
            dict_female.update({x: y})
        else:
            dict_male.update({x: y})
    return dict_female, dict_male


# Returns the average age and median age of the resulting dictionary
def find_median_average(data_set):
    sum_age = 0
    lst = []
    for x, y in data_set.items():
        y_age = y.get("age")
        sum_age += y_age
        lst.append(y_age)
    average_age = sum_age / len(data_set)
    median_age = statistics.median(lst)
    return average_age, median_age


# If a number is obtained - a function will print organs that have an age field greater than the number
# If no number is sent - a function will print all the members of the dictionary
def print_values_above(data_set, num=0):
    if num == 0:
        for x, y in data_set.items():
            print(f'{x} : {y}')
    else:
        for x, y in data_set.items():
            if y.get("age") > num:
                print(f'{x} : {y}')


if __name__ == '__main__':
    data_set = {
        1: {"name": "adham", "sex": "male", "age": 22},
        2: {"sex": "female", "age": 57, "height": 1.58, "name": "amal"},
        3: {"sex": "male", "age": 64, "height": 1.80, "name": "emad"},
        4: {"sex": "female", "age": 29, "height": 1.55, "name": "tamar"},
        5: {"sex": "female", "age": 20, "height": 1.65, "name": "rima"}
    }
    # ex.1 a:
    print("ex.1 a:")
    dict_female, dict_male = split_male_female(data_set)
    print(f'The male dictionary is: {dict_male}')
    print(f'The female dictionary is: {dict_female}\n')

    # ex.1 b:
    print("ex.1 b:")
    average_age, median_age = find_median_average(data_set)
    print(f'middle age: {median_age}')
    print(f'average age: {average_age}\n')

    # ex.1 c:
    print("ex.1 c:")
    print_values_above(data_set)
    # or
    print("\nage > 25:")
    print_values_above(data_set, 25)



