""" Rotation moves not completely done. Just a start done in time of the first 30 minutes after NYE 2023 Jan 1st 2024. Matrix system eventually working in all rotations of the Rubiks 6 * (3 * 5) subsequent moves """

# Charles Thomas Wallace Truscott 

def print_state(Rubiks):
	print("Front Face: {}\n Right Face: {}\n Left Face: {}\n Back Face: {}\n Upper Face: {}\n Down Face: {}\n".format(Rubiks[0], Rubiks[1], Rubiks[3], Rubiks[2], Rubiks[4], Rubiks[5]))
def LeftSideTurnedClosestFacing(Rubiks: list) -> list:
	SingleStateUF = (Rubiks[4][1][0], Rubiks[4][1][1])
	Rubiks[3][0][1] = Rubiks[5][1][0]; Rubiks[3][1][1] = Rubiks[5][1][1]
	Rubiks[4][1][0] = Rubiks[3][1][1]; Rubiks[4][1][1] = Rubiks[3][0][1]
	Rubiks[0][0][0], Rubiks[0][0][1],Rubiks[0][1][0], Rubiks[0][1][1] = Rubiks[0][1][0], Rubiks[0][0][0], Rubiks[0][1][1], Rubiks[0][0][1]
	Rubiks[5][1][0], Rubiks[5][1][1] = Rubiks[1][0][0], Rubiks[1][1][0]
	Rubiks[1][0][0] = SingleStateUF[0]
	Rubiks[1][1][0] = SingleStateUF[1]
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
	print("One solved move")
	print_state(LeftSideTurnedClosestFacing(RubiksCube))
	
CharlesTruscott()
