Pass = 0
defer = 0
fail = 0
progress = 0
trailer = 0
retriever = 0
exclude = 0
data = []

user = input("Part1, Part2, Part3, Part4: ")

def part1():
    print('_ ' * 40, " ")
    print('Horizontal Histogram')
    print('Progress ', progress, '   :', '*' * progress)
    print('Trailer ', trailer, '    :', '*' * trailer)
    print('Retriever ', retriever, '  :', '*' * retriever)
    print('Excluded ', exclude, '   :', '*' * exclude)
    print()
    print(progress + trailer + retriever + exclude, 'outcome in total.')
    print('_ ' * 40)


def part2():
    print('_ ' * 40, '\n')
    print('Progress  ', 'Trailer  ', 'Retriever  ', 'Excluded ')
    for x in range(max(progress, trailer, retriever, exclude)):
        print("    {0}         {1}          {2}           {3}".format(
            '*' if x < progress else ' ',
            '*' if x < trailer else ' ',
            '*' if x < retriever else ' ',
            '*' if x < exclude else ' '
        ))
    print()
    print(progress + trailer + retriever + exclude, 'outcomes in total.')
    print('_ ' * 40)


def part3():
    print('_ ' * 40, " ")
    print('Horizontal Histogram')
    print('Progress ', progress, '   :', '*' * progress)
    print('Trailer ', trailer, '    :', '*' * trailer)
    print('Retriever ', retriever, '  :', '*' * retriever)
    print('Excluded ', exclude, '   :', '*' * exclude, '\n')
    print(progress + trailer + retriever + exclude, 'outcome in total.')
    print('_ ' * 40, '\n')

    for i in data:
        print(i)


def part4():
    print('_ ' * 40, " ")
    print('Horizontal Histogram')
    print('Progress ', progress, '   :', '*' * progress)
    print('Trailer ', trailer, '    :', '*' * trailer)
    print('Retriever ', retriever, '  :', '*' * retriever)
    print('Excluded ', exclude, '   :', '*' * exclude, '\n')
    print(progress + trailer + retriever + exclude, 'outcomes in total.')
    print('_ ' * 40, '\n')

    outFile = open('data.txt', 'w')  # open the txt file
    for i in data:
        outFile.write(i + '\n')
    outFile.close()  # close the txt file

    # Print out the histogram saved in the txt file
    fileData = open('data.txt', 'r')
    read = fileData.read()
    print(read)
    fileData.close()


while True:
    try:
        Pass = int(input("Please enter your credit at pass: "))
        if Pass > 120 or Pass < 0 or (Pass % 20 != 0):
            print('Out of range\n')
            continue

        Defer = int(input("Please enter you credit at Defer: "))
        if Defer > 120 or Defer < 0 or (Defer % 20 != 0):
            print('Out of range\n')
            continue

        Fail = int(input("Please enter you credit at Fail: "))
        if Fail > 120 or Fail < 0 or (Fail % 20 != 0):
            print('Out of range\n')
            continue
    except:
        print("Integer Required\n")
        continue

    if Pass + Defer + Fail != 120:
        print("Total incorrect!\n")
        continue
    else:
        if Pass == 120:
            print("Progress\n")
            progress += 1
            data.append(f"Progress - {Pass}, {Defer}, {Fail}")
        elif Pass >= 100:
            print("Progress (module trailer)\n")
            trailer += 1
            data.append(f"Progress (module trailer) - {Pass}, {Defer}, {Fail}")
        elif (Pass >= 40 and Fail <= 60) or (Defer >= 60 and Fail <= 60):
            print("Do not Progress – module retriever\n")
            retriever += 1
            data.append(f"Do not Progress - module retriever - {Pass}, {Defer}, {Fail}")
        else:
            print("Exclude\n")
            exclude += 1
            data.append(f"Exclude - {Pass}, {Defer}, {Fail}")

    print('Would you like to enter another set of data ?')
    option = input("Enter 'y' for yes or 'q' to quit and view results: ")
    print()

    if option == 'y':
        continue
    elif option == 'q':
        if user == 'part1':
            part1()
        elif user == 'part2':
            part2()
        elif user == 'part3':
            part3()
        elif user == 'part4':
            part4()
        break
    else:
        print("Invalid input!")
        break
