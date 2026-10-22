def main():
    file_name = input('What is the name of the file you wish to work with? ')
    read_or_write = input('Are you going to (R)ead the file or (W)rite the file? ')
    file = open(file_name, read_or_write)
    questions = ('first name', 'last name', 'street address', 'city','state', 'zip code')
    if read_or_write == 'w':
        for i in range(len(questions)):
            x = input(f'Enter the {questions[i]}: ')
            file.write(x)
        file.close()
    if read_or_write == 'r':
        file = open(file_name, 'r')
        for file_contents in file:
            print(file_contents.rstrip('\n'))



if __name__ == '__main__':
    main()