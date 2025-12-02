# Voice AI - Learner / Builder
def welcome():
    print("Welcome to Voice AI!")
    profile = input("Are you a Learner or Builder? ").lower()
    
    if profile == "learner":
        topic = input("What topic do you want to learn? ")
        print(f"Great! I will help you learn {topic}.")
    elif profile == "builder":
        project = input("What project do you want to code? ")
        print(f"Awesome! I will help you build {project}.")
    else:
        print("Unknown profile. Please choose Learner or Builder.")

# Launch
welcome()
