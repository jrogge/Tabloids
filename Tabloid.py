import itertools as it

# partition class?
# NB: 0-indexing
class Tabloid:
    def __init__(self, shape, row_list):
        '''
        shape is a partition of some n
        row_list is a list of row sets of the tabloid
        '''
        self.shape = shape
        self.row_list = row_list
        self.n = 0
        for length in shape:
            self.n += length
        self.lex_comp = self.compute_lex_comp()
        self.dom_seq = self.compute_dom_seq()

    def __str__(self):
        return str(self.row_list)

    def compute_lex_comp(self):
        '''
        return the composition series used in the lexicographical ordering
        '''
        comp = [0] * self.n
        for row_ind, row in enumerate(self.row_list):
            for val in row:
                comp[val] = row_ind

        return comp

    def compute_dom_seq(self):
        '''
        return the sequence of compositions used in the dominance ordering
        '''
        # need list comprehension of [[0] * a] * b] because python uses
        # shallow lists apparently
        seq = [[0 for i in range(len(self.shape))] for i in range(self.n)]
        for row_ind, row in enumerate(self.row_list):
            for val in row:
                # increment <row> in the first <val> partitions
                for i in range(val, self.n):
                    seq[i][row_ind] += 1

        return seq

    def is_lex_greater(self, other):
        '''
        return self >_lex other
        '''
        for i in range(self.n):
            if self.lex_comp[i] < other.lex_comp[i]:
                return True
            elif self.lex_comp[i] > other.lex_comp[i]:
                return False

        return False

def merge_sort(A,B):
    #print("merge call: (", ",".join(map(str, A)), ")\n(",
    #        ",".join(map(str, B)), ")")
    A_sorted = []
    B_sorted = []
    if (len(A) < 2):
        A_sorted = A
    else:
        A_sorted = merge_sort(A[:len(A)//2], A[len(A)//2:])
    if (len(B) < 2):
        B_sorted = B
    else:
        B_sorted = merge_sort(B[:len(B)//2], B[len(B)//2:])

    A_ptr = 0
    B_ptr = 0
    out = []
    #print("==Merging==")
    #print("(", ",".join(map(str, A)), ")\n(",
    #        ",".join(map(str, B)), ")")
    while (A_ptr < len(A_sorted) and B_ptr < len(B_sorted)):
        #print("A:", A_sorted[A_ptr], "\tB:", B_sorted[B_ptr])
        if (A_sorted[A_ptr].is_lex_greater(B_sorted[B_ptr])):
            #print("add B")
            out.append(B_sorted[B_ptr])
            B_ptr += 1
        else:
            #print("add A")
            out.append(A_sorted[A_ptr])
            A_ptr += 1
    # either A or B will have been exhausted first, add rest of other
    if A_ptr == len(A):
        out += B_sorted[B_ptr:]
    else:
        out += A_sorted[A_ptr:]

    #print("Out:", ",".join(map(str, out)))
    return out

#A1_shape = [4]
#A1_rl = [[0,1,2,3]]
#A1 = Tabloid(A1_shape, A1_rl)
#print("A1:", A1)
#print("lex comp:", A1.lex_comp)
##print("dom seq:", A1.dom_seq)
#
#A12_shape = [2,1,1]
#A12_rl = [[2,3],[1],[0]]
#A12 = Tabloid(A12_shape, A12_rl)
#print("A12:", A12)
#print("lex comp:", A12.lex_comp)
##print("dom seq:", A12.dom_seq)
#
#print("A1 >_lex A12:", A1.is_lex_greater(A12))
#print("A12 >_lex A1:", A12.is_lex_greater(A1))

#def gen_tabloids(shapes, n):
#    '''
#    shapes is a list of partitions of n
#    for each shape, generate every tabloid of that shape
#    '''
#    it_str = ''
#    for i in range(n):
#        it_str += str(i)
#
#
#shapes_3 = [(3), (2,1), (1,1,1)]
#tabloids = []
#sorted_t = merge_sort(tabloids, [])
#for tab in sorted_t:
#    print(tab.row_list, tab.lex_comp)
