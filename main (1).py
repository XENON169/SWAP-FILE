def SwapingFiles():
    sample1 = input("Enter 1st file name...")
    sample2 = input("Enter 2nd file name...")


    with open(sample1.txt,'r') as a:
        data_a = a.read()

    with open(sample2.txt,'r') as b:
        data_b = b.read()

    with open(sample1.txt,'w') as a:
        a.write(data_b)

    with open(sample2.txt,'w') as b:
        b.write(data_a)
    
SwapingFiles()
