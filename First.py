#first_name = "Eklavya"
#age = 18
#distance_from_hostel = 3.3 
#is_hostel_nearby = True

#if is_hostel_nearby:
#    print(age,"hello",)
#else:
#   print("None of your business")

#import math

#print(math.pi)
#print(math.e)

#x = 250

#result = math.sqrt(x)

#print(result)

#height = float(input("Enter height of the triangle: "))
#base = float(input("Enter base length of the triangle: "))

#hypotenuse = height ** 2 + base **2

#print(round(hypotenuse, 2))


#x = input("Enter your number: ")

#print(x) 

#sentence = input("Enter a sentence: ")
#vowels = "aAeEiIoOuU"
#count1 = 0
#count2 = 0
#for char in sentence:
#    if char in vowels:
#        count1 += 1
#    else:
#        count2 += 1
#denom = count1 + count2
#result1 = count1 / denom * 100
#result2 = count2 / denom * 100
#print(f"Percentage of vowels is {result1:.2f}% and of consonants are {result2:.2f}%")

#sentence = input("Enter your Sentence: ")
#words = sentence.split()
#vowels = "aAiIoOeEuU"

#max_vowel_count = 0
#word_with_vowel_count = ""

#for word in words:
#    count = 0
#    for char in word:
#        if char in vowels:
#           count += 1
#
#if count > max_vowel_count:
#    max_vowel_count = count
#    word_with_vowel_count = word
#
#print(max_vowel_count , word_with_vowel_count)

#word = input("Enter a word: ")
#cased_word = word.lower()
#reversed_word = cased_word[::-1]
#if reversed_word == cased_word:
#    print("Positive")
#else:
#    print("Negative")

#num = int(input("Enter a number: "))
#result = num % 2
#if result == 0:
#    print("Even")
#else:
#    print("Odd")

#num = int(input("Enter a number: "))
#if num > 0:
#    print("positive")
#elif num == 0:
#    print("its a zero")
#else:
#    print("negative")

#num = int(input("Enter a number: "))
#x = int(input("Enter the number of multiplications: "))

#for y in range(1,x + 1):
#    print(y * num)

#for x in range(1,5):
#    for y in range(x):
#        print("*", end="")
#    print()
name = input("enter your name: ")
x = name.strip(" ")

print(type(x),x)
