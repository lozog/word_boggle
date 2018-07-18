def buildTrie(node, depth, pos, visited, TheGrid, maxDepth):
	visited.append(pos)
	letter = TheGrid[pos]
	node[letter] = {}
	depth += 1
	if (depth > maxDepth):
		return
	for neighbour in adjacencies[pos]:
		buildTrie(node[letter], depth, neighbour, visited, TheGrid, maxDepth)

def inTrie(trie, word):
	if word[0] not in trie:
		return False

	if len(word) == 1:
		return True
	return inTrie(trie[word[0]], word[1:])


# adjacency list
# TODO: this assumes a 3x3 grid. need to generalize for any size
# 0 1 2
# 3 4 5
# 6 7 8
adjacencies = [
	[1, 3, 4],
	[0, 2, 3, 4, 5],
	[1, 4, 5],
	[0, 1, 4, 6, 7],
	[0, 1, 2, 3, 5, 6, 7, 8],
	[1, 2, 4, 7, 8],
	[3, 4, 7],
	[3, 4, 5, 6, 8],
	[4, 5, 7]
]

# read in input (assumes well-formed input)
T = int(input())
for i in range(T):
	dictLen = int(input())
	dictionary = input().split()
	dims = input().split()
	w = int(dims[0])
	h = int(dims[1])
	boggleValues = input()
	TheGrid = boggleValues.split()

	# T = 1
	# dictLen = 4
	# dictionary = ['GEEKS', 'FOR', 'QUIZ', 'GO']
	# w = 3
	# h = 3
	# boggleValues = "G I Z U E K Q S E"
	# TheGrid = boggleValues.split()

	# using nested dicts for the trie
	TheTrie = {}

	# this will be the max depth of the trie
	maxWordLen = max(len(word) for word in dictionary)

	# build the trie
	for pos,letter in enumerate(TheGrid):
		buildTrie(TheTrie, 0, pos, [], TheGrid, maxWordLen)

	for word in dictionary:
		if inTrie(TheTrie, word):
			print("{} ".format(word), end='')
	print('')
