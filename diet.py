# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pulp import  *

import pandas as pd

import xlrd as f

#read in data
data = pd.read_excel("diet.xls",heeader=0)

#limit rows to just data rows
data = data[0:64]

#convert dataframe to list
data = data.values.tolist()

# Creates a list of the Ingredients
Ingredients = [x[0] for x in data] #list of food names

# A dictionary of the costs of each of the Ingredients is created
costs = dict([(x[0], float(x[1])) for x in data])

# A dictionary of calories in each of the Ingredients is created
calories = dict([(x[0], float(x[3])) for x in data])

# A dictionary of the cholestorol in each of the Ingredients is created
cholestorol = dict([(x[0], float(x[4])) for x in data])

# A dictionary of Total Fat in each of the Ingredients is created
totalfat = dict([(x[0], float(x[5])) for x in data])

# A dictionary of the sodium in each of the Ingredients is created
sodium = dict([(x[0], float(x[6])) for x in data])

# A dictionary of the carbohydrate in each of the Ingredients is created
carbohydrate = dict([(x[0], float(x[7])) for x in data])

# A dictionary of the fiber in each of the Ingredients is created
fiber = dict([(x[0], float(x[8])) for x in data])

# A dictionary of the protein in each of the Ingredients is created
protein = dict([(x[0], float(x[9])) for x in data])

# A dictionary of the vitaminA in each of the Ingredients is created
vitaminA = dict([(x[0], float(x[10])) for x in data])

# A dictionary of the vitaminC in each of the Ingredients is created
vitaminC = dict([(x[0], float(x[11])) for x in data])

# A dictionary of the calcium in each of the Ingredients is created
calcium = dict([(x[0], float(x[12])) for x in data])

# A dictionary of the iron in each of the Ingredients is created
iron = dict([(x[0], float(x[13])) for x in data])

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Diet Problem", LpMinimize)

# A dictionary called 'ingredient_vars' is created to contain the referenced Variables
ingredient_vars = LpVariable.dicts("Ingr",Ingredients,0)

# The objective function is added to 'prob' first
prob += lpSum([costs[i]*ingredient_vars[i] for i in Ingredients]), "Total Cost of Ingredients per can"

# The daily constraints are added to 'prob'

prob += lpSum([calories[i] * ingredient_vars[i] for i in Ingredients]) >= 1500.0, "MinCalorieRequirement"
prob += lpSum([calories[i] * ingredient_vars[i] for i in Ingredients]) <= 2500.0, "MaxCalorieRequirement"
prob += lpSum([cholestorol[i] * ingredient_vars[i] for i in Ingredients]) >= 30.0, "MinCholestorolRequirement"
prob += lpSum([cholestorol[i] * ingredient_vars[i] for i in Ingredients]) <= 240.0, "MaxCholestorolRequirement"
prob += lpSum([totalfat[i] * ingredient_vars[i] for i in Ingredients]) >= 20.0, "MinfatRequirement"
prob += lpSum([totalfat[i] * ingredient_vars[i] for i in Ingredients]) <= 70.0, "MaxfatRequirement"
prob += lpSum([sodium[i] * ingredient_vars[i] for i in Ingredients]) >= 800.0, "MinsodiumRequirement"
prob += lpSum([sodium[i] * ingredient_vars[i] for i in Ingredients]) <= 2000.0, "MaxsodiumRequirement"
prob += lpSum([carbohydrate[i] * ingredient_vars[i] for i in Ingredients]) >= 130.0, "MincarbohydrateRequirement"
prob += lpSum([carbohydrate[i] * ingredient_vars[i] for i in Ingredients]) <= 450.0, "MaxcarbohydrateRequirement"
prob += lpSum([fiber[i] * ingredient_vars[i] for i in Ingredients]) >= 125.0, "MinfiberRequirement"
prob += lpSum([fiber[i] * ingredient_vars[i] for i in Ingredients]) <= 250.0, "MaxfiberRequirement"
prob += lpSum([protein[i] * ingredient_vars[i] for i in Ingredients]) >= 60.0, "MinproteinRequirement"
prob += lpSum([protein[i] * ingredient_vars[i] for i in Ingredients]) <= 100.0, "MaxproteinRequirement"
prob += lpSum([vitaminA[i] * ingredient_vars[i] for i in Ingredients]) >= 1000.0, "MinvitaminARequirement"
prob += lpSum([vitaminA[i] * ingredient_vars[i] for i in Ingredients]) <= 10000.0, "MaxvitaminARequirement"
prob += lpSum([vitaminC[i] * ingredient_vars[i] for i in Ingredients]) >= 400.0, "MinvitaminCRequirement"
prob += lpSum([vitaminC[i] * ingredient_vars[i] for i in Ingredients]) <= 5000.0, "MaxvitaminCRequirement"
prob += lpSum([calcium[i] * ingredient_vars[i] for i in Ingredients]) >= 700.0, "MincalciumRequirement"
prob += lpSum([calcium[i] * ingredient_vars[i] for i in Ingredients]) <= 1500.0, "MaxcalciumRequirement"
prob += lpSum([iron[i] * ingredient_vars[i] for i in Ingredients]) >= 10.0, "MinironRequirement"
prob += lpSum([iron[i] * ingredient_vars[i] for i in Ingredients]) <= 40.0, "MaxironRequirement"



# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print ("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print (v.name, "=", v.varValue)
    
    # The optimised objective function value is printed to the screen
print ("Total Cost of Ingredients per day = ", value(prob.objective))

