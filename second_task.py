while True :
    list = []
    i = True
    while i == True :
        a = int(input("Enter a number: "))
        list.append(a)
        ques = input("end ? if yes then enter 'D' else enter any character: ")
        if ques == 'D' :
            i = False

    print("Input list = " , list)
    print("Output =")

    for i in list :
        if i > 0 :
            print(i)
    q = input("Want to continue? type 'y' for yes : ")
    if q != 'y':
        break
