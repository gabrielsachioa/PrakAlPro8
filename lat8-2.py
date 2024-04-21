with open("soal.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = line.split("||")

        print(line[0])
        jawaban = input("Jawab: ")
        if jawaban == line[1][1:]:
            print("Jawaban benar")
        else:
            print("Jawaban salah!")