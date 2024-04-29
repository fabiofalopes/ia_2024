

'''
    Mini teste materia até BSA e DSA

'''


# Ultima aula 
BSA - Basic Search Algorithm
DSA - Depth Search Algorithm

'''markdown
    
'''

'''python
g = {
    'A': ['B', 'C', 'E'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['D', 'F'],
    'F': ['C'],
    'G': ['F'],
    'H': []
}
'''

# BFS

1ª 
[('A', ['A'])]

2ª
[('B', ['A' , 'B'])]
[('C', ['A', 'C'])]
[('D', ['A' , 'E'])]

3ª
[('E', ['A' , 'B' ,])]
[('C', ['A', 'C'])]
[('D', ['A' , 'E'])]

[('E', ['A' , 'B'])]
[('C', ['A', 'C'])]
[('D', ['A' , 'E'])]







[('B', ['A', 'B'])]
[('C', ['A', 'C']), ('B', ['A', 'B'])]
[('E', ['A', 'E']), ('C', ['A', 'C']), ('B', ['A', 'B'])]