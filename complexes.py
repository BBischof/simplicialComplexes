# A simplex in JSON format:

# {0: [[1],[2],[3]], 1: [[1,2], [2,3], [3,1]], 2: [[1,2,3]]}

#a simple recursive powerset function
def powerset(elements):
    if len(elements) > 0:
        head = elements[0]
        for tail in powerset(elements[1:]):
            yield [head] + tail
            yield tail
    else:
        yield []

#validates if a json object is a simplicial complex by the following definition:
# Let V={1,2,…,n}V={1,2,…,n}. Let ΣΣ be a set of non-empty subsets of VV. 
# We call ΣΣ an Abstract Simplicial Complex if it has the following property: 
# whenever a set A∈ΣA∈Σ, every nonempty subset of AA is also an element of ΣΣ.
def validateJSON(simplex):
	for dim in simplex:
		if dim > 0:
			for j in range(len(simplex[dim])):
				simplex[dim][j]=sorted(simplex[dim][j])
			for sig in simplex[dim]:
				for p in powerset(sig):
					if len(p) == (len(sig)-1):
						if p not in simplex[len(p)-1]:
							print "The face: " + str(sig) + " is missing: " + str(p) + ", found: " + str(simplex[len(p)-1])
							return False
	return True

#ensures all simplices are sorted lists, useful for other functions.
def reorderJSON(unorderedSimplex):
	for dim in unorderedSimplex:
		if dim > 0:
			for j in range(len(unorderedSimplex[dim])):
				unorderedSimplex[dim][j]=sorted(unorderedSimplex[dim][j])
	return unorderedSimplex

