def main():
    print("Daily Sales Tracker")
    days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' )
    for index in range (len(days)):
        money_list = []
        money_list[index] = int(input(f'Enter the sales amount for  {days[index]}  \t: '))
        print(money_list)
#         print(f'the total is {process(money_list)}')
# def process(value_list):
#     total = 0
#     print(value_list)
#     for num in value_list:
#          total = total + num
#     return total

if __name__ == '__main__':
    main()
