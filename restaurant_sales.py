def main():
    print("Daily Sales Tracker")
    print()
    days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' )#tuple for days
    sales_list = [] # empty list to store the sales values

    for index in range (len(days)):
        value = int(input(f'Enter the sales amount for  {days[index]}  \t: '))
        sales_list.append(value)# puts the inpu tin teh list
    total = 0
    average = 0
    for num in sales_list:
         total += num
         average = total / len(sales_list)
        #uses length of sales list and total to calculate average
    print()
    print(f'Total weekly sales : ${total:,.2f}')
    print(f'Average weekly sales : ${average:,.2f}')
    print()
    print(f'The highest sales were ${max(sales_list):,.2f} on {days[sales_list.index(max(sales_list))]}')
    #uses the sales_index to get the number we should use for the day index
    print(f'The lowest sales were ${min(sales_list):,.2f} on {days[sales_list.index(min(sales_list))]}')


if __name__ == '__main__':
    main()