arr = []
ls = list()
count = 0
sum = 0.0
i = 0
while 1:
    val = input('������һ������')
    max = min = val
    try:

        if val == 'done':
            for i in range(len(arr)):
                a = int(arr[i])
                sum = sum + arr[i]
                ls.append(a)
            ls.sort()

            m = int(len(ls)) - 1
            ave = sum / int(len(ls))
            print("count :", len(ls))
            print("min :", ls[0])
            print("max :", ls[m])
            print("sum :", sum)
            print("avg :", ave)
            exit()
        else:
            float(val)
            arr.append(float(val))
            count = count + 1
    except ValueError:
        print('�Ƿ�����')
        print(ValueError)
        pass