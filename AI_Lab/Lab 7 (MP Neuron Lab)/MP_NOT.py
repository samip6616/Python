# ============================================================
# McCULLOCH-PITTS NEURON - NOT GATE (Dynamic Threshold)
# Program by: Samip Khadka
# Roll No: 36
# ============================================================

print("="*50)
print("  MCP NEURON: NOT GATE (Dynamic Threshold)")
print("  Program by: Samip Khadka")
print("  Roll No: 36")
print("="*50)

# MCP Neuron Function - T is now dynamic
def mcp_not(x1, T):
    w1 = -1          # Negative weight for inversion
    yin = x1 * w1
    if yin >= T:
        return 1
    else:
        return 0

# Let user set the threshold
T = float(input("Enter threshold value (T): "))

# Expected NOT gate outputs for (0), (1)
target = [1, 0]

inputs = [0, 1]
outputs = []

print(f"\nUsing Threshold T = {T}")
print("\n  x1  |  y")
print("-"*15)

for x1 in inputs:
    y = mcp_not(x1, T)
    outputs.append(y)
    print(f"  {x1}   |  {y}")

print("\n" + "="*50)
if outputs == target:
    print(" NOT Gate Implemented Successfully!")
else:
    print(" NOT Gate NOT Implemented — output doesn't match target")
    print(f"   Expected: {target}")
    print(f"   Got:      {outputs}")
print("="*50)