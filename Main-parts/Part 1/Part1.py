Pass = 0
defer = 0
fail = 0
progress = 0
trailer = 0
retriever = 0
exclude = 0

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
        elif Pass >= 100:
            print("Progress (module trailer)\n")
            trailer += 1
        elif (Pass >= 40 and Fail <= 60) or (Defer >= 60 and Fail <= 60):
            print("Do not Progress – module retriever\n")
            retriever += 1
        else:
            print("Exclude\n")
            exclude += 1

    print('Would you like to enter another set of data ?')
    option = input("Enter 'y' for yes or 'q' to quit and view results: ")
    print()

    if option == 'y':
        continue
    elif option == 'q':
        print('_ ' * 40, " ")
        print('Horizontal Histogram')
        print('Progress ', progress, '   :', '*' * progress)
        print('Trailer ', trailer, '    :', '*' * trailer)
        print('Retriever ', retriever, '  :', '*' * retriever)
        print('Excluded ', exclude, '   :', '*' * exclude)
        print()
        print(progress + trailer + retriever + exclude, 'outcome in total.')
        print('_ ' * 40)
        break
    else:
        print("Invalid input!")
        break
