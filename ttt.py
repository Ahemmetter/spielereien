#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Dieses Programm ist eine kleine Umsetzung des Klassikers Tic-Tac-Toe,
inspiriert von "War Games". Vielleicht reicht das ja als Gnadenpunkt :)"""

X = "X"
O = "Ø"
tie = "Okay..dieses Mal wars unentschieden...."

def new_board():
	"""Baut ein Array mit den 9 Feldern. Diese sind zur besseren
	Orientierung mit ihrer jeweiligen Stelle gefüllt."""
	board = []
	for zelle in range(9):
		board.append(zelle)
	return board

def print_board(board):
	"""Gibt das jeweils aktuelle Spielbrett aus."""
	print "\n\t", board[0], "|", board[1], "|", board[2]
	print "\t", "----------"
	print "\t", board[3], "|", board[4], "|", board[5]
	print "\t", "----------"
	print "\t", board[6], "|", board[7], "|", board[8]

def erlaubte_zuege(board):
	"""Array, das die jeweils offenen Felder enthält."""
	zuege = []
	for zelle in range(9):
		if type(board[zelle]) == int:
			zuege.append(zelle)
	return zuege

def gewinner(board):
	"""Siegbedingungen. In jeder Runde wird geprüft, ob 3 gleiche Symbole
	in einer Reihe, Spalte oder Diagonale sind. Sobald der erste Spieler
	5 mal an der Reihe war und niemand gewonnen hat, ist das Spiel vorbei.
	Eigentlich sollte die Untschieden-Bedingung so etwas wie "if int not
	in board...." sein, aber das gab nur Probleme. Für den Fall mit dem
	Spielbrett mit 9 Kästchen ist aber diese Bedingung ausreichend. """
	sieg = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
	test_frei = 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8
	for i in range(len(sieg)):
		if board[sieg[i][0]] == board[sieg[i][1]] == board[sieg[i][2]] != test_frei:
			sieger = board[sieg[i][0]]
			return sieger
	while test_frei in board:
		return None
	if board.count(erster) == 5:
		return tie

def mensch_dran(board, human):
	"""Wenn der Spieler an der Reihe ist, kann er eine Auswahl aus den
	möglichen Kästchen treffen."""
	zug = None
	while zug not in erlaubte_zuege(board):
		zug = int(raw_input("Wähle weise, Sterblicher (0-8):  "))
		if zug not in erlaubte_zuege(board):
			print "Meeep. Nicht da."
	return zug

def comp_dran(board, comp, human):
	"""Der Computer testet jede Möglichkeit, ob er im nächsten Zug
	gewinnen kann oder ob der den Spieler blocken kann. Wenn beides nicht
	geht, nimmt er aus dem Array beste_zuege die nächste freie Zahl."""
	beste_zuege = [4,0,2,6,8,1,3,5,7]
#wenn der Computer im nächsten Zug gewinnen kann:
	for zug in erlaubte_zuege(board):
		board[zug] = comp
		if gewinner(board) == comp:
			return zug
		board[zug] = zug
#wenn der Spieler im nächsten Zug gewinnen kann:
	for zug in erlaubte_zuege(board):
		board[zug] = human
		if gewinner(board) == human:
			return zug
		board[zug] = zug
#wenn niemand im nächsten Zug gewinnen kann:
	for zug in beste_zuege:
		if zug in erlaubte_zuege(board):
			return zug

def naechster(turn):
	"""Einfache Funktion, die jeweils den anderen Spieler an die Reihe
	lässt."""
	if turn == X:
		return O
	else:
		return X

print \
	"""
	Sei gegrüßt, Sterblicher. Bist du bereit für das Spiel der Götter?
	Solltest du gewinnen, verrate ich dir die Antwort auf deine tiefste 
	Frage. Sie wird dir aber nicht gefallen...
	Egal. Unsere Regeln sind die folgenden:
	
	Du machst einen Zug, indem du eine Zahl von 0 - 8 eintippst. Danach
	bin ich dran.
	Die Zahlen entsprechen dem folgenden Muster:
	
						 0 | 1 | 2
						-----------
						 3 | 4 | 5
						-----------
						 6 | 7 | 8
	
	Sei bereit, Sterblicher....
	
	"""
choose_symbol = raw_input("Willst du als X oder Ø spielen? (x, o):  ")
while choose_symbol not in ("x", "o"):
	print "Sorry, aber das habe ich leider nicht verstanden. Also nochmal:"
	choose_symbol = raw_input("Willst du als X oder Ø spielen? (x, o):  ")
if choose_symbol == "x":
	human = X
	comp = O
else:
	human = O
	comp = X

go_first = raw_input("Willst du den ersten Zug machen? (y, n):  ")
while go_first not in ("y", "n"):
	print "Also was genau willst du jetzt?"
	go_first = raw_input("Willst du den ersten Zug machen? (y, n):  ")
if go_first == "y":
	print "Sehr wohl. Du wirst es brauchen."
	erster = human
else:
	print "Muuuhhhaahahaha, du machst es mir aber wirklich zu leicht."
	erster = comp

if erster == X:
	turn = X
else:
	turn = O
board = new_board()
print_board(board)
"""Hauptprogramm: Solange es keinen Gewinner gibt, wird entweder der Zug
des Spielers oder des Computers abgefragt und das neue Spielbrett
ausgegeben. Dann kommt der nächste Spieler dran."""
while not gewinner(board):
	if turn == human:
		zug = mensch_dran(board, human)
		board[zug] = human
	else:
		zug = comp_dran(board, comp, human)
		board[zug] = comp
	print_board(board)
	turn = naechster(turn)

if gewinner(board) == human:
	print \
	"""Herzlichen Glückwunsch. Wie versprochen, hier die Antwort auf
	deine tiefste Frage, die Antwort auf das Leben, das Universum und alles:
	
	
						42
	
	
	Ich hab dir ja gesagt, sie wird dir nicht gefallen.
	"""
elif gewinner(board) == comp:
	print "Haha, du hättest sowieso nicht gegen meine grandiose Übermacht gewonnen."
else:
	print tie
