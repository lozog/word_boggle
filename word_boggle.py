def buildTrie(node, depth, pos, visited, TheGrid, maxDepth):
	visited.append(pos)
	letter = TheGrid[pos]
	node[letter] = {}
	depth += 1
	if (depth > maxDepth):
		return
	for neighbour in adjacencies[pos]:
		# TODO: what if 2 neighbours are the same letter?
		buildTrie(node[letter], depth, neighbour, visited, TheGrid, maxDepth)

def inTrie(trie, word):
	if word[0] not in trie:
		return False

	if len(word) == 1:
		return True
	return inTrie(trie[word[0]], word[1:])

def buildAdjacencies(w, h):
	adjacencies = []
	for row in range(h):
		for col in range(w):
			pos = row*w + col
			adjacencies.append([])
			if col > 0: # if not in left col
				adjacencies[pos].append(row*w + (col-1))
				if row > 0: # up left
					adjacencies[pos].append((row-1)*w + (col-1))
				if row < h-1: # down left
					adjacencies[pos].append((row+1)*w + (col-1))
			if col < w-1: # if not in right col
				adjacencies[pos].append(row*w + (col+1))
				if row > 0: # up right
					adjacencies[pos].append((row-1)*w + (col+1))
				if row < h-1: # down right
					adjacencies[pos].append((row+1)*w + (col+1))
			if row > 0: # if not in top row
				adjacencies[pos].append((row-1)*w + col)
			if row < h-1: # if not in bottom row
				adjacencies[pos].append((row+1)*w + col)
	return adjacencies

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
	print(TheGrid)
	adjacencies = buildAdjacencies(w, h)

	# using nested dicts for the trie
	TheTrie = {}

	# this will be the max depth of the trie
	maxWordLen = max(len(word) for word in dictionary)

	# build the trie
	for pos,letter in enumerate(TheGrid):
		buildTrie(TheTrie, 0, pos, [], TheGrid, maxWordLen)

	# print words from dictionary that can be formed from the grid
	for word in dictionary:
		if inTrie(TheTrie, word):
			print("{} ".format(word), end='')
	print('')