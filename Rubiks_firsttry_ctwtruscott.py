""" There is symmetry for the problem and synonymous moves, and moves that lead to an infinite graph, such as four rotations then four rotations of the same move, of the 6 times 3 turn moves. Matrix representation and coordinates of reference, directional inference. Data representation is unique. Rotation moves not completely done. Just a start done in time of the first 30 minutes after NYE 2023 Jan 1st 2024. Matrix system eventually working in all rotations of the Rubiks (3 * 6) * (3 * 5) subsequent moves. Revision 1, 5 a.m. January 1st 2024 with a cup of tea. Based on matrix arrangements of permutations of states. I solved it so it would be in a queue and that for each subsequent state each subsequent state would be pushed onto the heap and automatically searched until the solved state was found. Powers of 18 to powers of 15 (non inclusive) or 18^d edges populate the graph where d is the depth of the graph. Going to work in a breadth-first search when all matrix rotations of the 2 x 2 are solved into lambdas calling defined functions. May need refactoring and going to draw a graph with diameter 18^d for d = 1, 2, 3 on paper. Charles Truscott"""

# Charles Thomas Wallace Truscott 

def print_state(Rubiks):
	print("Front Face: {}\n Right Face: {}\n Left Face: {}\n Back Face: {}\n Upper Face: {}\n Down Face: {}\n".format(Rubiks[0], Rubiks[1], Rubiks[3], Rubiks[2], Rubiks[4], Rubiks[5]))

def FRU_1_1(Rubiks: list):
	pass
def FRU_1_2(Rubiks: list):
	pass
def FRU_1_3(Rubiks: list):
	pass
def FRU_2_1(Rubiks: list):
	pass
def FRU_2_2(Rubiks: list):
	pass
def FRU_2_3(Rubiks: list):
	pass
def WL_1_1(Rubiks: list):
	pass
def WL_1_2(Rubiks: list):
	pass
def WL_1_3(Rubiks: list):
	pass
def WL_2_1(Rubiks: list):
	pass
def WL_2_2(Rubiks: list):
	pass
def WL_2_3(Rubiks: list):
	pass
def HL_1_1(Rubiks: list) -> list:
	pass
def HL_1_2(Rubiks: list):
	pass
def HL_1_3(Rubiks: list):
	pass
def HL_2_1(Rubiks: list) -> list:
	SingleStateUF = (Rubiks[4][1][0], Rubiks[4][1][1])
	SingleStateLF = (Rubiks[3][0][1], Rubiks[3][1][1])
	Rubiks[3][0][1] = Rubiks[5][1][0]; Rubiks[3][1][1] = Rubiks[5][1][1]
	Rubiks[4][1][0] = SingleStateLF[0]; Rubiks[4][1][1] = SingleStateLF[1]
	Rubiks[0][0][0], Rubiks[0][0][1],Rubiks[0][1][0], Rubiks[0][1][1] = Rubiks[0][1][0], Rubiks[0][0][0], Rubiks[0][1][1], Rubiks[0][0][1]
	Rubiks[5][1][0], Rubiks[5][1][1] = Rubiks[1][0][0], Rubiks[1][1][0]
	Rubiks[1][0][0] = SingleStateUF[0]
	Rubiks[1][1][0] = SingleStateUF[1]
	return Rubiks
def HL_2_2(Rubiks: list):
	pass
def HL_2_3(Rubiks: list):
	pass
def CharlesTruscott():
	FF = [["G", "G"], ["G", "G"]]
	BF = [["B", "B"], ["B", "B"]]
	LF = [["O", "O"], ["O", "O"]]
	RF = [["R", "R"], ["R", "R"]]
	UF = [["W", "W"], ["W", "W"]]
	DF = [["Y", "Y"], ["Y", "Y"]]
	RubiksCube = [FF, RF, BF, LF, UF, DF]
	print_state(RubiksCube)
	print("One solved move")
	print_state(LeftSideTurnedClosestFacing(RubiksCube))
	
CharlesTruscott()


""" Front Face: [['G', 'G'], ['G', 'G']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['B', 'B'], ['B', 'B']]
 Upper Face: [['W', 'W'], ['W', 'W']]
 Down Face: [['Y', 'Y'], ['Y', 'Y']]

One solved move
Front Face: [['G', 'G'], ['G', 'G']]
 Right Face: [['W', 'R'], ['W', 'R']]
 Left Face: [['O', 'Y'], ['O', 'Y']]
 Back Face: [['B', 'B'], ['B', 'B']]
 Upper Face: [['W', 'W'], ['O', 'O']]
 Down Face: [['Y', 'Y'], ['R', 'R']]


[Program finished]

"""

# Thank you Eric Grimson, John Guttag, Ana Bell and MITx and MIT OCW
