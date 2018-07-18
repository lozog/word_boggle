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

T = 1
dictLen = 4
dictionary = ['GEEKS', 'FOR', 'QUIZ', 'GO']
w = 3
h = 3
boggleValues = "G I Z U E K Q S E"
TheGrid = boggleValues.split()

# using nested dicts for the trie
TheTrie = {}

# this will be the max depth of the trie
maxWordLen = max(len(word) for word in dictionary)

# build the trie
for pos,letter in enumerate(TheGrid):
	buildTrie(TheTrie, 0, pos, [], TheGrid, maxWordLen)

# quick test
print(inTrie(TheTrie, "GEEKY"))
