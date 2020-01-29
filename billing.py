Name=input("Enter the name:")
def fare(location,destination,facility):
    if facility=="ac":
        cost=25
        kms=250
        totalcost=kms*cost
        print("Amount to pay",totalcost)
    elif facility=="nonac":
        cost=10
        kms=250
        totalcost=kms*cost
        print("Amount to pay",totalcost)
    else:
        return 0
location=input("Enter the location:")
destination=input("Enter the destination:")
facility=input("enter the facility:")
fare(location,destination,facility)
print("********************")
print("Name:",Name)
print("Location:",location)
print("Destination:",destination)

