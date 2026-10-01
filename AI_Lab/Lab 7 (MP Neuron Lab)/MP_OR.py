# ============================================================
# McCULLOCH-PITTS NEURON - OR GATE (Dynamic Threshold)
# Program by: Samip Khadka
# Roll No: 36
# ============================================================

print("="*50)
print("  MCP NEURON: OR GATE (Dynamic Threshold)")
print("  Program by: Samip Khadka")
print("  Roll No: 36")
print("="*50)

# MCP Neuron Function - T is now dynamic
def mcp_or(x1, x2, T):
    w1 = 1
    w2 = 1
    yin = (x1 * w1) + (x2 * w2)
    if yin >= T:
        return 1
    else:
        return 0

# Let user set the threshold
T = float(input("Enter threshold value (T): "))

# Expected OR gate outputs for (0,0),(0,1),(1,0),(1,1)
target = [0, 1, 1, 1]

inputs = [(0,0), (0,1), (1,0), (1,1)]
outputs = []

print(f"\nUsing Threshold T = {T}")
print("\n  x1   x2  |  y")
print("-"*20)

for x1, x2 in inputs:
    y = mcp_or(x1, x2, T)
    outputs.append(y)
    print(f"  {x1}    {x2}   |  {y}")

print("\n" + "="*50)
if outputs == target:
    print(" OR Gate Implemented Successfully!")
else:
    print(" OR Gate NOT Implemented — output doesn't match target")
    print(f"   Expected: {target}")
    print(f"   Got:      {outputs}")
print("="*50)