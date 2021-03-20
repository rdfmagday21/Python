def main():
    
    numbers = []
    userInput = input("Enter elements: ")
    if len(numbers) == None:
        median(numbers)
        mode(numbers)
        mean(numbers)
    else:
        elements = userInput.split()
        for i in elements:
            numbers.append(int(i))
        median(numbers)
        mode(numbers)
        mean(numbers)

def median(numbers):
    if len(numbers) == 0:
        return 0
    else:
        numbers.sort()
        midpoint = len(numbers) // 2
        print("The median is", end =" ")
        if len(numbers) % 2 == 1:
            print(numbers[midpoint])
        else:
            print((numbers[midpoint] + numbers[midpoint - 1]) / 2)
def mode(numbers):
    if len(numbers) == 0:
        return 0
    else:
        numberDictionary = {}
        for i in numbers:
            number = numberDictionary.get(i, None)
            if number == None:
                numberDictionary[i] = 1
            else:
                numberDictionary[i] = number + 1

        theMaximum = max(numberDictionary.values())
        for key in numberDictionary:
            if numberDictionary[key] == theMaximum:
                print("The mode is", key)
                break
def mean(numbers):
    if len(numbers) == 0:
        return 0
    else:
        sum = 0
        for i in range(0, len(numbers)):
            sum = sum + numbers[i]
        print("The mean is", sum/len(numbers))
         
if __name__ == "__main__":
    main()