# Python program for the above approach

# Function to find the remaining
# two rectangle coordinates
def Create_Rectangle(arr, n):

	for i in range(n):
		arr[i] = [i for i in arr[i]]

	# Pairs to store the position of given
	# two coordinates of the rectangle.
	p1 = [-1, -1]
	p2 = [-1, -1]

	# Pairs to store the remaining two
	# coordinates of the rectangle.
	p3 = []
	p4 = []

	# Traverse through matrix and
	# find pairs p1 and p2
	for i in range(n):
		for j in range(n):
			if (arr[i][j] == '1'):
				if (p1[0] == -1):
					p1 = [i, j]
				else:
					p2 = [i, j]

	p3 = p1
	p4 = p2

	# First Case
	if (p1[0] == p2[0]):
		p3[0] = (p1[0] + 1) % n
		p4[0] = (p2[0] + 1) % n
	# Second Case
	elif (p1[1] == p2[1]):
		p3[1] = (p1[1] + 1) % n
		p4[1] = (p2[1] + 1) % n
	# Third Case
	else:
		p3[0], p4[0] = p4[0],p3[0]

	arr[p3[0]][p3[1]] = '1'
	arr[p4[0]][p4[1]] = '1'

	# Print the matrix
	for i in range(n):
		print("".join(arr[i]))


# Driver code
if __name__ == '__main__':
	# Given Input
	n = 4
	arr = ["0010", "0000", "1000", "0000"]

	# Function Call
	Create_Rectangle(arr, n)

# This code is contributed by mohit kumar 29.
