def main():
    programming_classes = ('Intro to Python', 
                           'Advanced Python', 
                           'Database Essentials', 
                           'Web Development Basics', 
                           'Data Structures in Python', 
                           'Web Design Fundamentals')
    
    # Loop to print each class
    for course in programming_classes:
        print(course)
    
    print("\nTotal number of classes:", len(programming_classes))
main()