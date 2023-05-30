import re


responses = {
    r"hi|hello|hey": ["Welcome to our Book-Store! How can I assist you?"],
    r"menu|bookslist": ["Our Book-Store includes a variety of books, such as Programming Books and Science Books."],
    r"available": ["Sure, let me check availability. Please enter a book name."],
    r"hours": ["We're open from 10am to 10pm every day."],
    r"location|directions": ["We're located at 123 Main Street in Nashik. Can I help with directions?"],
    r"thanks|thank you": ["You're welcome!"],
    r"engineering": ["We offer a variety of Bachelor of Engineering and Master of Engineering books, including Computer, IT, and EN & TC Engineering books."],
    r"payment": ["We have both offline and online payment modes available."],
    r"programming": ["OOP - Rs. 500, CPP - Rs. 300, C - Rs. 200, Java - Rs. 700"],
    r"science": ["Physics - Rs. 500, Chemistry - Rs. 300, Biology - Rs. 200, Mathematics - Rs. 700"],
    r"python": ["Sorry, this book is out of stock!"]
}

def match_response(user_input):
    for pattern, response in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return ["I'm sorry, I didn't understand your request. Please try again."]

domain = "Book-Store"
print("Welcome to our Book-Store. How can I assist you?")

while True:
    user_input = input("You: ")
    response = match_response(user_input)
    print("Bot: ", response[0])

