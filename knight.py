import math

pos_chang = [
    ("x" : 2, "y" : 1),
    ("x" : -2, "y" : 1),
    ("x" : 1, "y" : 2),
    ("x" : -1, "y" : 2),
    ("x" : 1, "y" : -2),
    ("x" : 2, "y" : -1),
    ("x" : -1, "y" : -2),
    ("x" : -2, "y" : -1)
]

def possible_moves(s,position):
	arr = []
	for element in pos_chang:
		ty = s["y"] - element["y"]
		tx = s["x"] - element["x"]
		if (tx > -1 and ty > -1) and (tx < 8 and ty < 8):
			arr+=[{ "x" : tx, "y" : ty, "parent":position}]
	return arr

def aKa(start,end):
	if end>63:
		return
	s={"x":start%8, "y":math.floor(start/8)}
	e={"x":end%8, "y":math.floor(end/8)}
	count=0
	pos=0
	q=[{"x":s["x"], "y":s["y"],"parent":-1}]
	while q[pos]["x"] != e["x"] or q[pos]["y"] != e["y"]:
		moves = possible_moves(q[pos],pos)
		q+= moves
		pos+=1

	i = pos

	while i != 0:
		i=q[i]["parent"]
		count+=1

	return count


print aKa(3,63)