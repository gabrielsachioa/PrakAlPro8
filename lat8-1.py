with open("file/teks1.txt", "r") as file1, open("file/teks2.txt", "r") as file2:
       data1 = file1.readlines()
       data2 = file2.readlines()

       for i in range(len(data1)):
            if data1[i] != data2[i]:
                print(f'teks 1: {data1[i]}', end="")
                print(f'teks 2: {data2[i]}', end="")
                print()