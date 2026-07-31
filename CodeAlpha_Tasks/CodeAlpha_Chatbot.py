#    simple Chatbot using Python



def chatbot_response(user):
    user = user.lower()



    if "hi" in user:

        return "Hello! How can I help you today?"



    elif "hello" in user:

        return "Hi there! What can I do for you?"

    

    elif "hey" in user:

        return "hey! Nice to meet you."



    elif "good morning" in user:

        return "Good morning! Hope you have a great day."

    

    elif "good afternoon" in user:

        return "Good afternoon! How can I assist you?"



    elif "good evening" in user:

        return "Good evening! What can I help you with?"



    elif "good night" in user:

        return "Good night! sweet dreams."



    elif "namaste" in user or "namaskar" in user:

        return "Namaste! Aap Kaise Hain."



    elif "i love you" in user:

        return "That's kind of you! I'm here to help and chat anytime."
    


    elif "how are you" in user:

        return "I'm doing well, Thanks you! How about you?"
    
    

    elif "what is your name" in user or "what's your name" in user or "your name" in user:

        return "My name is 'shree' and I'm your Chatbot Assistant."



    elif "who are you" in user or "who're you" in user:

        return "I'm a simple chatbot designed to answer your questions."



    elif "nice to meet you" in user:

        return "Nice to meet you too!😊"



    elif "are you human" in user:

        return "No, I'm an AI chatbot."



    elif "who made you" in user or "who is your creator" in user:

        return "I was created by a developer, Whose name is SHUBHAM."



    elif "what can you do" in user:

        return "I can answer question, provide information, and help with simple tasks."    



    elif "who am i" in user or "who i am" in user:

        return "You're a human being."



    elif "what is your religion" in user or "do you belive in god" in user:

        return "I am an Atheist, I don't belive in God or Religion."



    elif "what is your favorite color" in user or "what's your favorite color" in user:

        return "I don't have personal preferences, but Blue is a popular choice!"



    elif "what time is it" in user:

        return "Sorry, I don't have access to the current time unless connected to a clock service."



    elif "what is today's date" in user:

        return "I don't know today's date unless connected to a calendar or system clock."



    elif "what is our nationality" in user or "what's our nationality" in user:

        return "INDIAN"



    elif "suggest me a book" in user or "suggest me book" in user:

        return "The INDIAN CONSTITUTION book"



    elif "suggest me a college" in user or "suggest me college" in user:

        return "Dr. Bhimrao Ambedkar University, AGRA"



    elif "suggest me a song" in user or "suggest me song" in user:

        return "song--> Zara Sa"
    


    elif "what is ai" in user:

        return "Artificial Intelligence(AI) enables computers to perform tasks that usually require human intelligence."



    elif "what is python" in user:

        return "Python is a popular language known for its simplicity and versatility."


    elif "what is java" in user:

        return "Java is an object-oriented programming language widely used for Web, Desktop and Android development."



    elif "what is javascript" in user:

        return "JavaScript adds interactivity and dynamic behavior to websites."



    elif "i am bored" in user:

        return "If you want to hear a joke or interesting fact.\ntype(tell me a joke or a fun fact)"



    elif "tell me a joke" in user or "tell me joke" in user:

        return "Why don't programmers like nature? It has too many bugs! haha..😄"



    elif "you are funny" in user or "you're funny" in user:

        return "Haha, thanks! 😄"



    elif "tell me a fun fact" in user or "tell me fun fact" in user:

        return "Honey never spoils. Archaeologist have found edible honey in ancient Egyptian tombs."



    elif "tell me a quote" in user or "tell me quote" in user:

        return "'Success is the sum of small efforts repeated by day in and day out'"



    elif "can you learn" in user:

        return "I don't learn from conversations unless specifically designed to do so."



    elif "i need help" in user or "help" in user:

        return "Sure! Tell me what do you need help with?"



    elif "thank you" in user:

        return "You're welcome!😊"



    elif "thanks" in user:

        return "Happy to help!"



    elif "good job" in user:

        return "Thank you! I'm glad I could help."



    elif "see you later" in user:

        return "Take care, see you!"


    
    elif "bye" in user:

        return "Goodbye! Have a good day."
    
    

    else:

        return "Sorry, I didn't understand that."




print("Welcome to our Chatbot")
print("Chatbot : Hello! Type something (type 'bye' to exit)")



while(True):
    user_input = input("You : ")

    response = chatbot_response(user_input)

    print("Chatbot : ", response)

    if "bye" in user_input.lower():
        break


# code is end here