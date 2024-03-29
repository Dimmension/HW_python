def postfixForm():
    arr = list(input().split())
    #важно создать новый массив, иначе не будет работать
    res = []
    for symbol in arr:
        if symbol.isdigit():
            res.append(int(symbol))
        else:
            a = int(res.pop())
            b = int(res.pop())
            match symbol:
                case '*':
                    result = b*a
                case '/':
                    result = b/a
                case '-':
                    result = b-a
                case '+':
                    result = b+a
            res.append(result)
    return res.pop()


print(postfixForm())
