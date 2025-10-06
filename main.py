def chatbot():
    print("Chatbot: Hello! I’m your assistant. Ask me anything!")
    print("Type 'exit' to end the chat.\n")

    qa = {
        "hi": "Hello there! How can I help you today?",
        "hello": "Hi! What’s up?",
        "how are you": "I’m just a bunch of code, but I’m doing great!",
        "your name": "I’m your Python chatbot assistant!",
        "who created you": "I was created using Python.",
        "bye": "Goodbye! Have a great day!",
        "python": "Python is a high-level programming language known for its simplicity and readability.",
        "ai": "AI stands for Artificial Intelligence — it makes machines think and learn like humans.",
        "machine learning": "Machine Learning is a part of AI that allows systems to learn from data.",
        "deep learning": "Deep Learning uses neural networks to process complex data patterns.",
        "data science": "Data Science involves analyzing and interpreting large data sets to extract insights.",
        "chatbot": "A chatbot is a program that simulates human conversation using text or speech.",
        "sql": "SQL stands for Structured Query Language, used for managing relational databases.",
        "database": "A database stores and organizes structured information for easy access.",
        "cloud computing": "Cloud computing provides computing services like storage and servers over the internet.",
        "iot": "IoT stands for Internet of Things — connecting physical devices to the internet.",
        "big data": "Big Data refers to very large data sets analyzed for insights and patterns.",
        "data mining": "Data mining extracts meaningful patterns from large datasets.",
        "algorithm": "An algorithm is a set of instructions designed to perform a task or solve a problem.",
        "neural network": "A neural network mimics the human brain’s neurons to process information.",
        "gpu": "A GPU is used to speed up computation, especially in AI and deep learning.",
        "api": "API stands for Application Programming Interface, allowing different systems to communicate.",
        "html": "HTML stands for HyperText Markup Language, used to structure web pages.",
        "css": "CSS stands for Cascading Style Sheets, used to style web pages.",
        "javascript": "JavaScript is a programming language for adding interactivity to websites.",
        "react": "React is a JavaScript library for building user interfaces.",
        "firebase": "Firebase is Google’s platform for building web and mobile apps.",
        "json": "JSON stands for JavaScript Object Notation — a lightweight data format.",
        "csv": "CSV stands for Comma Separated Values — used for tabular data storage.",
        "join": "SQL JOIN combines records from two or more tables based on a related column.",
        "primary key": "A Primary Key uniquely identifies each record in a table.",
        "foreign key": "A Foreign Key links one table to another using a key relationship.",
        "normalization": "Normalization organizes data to minimize redundancy in databases.",
        "oops": "OOP means Object-Oriented Programming — based on classes and objects.",
        "inheritance": "Inheritance allows one class to derive features from another class.",
        "polymorphism": "Polymorphism lets one interface be used for different data types.",
        "encapsulation": "Encapsulation hides data within a class, exposing only necessary parts.",
        "abstraction": "Abstraction hides unnecessary details while showing essential features.",
        "compiler": "A compiler converts high-level code into machine code before execution.",
        "interpreter": "An interpreter executes code line by line.",
        "ide": "IDE stands for Integrated Development Environment — helps in writing and debugging code.",
        "debugging": "Debugging means finding and fixing errors in your code.",
        "version control": "Version control tracks and manages code changes over time.",
        "git": "Git is a version control system used to track code changes.",
        "github": "GitHub is a cloud platform for hosting and collaborating on Git projects.",
        "operating system": "An OS manages computer hardware and software resources.",
        "cpu": "CPU stands for Central Processing Unit — the main processor of a computer.",
        "ram": "RAM is temporary memory that stores data while programs are running.",
        "ip address": "An IP address identifies a device on a network uniquely.",
        "framework": "A framework provides a foundation for developing software applications.",
        "dataset": "A dataset is a collection of related data used for analysis or training models.",
    }

    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Chatbot: Bye! Take care.")
            break

        response = None
        for key, value in qa.items():
            if key in user_input:
                response = value
                break

        if response:
            print("Chatbot:", response)
        else:
            print("Chatbot: Sorry, I don’t know that. Can you ask something else?")


chatbot()
