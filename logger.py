

def logUser(info):
    print(str(info))
    print("opening log...")
    data = open('./log.txt', 'a')
    text = data.read()
    print(text)
    data.write(info)
    data.close()
    return "LOG CREATED..."

