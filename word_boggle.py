from copy import copy

def buildTrie(node, depth, pos, visited, TheGrid, maxDepth):
	if (pos in visited):
		return
	visited.append(pos)
	letter = TheGrid[pos]
	if not letter in node:
		node[letter] = []
	node[letter].append({})
	depth += 1
	if (depth > maxDepth):
		return
	for neighbour in adjacencies[pos]:
		# last element in node is the dict we just appended
		# thus, index with -1
		buildTrie(node[letter][-1], depth, neighbour, copy(visited), TheGrid, maxDepth)

def inTrie(trie, word):
	if word[0] not in trie:
		return False

	if len(word) == 1:
		return True

	canMakeWord = False
	for nextLetter in trie[word[0]]:
		canMakeWord = inTrie(nextLetter, word[1:])
		if canMakeWord:
			break
	return canMakeWord

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
	h = int(dims[0])
	w = int(dims[1])
	boggleValues = input()

	TheGrid = boggleValues.split()
	# print(TheGrid)
	adjacencies = buildAdjacencies(w, h)
	# for adj in adjacencies:
		# print(adj)

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