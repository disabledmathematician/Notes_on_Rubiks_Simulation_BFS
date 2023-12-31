
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
	SingleStateUF = (Rubiks[4][0][0], Rubiks[4][0][1])
	SingleStateLF = (Rubiks[3][0][0], Rubiks[3][1][0])
	SingleStateRF = (Rubiks[1][0][1], Rubiks[1][1][1])
	Rubiks[3][0][0], Rubiks[3][1][0] = Rubiks[5][0][0], Rubiks[5][0][1]
	Rubiks[1][0][1], Rubiks[1][1][1] = Rubiks[4][0][0], Rubiks[4][0][1]
	Rubiks[5][0][0], Rubiks[5][0][1] = SingleStateRF[0], SingleStateRF[1]
	Rubiks[4][0][0], Rubiks[4][0][1] = SingleStateLF[0], SingleStateLF[1]
	SavedStateBF0 = (Rubiks[2][0][1], Rubiks[2][1][1])
	SavedStateBF1 = Rubiks[2][0][0], Rubiks[2][1][0]
	Rubiks[2][0][0], Rubiks[2][0][1] = SavedStateBF0[0], SavedStateBF0[1]
	Rubiks[2][1][0], Rubiks[2][1][1] = SavedStateBF1[0], SavedStateBF1[1]
	return Rubiks
def HL_1_2(Rubiks: list):
	for x in range(2):
		HL_1_1(Rubiks)
	return Rubiks
def HL_1_3(Rubiks: list):
	for x in range(3):
		HL_1_1(Rubiks)
	return Rubiks
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
	for x in range(2):
		HL_2_1(Rubiks)
	return Rubiks
def HL_2_3(Rubiks: list):
	for x in range(3):
		HL_2_1(Rubiks)
	return Rubiks
def CharlesTruscott():
	FF = [["G", "G"], ["G", "G"]]
	BF = [["B", "B"], ["B", "B"]]
	LF = [["O", "O"], ["O", "O"]]
	RF = [["R", "R"], ["R", "R"]]
	UF = [["W", "W"], ["W", "W"]]
	DF = [["Y", "Y"], ["Y", "Y"]]
	RubiksCube = [FF, RF, BF, LF, UF, DF]
	print_state(RubiksCube)
	print("Rotate left closest facing side upward once")
	HL_2_1(RubiksCube)
	print_state(RubiksCube)
	print("Then three more times for its original state")
	HL_2_3(RubiksCube)
	print_state(RubiksCube)
	print("Turn the left furthest side upward twice and the left closest side upward twice")
	HL_2_2(RubiksCube)
	HL_1_2(RubiksCube)
	print_state(RubiksCube)
	print("Then turn the left furthest side once")
	HL_2_1(RubiksCube)
	print_state(RubiksCube)
	
CharlesTruscott()


""" Front Face: [['G', 'G'], ['G', 'G']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['B', 'B'], ['B', 'B']]
 Upper Face: [['W', 'W'], ['W', 'W']]
 Down Face: [['Y', 'Y'], ['Y', 'Y']]

Rotate left closest facing side upward once
Front Face: [['G', 'G'], ['G', 'G']]
 Right Face: [['W', 'R'], ['W', 'R']]
 Left Face: [['O', 'Y'], ['O', 'Y']]
 Back Face: [['B', 'B'], ['B', 'B']]
 Upper Face: [['W', 'W'], ['O', 'O']]
 Down Face: [['Y', 'Y'], ['R', 'R']]

Then three more times for its original state
Front Face: [['G', 'G'], ['G', 'G']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['B', 'B'], ['B', 'B']]
 Upper Face: [['W', 'W'], ['W', 'W']]
 Down Face: [['Y', 'Y'], ['Y', 'Y']]

Turn the left furthest side upward twice and the left closest side upward twice
Front Face: [['G', 'G'], ['G', 'G']]
 Right Face: [['O', 'O'], ['O', 'O']]
 Left Face: [['R', 'R'], ['R', 'R']]
 Back Face: [['B', 'B'], ['B', 'B']]
 Upper Face: [['Y', 'Y'], ['Y', 'Y']]
 Down Face: [['W', 'W'], ['W', 'W']]

Then turn the left furthest side once
Front Face: [['G', 'G'], ['G', 'G']]
 Right Face: [['Y', 'O'], ['Y', 'O']]
 Left Face: [['R', 'W'], ['R', 'W']]
 Back Face: [['B', 'B'], ['B', 'B']]
 Upper Face: [['Y', 'Y'], ['R', 'R']]
 Down Face: [['W', 'W'], ['O', 'O']]


[Program finished]
"""

# Thank you Eric Grimson, John Guttag, Ana Bell and MITx and MIT OCW
