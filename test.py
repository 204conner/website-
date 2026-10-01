# numbers = [5, 10, 15, 20]
# numbers = list(range(5))
# numbers = [0] * 5
# numbers = [1, 2, 3] * 3
# numbers = [1, 2, 3, 4]
# for num in numbers:
#     print(num)
# my_list = [10, 20, 30, 40]
# print(my_list[0], my_list[1],my_list[2], my_list[3])
#
# index = 0
# while index < 4:
#     print(my_list[index])
#     index += 1
# print(my_list[-1], my_list[-2], my_list[-3], my_list[-4])
# my_list = [10, 20, 30, 40]
# index = 0
# while index < len(my_list):
#     print(my_list[index])
#     index +=1
# names = ['jenny', 'kelly', 'chloe', 'aubrey']
# for index in range(len(names)):
#     print(names[index])
#     index+=1
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# numbers[0] = 99
# print(numbers)
# numbers = [0] * 5
# for index in range(len(numbers)):
#     numbers[index] = 99
# print(numbers)
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# list3 = list1 + list2
# print(list3)
# girl_names = ['joanne', 'karen', 'lori']
# boy_names = ['chris', 'jerry', 'will']
# all_names = girl_names + boy_names
# print(all_names)
# days = ['sunday', 'monday', 'tuesday', 'wednesday','thursday','friday','saturday']
# mySlice = days[2:5]
# print(mySlice)
# def main():
#      prod_nums = ['V475', 'F987','Q143','R688']
#      search = input('Enter a product number: ' )
#      if search in prod_nums:
#          print(f'{search} was found in the list.')
#      else:
#         print(f'{search} was not found in the list')
# if __name__ == '__main__':
#     main()
# play_again = 'y'
# while play_again in['y','Y','yes','Yes']:
#
#     play_again = input('do you want to play again?')
# def main():
#     name_list = []
#     again = 'y'
#     while again.upper() in ['Y','y']:
#         name = input ('Enter a name: ')
#         name_list.append(name)
#         print('Do you want to add another name?')
#         again = input('y =yes anything else = no')
#         print()
#     print('here are the names you entered ')
#     for name in name_list:
#         print(name)
# if __name__ == '__main__':
#     main()
# def main():
#     names = ['james','kathryn', 'bill']
#     print('the list of names before insert')
#     print(names)
#     names.insert(0, 'joe')
#     print('names after the insert')
#     print(names)
# if __name__ == '__main__':
#     main()
# def main():
#     food = ['pizza','burger','chips']
#     print('here are the items in the food list:')
#     print(food)
#     item = input('which item should i remove')
#     try:
#         food.remove(item)
#         print('here is the revised list:')
#         print(food)
#     except ValueError:
#         print('that item was not found in the list')
# if __name__ == '__main__':
#     main()
# my_list = [1,2,3,4,5]
# print('before deletion:', my_list)
# del my_list[2]
# print('list after deletion:', my_list)
# def main():
#     food = ['pizza','burger','chips']
#     print('here are the items in the food list:')
#     print(food)
#     item = input('which item should i change?')
#     try:
#         item_index = food.index(item)
#         new_item = input('enter the new value:')
#         food[item_index] = new_item
#         print('here is the revised list :')
#         print(food)
#     except ValueError:
#         print('That item was not found in the list.')
# if __name__ == '__main__':
#     main()
# my_list = [9,1,0,2,8,6,7,4,5,3]
# print('Original order:', my_list)
# my_list.sort()
# print('sorted order:', my_list)
# my_list = [5,4,3,2,50,40,30]
# print('The lowest value is', min(my_list))
# print('The highest value is', max(my_list))
# list1  = [1,2,3,4]
# list2 = list1
# print(list2)
# list1 =[1,2,3,4]
# list2=[]
# for item in list1:
#     list2.append(item)
# list1 = [1,2,3,4]
# list2 = [] + list1
# NUM_EMPLOYEE = 3
# def main():
#     hours = [0] * NUM_EMPLOYEE
#
#     for index in range(NUM_EMPLOYEE):
#         hours[index]= float(input(f'Enter the hours worked by employee {index +  1}:'))
#     pay_rate = float(input('enter the hourly pay rate:'))
#     for index in range(NUM_EMPLOYEE):
#         gross_pay = hours[index] * pay_rate
#         print(f'gross pay for employee {index + 1}: ${gross_pay:,.2f}')
# if __name__ == '__main__':
#     main()
