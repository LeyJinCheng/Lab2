def display_average(user_values):
    average=sum(user_values)/len(user_values)
    format_float = "{:.2f}".format(average)
    print("The average of the 3 number is " + format_float)

def get_user_value():
    x = int(input("Enter first value "))
    y = int(input("Enter first value "))
    z = int(input("Enter first value "))

    print("The values are " + str(x) + " , " + str(y) + " , " + str(z))
    return [x,y,z]

def find_min_max(user_values):
    print("The highest number is =" +str(max(user_values)))
    print("The lowest number is =" +str(min(user_values)))

def sort_tem(user_values):
    print(sorted(user_values))
def find_median(user_values):
    middle_index=(len(user_values)+1)//2
    print(user_values[middle_index-1])
def main():
    user_values=get_user_value()
    display_average(user_values)
    find_min_max(user_values)
    sort_tem(user_values)
    find_median(user_values)


if __name__ == '__main__':
    main()


