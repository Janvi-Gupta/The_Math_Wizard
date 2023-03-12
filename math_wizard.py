operation = {"substract": "-", "multiple": "*", "division": "/", "plus": "+", "equals": "=", "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}

with open("TMW_small.txt", "r") as f:
  read = f.readlines()

lst = []
for i in range(1, len(read)):
    lst.append(read[i].split())

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] in operation:
            lst[i][j] = operation[lst[i][j]]

for i in range(len(lst)):
    # Perform division first
    while '/' in lst[i]:
        index = lst[i].index('/')
        num1 = int(lst[i][index-1])
        num2 = int(lst[i][index+1])
        result = num1 / num2
        lst[i] = lst[i][:index-1] + [result] + lst[i][index+2:]

    while '*' in lst[i]:
        index = lst[i].index('*')
        num1 = int(lst[i][index-1])
        num2 = int(lst[i][index+1])
        result = num1 * num2
        lst[i] = lst[i][:index-1] + [result] + lst[i][index+2:]
    
    while '+' in lst[i]:
        index = lst[i].index('+')
        num1 = int(lst[i][index-1])
        num2 = int(lst[i][index+1])
        result = num1 + num2
        lst[i] = lst[i][:index-1] + [result] + lst[i][index+2:]

    before_eq = str(lst[i][0])
    after_eq = str(lst[i][-1])
    if before_eq.isdigit():
      before_eq = int(before_eq)
    if after_eq.isdigit():
      after_eq = int(after_eq)

    res = ""
    if before_eq == after_eq:
      res = "True"
    else:
      res = "False"
  
    file = open("output.txt", "a")
    file.write(res)
    file.close()
    
file = open("output.txt", "r")
file.readlines()
