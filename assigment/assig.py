# Assignment 1 - Python Basics
 

num1 = 5
num2 = -10
print("Integer examples:", num1, num2)


price = 3.14
temperature = -0.5
print("Float examples:", price, temperature)


city_name = "Karachi"
print("String example:", city_name)


is_happy = True
is_raining = False
print("Boolean examples:", is_happy, is_raining)
print()

# 2. Create three variables: name, age, city and print them.
name = "Gargi"
age = 20
city = "Jaipur"
print("Question 2 output:")
print("Name:", name)
print("Age:", age)
print("City:", city)
print()

# 3. Take a user's name as input, print uppercase and total length.
user_name = input("Enter your name: ")
print("Name in uppercase:", user_name.upper())
print("Total number of characters:", len(user_name))
print()

# 4. Explain five commonly used string methods in Python with examples.

text = "hello"
print("upper() example:", text.upper())


text2 = "WORLD"
print("lower() example:", text2.lower())


text3 = "  good morning  "
print("strip() example:", text3.strip())


text4 = "I like apples"
print("replace() example:", text4.replace("apples", "bananas"))


text5 = "one two three"
print("split() example:", text5.split())
print()

# 5. Create a list of five fruits and print required details.
fruits = ["apple", "banana", "mango", "grapes", "orange"]
print("Fruit list:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Total number of fruits:", len(fruits))
print()

# 6. Create and update a number list.
numbers = [10, 20, 30, 40, 50]
numbers.append(60)    # Add 60 to the list.
numbers.remove(20)    # Remove 20 from the list.
print("Updated number list:", numbers)
print()

# 7. What is Artificial Intelligence (AI)?
# AI is the ability of machines to do tasks that normally need human thinking.
# AI is important because it helps us solve problems faster and improve daily life.
# Four real-life applications of AI:
# 1. Voice assistants like Alexa and Siri.
# 2. Self-driving cars.
# 3. Medical diagnosis systems.
# 4. Online shopping recommendations.
print("AI explanation:")
print("AI means machines can learn and make decisions like people.")
print("AI is useful because it saves time and makes work easier.")
print("Examples: voice assistants, self-driving cars, medical help, shopping suggestions.")
print()

# 8. Identify whether these are examples of AI and why.
print("AI examples:")
print("ChatGPT: Yes, it is AI because it can understand text and answer questions.")
print("Google Maps route prediction: Yes, it is AI because it uses data to choose the best route.")
print("Calculator: No, it is not AI because it only does fixed math without learning.")
print("Netflix recommendations: Yes, it is AI because it suggests shows based on user choices.")
print("Voice assistants (Alexa/Siri): Yes, they are AI because they listen and respond like a helper.")