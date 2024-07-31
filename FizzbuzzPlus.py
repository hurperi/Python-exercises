for i in range(1,101):
    output = ""
    if i%3 == 0 or '3' in str(i):
        output += "Fizz"
    if i % 5 == 0 or '5' in str(i):
        output += "Buzz"
    if i%7 == 0 or '7' in str(i):
        output+= "Bazz"
    
    if output == "":
        print(i)
    
    else:
        print(output)
    