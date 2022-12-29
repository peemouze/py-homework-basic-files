

def total_file():
    out_file = "rewrite_file.txt"
    path1 = '1.txt'
    path2 = '2.txt'
    path3 = '3.txt'
    with open(path1, 'r', encoding='utf-8') as f1:
        file1 = f1.readlines()
    with open(path2, 'r', encoding='utf-8') as f2:
        file2 = f2.readlines()
    with open(path3, 'r', encoding='utf-8') as f3:
        file3 = f3.readlines()
    with open(out_file, 'w', encoding='utf-8') as f_total:

        if len(file1) < len(file2) and len(file1) < len(file3):
            f_total.write(path1 + '\n')
            f_total.write(str(len(file1)) + '\n')
            f_total.writelines(file1)
            f_total.write('\n')
        elif len(file2) < len(file1) and len(file2) < len(file3):
            f_total.write(path2 + '\n')
            f_total.write(str(len(file2)) + '\n')
            f_total.writelines(file2)
            f_total.write('\n')
        elif len(file3) < len(file1) and len(file3) < len(file2):
            f_total.write(path3 + '\n')
            f_total.write(str(len(file3)) + '\n')
            f_total.writelines(file3)
            f_total.write('\n')
        if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                file3):
            f_total.write(path1 + '\n')
            f_total.write(str(len(file1)) + '\n')
            f_total.writelines(file1)
            f_total.write('\n')
        elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(file3):
            f_total.write(path2 + '\n')
            f_total.write(str(len(file2)) + '\n')
            f_total.writelines(file2)
            f_total.write('\n')
        elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(file2):
            f_total.write(path3 + '\n')
            f_total.write(str(len(file3)) + '\n')
            f_total.writelines(file3)
            f_total.write('\n')
        if len(file1) > len(file2) and len(file1) > len(file3):
            f_total.write(path1 + '\n')
            f_total.write(str(len(file1)) + '\n')
            f_total.writelines(file1)
        elif len(file2) > len(file1) and len(file2) > len(file3):
            f_total.write(path2 + '\n')
            f_total.write(str(len(file2)) + '\n')
            f_total.writelines(file2)
        elif len(file3) > len(file1) and len(file3) > len(file2):
            f_total.write(path3 + '\n')
            f_total.write(str(len(file3)) + '\n')
            f_total.writelines(file3)
    return

total_file()