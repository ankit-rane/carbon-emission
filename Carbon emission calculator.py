#Carbon footprint calculator of an individual or family.
print("Welcome to Personal carbon calculator. Please provide the following details");
print("If you are a u are a Non-vegetarian then input 1")
print("Else input any other valid number")
carbon_emission=0.0
family_members=float(input("Enter family members"))
food=float(input())
calories=float(input("Enter avg calories"))
if(food==1):
    carbon_emission += (calories*0.01)*family_members
else:
    carbon_emission += (calories*0.005)*family_members
driven_miles=float(input("Enter avg kms driven in a year"))
if(driven_miles>0):
    carbon_emission += driven_miles*0.01
else:
    print("enter valid kms driven")
household_utilities=float(input("Enter number of household utilities \nThey include 1)Electricity \n2)Natural Gas \n3)Fuel \n4)oil"))
total_expenditures=float(input("Enter total expenditures spent after the utilities"))
if(family_members>0&household_utilities>0&total_expenditures>0):
    carbon_emission += (0.12*total_expenditures)*household_utilities
else:
    print("enter valid details")
carbon_emission += ((0.12*total_expenditures)*household_utilities)*family_members
Print("your carbon emissions are"+carbon_emission+"metric tonnes")