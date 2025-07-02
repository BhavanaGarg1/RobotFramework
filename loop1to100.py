print(*range(1, 101), sep="\n")

# •	range(1, 101) lazily generates 1 → 100.
# •	The splat operator * unpacks that sequence into individual arguments for print.
# •	sep="\n" tells print to insert a newline between each argument.


list(map(print, range(1, 101)))

# •	map(print, sequence) calls print() once for every item.
# •	Wrapping with list() forces evaluation in CPython (otherwise the map object is lazy and
# nothing is printed).
