if __name__ == '__main__':
	# Request the 5 ratings from the user
	print("Enter First Grade")
	rating1 = float(input())
	print("Enter the second grade")
	rating2 = float(input())
	print("Enter the third grade")
	rating3 = float(input())
	print("Enter the fourth grade")
	rating4 = float(input())
	print("Enter the fifth grade")
	rating5 = float(input())
	# Calculate the average
	average = (rating1+rating2+rating3+rating4+rating5)/5
	# Show the result
	print("The average of the 5 ratings is:",average)