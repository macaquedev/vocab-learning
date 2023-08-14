#  8 outputs
#  9 inputs

OUTPUTS = 8
INPUTS = 9

print("Outputs")

for i in range(1, OUTPUTS * INPUTS + 1, INPUTS):
    print("Connect", list(range(i, i+INPUTS)), "to", int((i-1)/INPUTS)+1)

print("\n\nInputs")

for i in range(INPUTS):
    print("Connect", [j + i for j in range(1, OUTPUTS * INPUTS + 1, INPUTS)], "to", i+1)