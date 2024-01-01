
# Charles Thomas Wallace Truscott 

def print_state(Rubiks):
	print("Front Face: {}\n Right Face: {}\n Left Face: {}\n Back Face: {}\n Upper Face: {}\n Down Face: {}\n".format(Rubiks[0], Rubiks[1], Rubiks[3], Rubiks[2], Rubiks[4], Rubiks[5]))

def FRU_1_1(Rubiks: list):
	SaveStateDF = Rubiks[4][0][0], Rubiks[4][1][0]
	SaveStateLF = Rubiks[3][0][0], Rubiks[3][1][0]
	SaveStateUF = Rubiks[5][0][0], Rubiks[5][1][0]
	SaveStateBF = Rubiks[2][0][1], Rubiks[2][1][1]
	SaveStateFF = Rubiks[0][0][0], Rubiks[0][1][0]
	Rubiks[0][0][0], Rubiks[0][1][0] = SaveStateDF[1], SaveStateDF[0]
	Rubiks[2][0][1], Rubiks[2][1][1] = SaveStateUF[1], SaveStateUF[0]
	Rubiks[5][0][0], Rubiks[5][1][0] = SaveStateFF[0], SaveStateFF[1]
	Rubiks[4][0][0], Rubiks[4][1][0] = SaveStateBF[0], SaveStateBF[1]
	SaveStateLF1 = Rubiks[3][0][1], Rubiks[3][1][1]
	SaveStateLF2 = Rubiks[3][0][0], Rubiks[3][1][0]
	Rubiks[3][0][0] = SaveStateLF2[1]
	Rubiks[3][0][1] = SaveStateLF2[0]
	Rubiks[3][1][0] = SaveStateLF1[1]
	Rubiks[3][1][1] = SaveStateLF1[0]
	return Rubiks
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
#	print("Rotate left closest facing side upward once")
#	HL_2_1(RubiksCube)
#	print_state(RubiksCube)
#	print("Then three more times for its original state")
#	HL_2_3(RubiksCube)
#	print_state(RubiksCube)
#	print("Turn the left closest side upward twice and the left furthest side upward twice")
#	HL_2_2(RubiksCube)
#	HL_1_2(RubiksCube)
#	print_state(RubiksCube)
#	print("Then turn the left closest side once")
#	HL_2_1(RubiksCube)
#	print_state(RubiksCube)
#	print("Then turn the left furthest side once")
#	HL_1_1(RubiksCube)
#	print_state(RubiksCube)
	answer = ""
	while answer != str("quit"):
		print("Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube")
		answer = str(input())
		if answer == str("LFFU1"):
			HL_1_1(RubiksCube)
		elif answer == str("LFFU2"):
			HL_1_2(RubiksCube)
		elif answer == str("LFFU3"):
			HL_1_3(RubiksCube)
		elif answer == str("LFCU1"):
			HL_2_1(RubiksCube)
		elif answer == str("LFCU2"):
			HL_2_2(RubiksCube)
		elif answer == str("LFCU3"):
			HL_2_3(RubiksCube)
		elif answer == str("FRLU1"):
			FRU_1_1(RubiksCube)
		print_state(RubiksCube)
CharlesTruscott()


""" Front Face: [['G', 'G'], ['G', 'G']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['B', 'B'], ['B', 'B']]
 Upper Face: [['W', 'W'], ['W', 'W']]
 Down Face: [['Y', 'Y'], ['Y', 'Y']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube
FRLU1
Front Face: [['W', 'G'], ['W', 'G']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['B', 'Y'], ['B', 'Y']]
 Upper Face: [['B', 'W'], ['B', 'W']]
 Down Face: [['G', 'Y'], ['G', 'Y']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube
FRLU1
Front Face: [['B', 'G'], ['B', 'G']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['B', 'G'], ['B', 'G']]
 Upper Face: [['Y', 'W'], ['Y', 'W']]
 Down Face: [['W', 'Y'], ['W', 'Y']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube
FRLU1
Front Face: [['Y', 'G'], ['Y', 'G']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['B', 'W'], ['B', 'W']]
 Upper Face: [['G', 'W'], ['G', 'W']]
 Down Face: [['B', 'Y'], ['B', 'Y']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube
LFCU1
Front Face: [['Y', 'Y'], ['G', 'G']]
 Right Face: [['G', 'R'], ['W', 'R']]
 Left Face: [['O', 'B'], ['O', 'Y']]
 Back Face: [['B', 'W'], ['B', 'W']]
 Upper Face: [['G', 'W'], ['O', 'O']]
 Down Face: [['B', 'Y'], ['R', 'R']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube
FRLU1
Front Face: [['O', 'Y'], ['G', 'G']]
 Right Face: [['G', 'R'], ['W', 'R']]
 Left Face: [['O', 'O'], ['Y', 'B']]
 Back Face: [['B', 'R'], ['B', 'B']]
 Upper Face: [['W', 'W'], ['W', 'O']]
 Down Face: [['Y', 'Y'], ['G', 'R']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube
"""

# Thank you Eric Grimson, John Guttag, Ana Bell and MITx and MIT OCW
# Nice stay in Tweed Centre for Mental Health Kurrajong Unit from November 23rd to December 22nd. Friendly nurses, great roast beef, great roast lamb and potato, great beef rendang, butter chicken, soap washes, 9 hours sleep, 8:30 a.m. wake up, 12 30 p.m. lunch and 5:30 p.m. dinner and sunshine and coffee and tea and fruit and prunes. Dad taught me to make rice pudding and Cremè caramele but not chocolate creme or frùche or Panna cotta, rare delicatessens that allowed me to survive. Wish I could enter a culinary business. Love chicken sandwiches and mayonnaise 

