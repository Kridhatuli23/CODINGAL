medical_cause=input("Did you have a medical cause? (Y/N): ").strip().upper()
if medical_cause=="Y": 
    print("You are allowed")
else:
    attend=int(input("Enter the attendance of the student: "))
    if attend>=75:
        print("You are allowed")
    else:
        print("You aren't allowed")