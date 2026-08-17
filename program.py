from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")
    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")
    @Rule(StudentFacts(likes='AI'), StudentFacts(likes='Programming'))
    def aids(self):
        print("Suggested Career Path: AIDS Engineering")
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Graphics'))
    def civil(self):
        print("Suggested Career Path: CIVIL Engineering")
        

def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    print("1. Maths")
    print("2.Physics ")
    print(  "3. Programming \n")
    print( "4.Biology \n")
    print(  "5. Chemistry \n")
    print(   "6. Circuits \n")
    print( "7. AI \n")
    print(  "8. Graphics \n") 
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()


	

