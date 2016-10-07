from random import choice

def make_grid(height, width):
    dice = ['CSOAHP', 'ABBOJO', 'ENSIUE', 'FSKFAP','EGAENE', 'YIDSTT', 'ATTOWO',
'TOESIS', 'RHTVWE', 'HLNNRZ', 'MTIOUC', 'NEEHGW', 'DIXRLE', 'YLDERV',
'QHMUNI', 'RETTYL']




    return {(row,col): choice(choice(dice))
                  for row in range (height)
                  for col in range(width)}


def neighbours_of_position((row,col)):
    return [ (row -1, col -1), (row - 1, col), (row - 1, col + 1),
             (row, col - 1),                    (row, col + 1),
             (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

def all_grid_neighbours(grid):
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours

def pos_to_letter(grid, p):
    return 'QU' if grid[p] == 'Q' else grid[p]

    # if grid[pos] == 'Q':
    #     return 'QU'
    # else:
    #     return grid[pos]


def path_to_word(grid, path):
    return ''.join([pos_to_letter(grid, p) for p in path])

def is_a_real_word(word, dictionary):
    return word in dictionary

def search(grid, dictionary):
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary

    def do_search(path):
        word = path_to_word(grid, path)
        if is_a_real_word(word, full_words):
            paths.append(path)
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])

    for position in grid:

        do_search([position])

    words = []

    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)

def get_dictionary(dictionary_file):
    full_words, stems = set(), set()

    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)

            for i in range(1, len(word)):
                stems.add(word[:i])

        return full_words, stems

def display_grid (grid):
    height, width = max(grid)
    height +=1
    width +=1


    for r in range(height):
        rowAsText = " ".join(grid[(r,c)] for c in range(width))
        print rowAsText






def display_words(words):
    for word in words:
        print word
    print ", ".join(words)
    longest = max(words, key=lambda w: len(w))
    print "Found {0} words".format(len(words))
    print longest + " is the longest word found"

def check():
 return 1

def main():
    grid = make_grid(4,4)
    dictionary = get_dictionary('bogwords.txt')
    words = search(grid, dictionary)
    display_words(words)
    display_grid(grid)



main()