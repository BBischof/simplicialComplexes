# Simplicial Complexes 

For working with simplicial complexes, one has need for some little scripts. I intend on implementing a series of such scripts in this repo. 

## Simplicial Complex Format

I have decided to use a JSON format as a convenient way to store simplicial complex data. In particular, keys are the dimensions of simplexes, and the values are lists of simplexes. Each simplex is a list itself of vertices included. Thus, the length of a list representing a vertex is equal to 1 greater than its dimension. 

E.g.:
```
{0: [[1],[2],[3]], 1: [[1,2], [2,3], [3,1]], 2: [[1,2,3]]}
```
represents a simplicial complex with three vertices, three 1-cells, and one 2-cell.

## Functions:

List of implemented functions:
- reorderJSON(unorderedSimplex): returns Boolean
- validateJSON(unorderedSimplex): returns Dictionary
