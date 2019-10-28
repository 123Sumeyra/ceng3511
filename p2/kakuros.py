from ortools.sat.python import cp_model
model = cp_model.CpModel()

solver = cp_model.CpSolver()

# Creates the model.
def Kakuros(ia,ai):

# Creates the variables.
    a1 = model.NewIntVar(1, 9, 'a1')
    a2 = model.NewIntVar(1, 9, 'a2')
    a3 = model.NewIntVar(1, 9, 'a3')
    b1 = model.NewIntVar(1, 9, 'b1')
    b2 = model.NewIntVar(1, 9, 'b2')
    b3 = model.NewIntVar(1, 9, 'b3')
    c1 = model.NewIntVar(1, 9, 'c1')
    c2 = model.NewIntVar(1, 9, 'c2')
    c3 = model.NewIntVar(1, 9, 'c3')

# Creates the constraints.
    Row1 = [a1, a2, a3]
    Row2 = [b1, b2, b3]
    Row3 = [c1, c2, c3]
    Col1 = [a1, b1, c1]
    Col2 = [a2, b2, c2]
    Col3 = [a3, b3, c3]

    model.AddAllDifferent(Row1)
    model.AddAllDifferent(Row2)
    model.AddAllDifferent(Row3)
    model.AddAllDifferent(Col1)
    model.AddAllDifferent(Col2)
    model.AddAllDifferent(Col3)

    model.Add((a1 + a2 + a3) == ia[3])
    model.Add((b1 + b2 + b3) == ia[4])
    model.Add((c1 + c2 + c3) == ia[5])
    model.Add((a1 + b1 + c1) == ia[0])
    model.Add((a2 + b2 + c2) == ia[1])
    model.Add((a3 + b3 + c3) == ia[2])


    status = solver.Solve(model)
    if status == cp_model.FEASIBLE:
        ai.writelines(
            str(ia[3]) + ", " + str(solver.Value(a1)) + ", " + str(solver.Value(a2)) + ", " + str(solver.Value(a3)) + "\n")

        ai.writelines(
        str(ia[4]) + ", " + str(solver.Value(b1)) + ", " + str(solver.Value(b2)) + ", " + str(solver.Value(b3)) + "\n")

        ai.writelines(
            str(ia[5]) + ", " + str(solver.Value(c1)) + ", " + str(solver.Value(c2)) + ", " + str( solver.Value(c3)))




with open('kakuro_input.txt', "r") as md:
     line = md.readlines()
     #print(line)
     s =[]
     for i in line:
         line_split = i.strip().split(",")
         for x in line_split:
             s.append(int(x))


with open("kakuro_output.txt", "w") as ai:
    line = line[0].strip()
    ai.writelines("x" + ", " + str(line) + "\n")
    Kakuros(s,ai)