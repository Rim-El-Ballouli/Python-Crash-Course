with open('begin_to_knit.txt', encoding="utf8") as file_object:
    content = file_object.read()
    count = content.count('the')
    print(count)