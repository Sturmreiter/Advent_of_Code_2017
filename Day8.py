variables = {}
highest = 0
with open('Day8_input.txt') as file:
    for statement in file:
        commands = statement.split(sep=None,maxsplit=5) 
        # 0 = variable name, 1 = inc/dec, 2 = value to add, 3 = if,
        # 4 = name of if variable, 5 = </>/== statement
        ifstatement = "variables.get('" + commands[4] + "',0) " + commands[5]
        if eval(ifstatement):
            mult = (1 if commands[1] == 'inc' else -1)
            variables[commands[0]] = variables.get(commands[0],0) + mult * int(commands[2])
            if variables[commands[0]] > highest:
                highest = variables[commands[0]]

variablesSorted = sorted(variables, key=variables.get)
print(variables[variablesSorted[-1]])
print(highest)

