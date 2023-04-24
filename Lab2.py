def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def calc_average(number_list):
    total = 0
    for i in number_list:
        total += float(i)
    average = total / len(number_list)
    return average


def get_user_input():
    user_input = input()
    number_list = user_input.split(",")
    return number_list

def find_min_max(number_list):
    min_temp = min(number_list)
    max_temp = max(number_list)
    temp_list = [min_temp, max_temp]
    return temp_list


def sort_temperature(number_list):
    return sorted(number_list)

def calc_median_temperature(number_list):
    if len(number_list) % 2 == 1:
        median = number_list[int((len(number_list)-1)/2)]

    else:
        median = int((int(number_list[int(len(number_list)/2)]) + int(number_list[int(len(number_list)/2-1)])))/2

    return median


def main():
    display_main_menu()
    number_list = get_user_input()
    min_max_temp = find_min_max(number_list)
    print("Min Temperature is "+min_max_temp[0])
    print("Max Temperature is "+min_max_temp[1])
    average = calc_average(number_list)
    print("Average is "+str(average))
    sorted = sort_temperature(number_list)
    print("Sorted list: "+str(sorted))
    median = calc_median_temperature(sorted)
    print("Median is "+str(median))

if __name__ == "__main__":
    main()




