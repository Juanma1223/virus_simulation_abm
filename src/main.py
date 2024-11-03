import json
from simulation import InitSimulation, StartSimulation

inputFile = open('input.json')

data = json.load(inputFile)

InitSimulation(data)