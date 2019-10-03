# Author: Jessica Strait
# This project reads and organizes sales data from a file as a comprehensive table.

# In our first function, we get to do the following things: open our file and read it; create empty lists for the ID
# numbers and sales data; and create a while loop to add all of our IDs and finish the empty sales list.
# Don't forget to close the file at the end!
def getIDs(filename):
    filename = open(filename, 'r')
    ids = filename.readline()
    id_numbers = []
    sales_data = []
    while ids != "":
        ids = ids.rstrip('\n')
        id_numbers.append(ids)
        sales_data.append([0.0, 0.0, 0.0, 0.0])
        ids = filename.readline()
    filename.close()
    return id_numbers, sales_data


# In our next function, we need to split the three different parts of the file. Then, we need to isolate each variable
# so that they can be manipulated individually. We have some formulas to do this with, and then our new values should be
# used to fill that empty data list.
def process_sales_data(filename, id_list, sales_data):
    file = open(filename, 'r')
    for line in file:
        id_number, month, sales = line.rstrip("\n").split()
        location = id_list.index(id_number)
        month = int(month)
        quarter = (month - 1)//3
        sales = round(float(sales), 2)
        sales_data[location][quarter] += sales
    file.close()


# This next function will have a lot of crazy calculations! We should start by just totalling our rows and columns. We
# need to remember that columns don't "exist" in Python, so we will need to create a for loop to identify the values we
# want. We also need to total either the ID totals or quarter totals; they should be equivalent, so it does not matter
# which we choose.
def print_report(id_list, sales_data):
    id_totals = []
    for value in range(len(sales_data)):
        id_totals.append(round(sum(sales_data[value]), 2))
    id_totals.append(round(sum(map(sum, sales_data)), 2))
    quarter_totals = [0, 0, 0, 0]
    for row in range(len(sales_data)):
        for column in range(len(sales_data[row])):
            quarter_totals[column] += sales_data[row][column]
    sales_data.append(quarter_totals)
# Next, we need to format our information and identify some key data points. We can set up our information spaced apart,
# and we should have each row and column rounded off to two decimal places. We should also sort our sales list so that
# we can find the biggest sale by a salesman in a quarter: the highest ranking quarter will be significantly simpler
# to find, as we can maximize the "quarter_totals" list that we made earlier in this function.
    print("--------Annual Sales Report--------")
    print("ID\tQT1\t\tQT2\t\tQT3\t\tQT4\t\tTotal")
    for row in range(len(sales_data)):
        for column in range(len(sales_data[row])):
            sales_data[row][column] = format(sales_data[row][column], '.2f')
    id_list.append('Total')
    for row in range(len(sales_data)):
        print(id_list[row], '\t \t'.join(sales_data[row]), '\t \t', id_totals[row])
    max_salesman = sorted(sales_data, key=lambda x: x[1])
    id_list.sort()
    print("Max Sales by Salesperson: ID =", id_list[0], "Amount = $", (max_salesman[0][0]))
    max_quarter = max(quarter_totals)
    print("Max Sales by Quarter: Quarter =", quarter_totals.index(max(quarter_totals))+1, "Amount = $", max_quarter)


# Finally, we need to ask the user for input and call all of our functions! Remember, because our first function
#  produced two different returned items, we need to specify those as well. Great work- this was a difficult project! :)
def main():
    sales_ids = input("Enter the name of the sales ids file.")
    data_file = input("Enter the name of the sales data file.")
    id_numbers, sales_list = getIDs(sales_ids)
    getIDs(sales_ids)
    process_sales_data(data_file, id_numbers, sales_list)
    print_report(id_numbers, sales_list)


main()

