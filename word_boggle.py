# adjacency list
# 0 1 2
# 3 4 5
# 6 7 8
adj = {
	[ [1, 3, 4],
		[0, 2, 3, 4, 5],
		[1, 4, 5]],
	[ [0, 1, 4, 6, 7],
		[0, 1, 2, 3, 5, 6, 7, 8],
		[1, 2, 4, 7, 8]],
	[ [3, 4, 7],
		[3, 4, 5, 6, 8],
		[4, 5, 7]]
}

T = 1
dictLen = 4
dictionary = ['GEEKS', 'FOR', 'QUIZ', 'GO']
w = 3
h = 3
boggleValues = "G I Z U E K Q S E"

# read boggleValues into grid
TheGrid = []
for i in range(w):
	TheGrid.append([''] * h)

i = 0
row = 0
col = 0
for letter in boggleValues:

	# skip invalid characters
	# assuming 26-char alphabet
	if (letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
		continue
	
	TheGrid[row][col] = letter

	col += 1
	if (col > w-1):
		row += 1
		col = 0

