# ============================================================
# McCULLOCH-PITTS NEURON - NOR GATE (Dynamic Weights & Threshold)
# Program by: Samip Khadka
# Roll No: 36
# ============================================================

print("="*50)
print("  MCP NEURON: NOR GATE (Dynamic Weights & Threshold)")
print("  Program by: Samip Khadka")
print("  Roll No: 36")
print("="*50)

# MCP Neuron Function - w1, w2, T are all dynamic
def mcp_nor(x1, x2, w1, w2, T):
    yin = (x1 * w1) + (x2 * w2)
    if yin >= T:
        return 1
    else:
        return 0

# Expected NOR gate outputs for (0,0),(0,1),(1,0),(1,1)
target = [1, 0, 0, 0]
inputs = [(0,0), (0,1), (1,0), (1,1)]

attempt = 1
success = False

while not success:
    print(f"\n--- Attempt {attempt} ---")
    w1 = float(input("Enter weight w1: "))
    w2 = float(input("Enter weight w2: "))
    T = float(input("Enter threshold value (T): "))

    outputs = []
    print(f"\nUsing w1={w1}, w2={w2}, T={T}")
    print("\n  x1   x2  |  y")
    print("-"*20)

    for x1, x2 in inputs:
        y = mcp_nor(x1, x2, w1, w2, T)
        outputs.append(y)
        print(f"  {x1}    {x2}   |  {y}")

    print("\n" + "="*50)
    if outputs == target:
        success = True
        print(" NOR Gate Implemented Successfully!")
        print(f"   Final values -> w1={w1}, w2={w2}, T={T}")
    else:
        print(" NOR Gate NOT Implemented — output doesn't match target")
        print(f"   Expected: {target}")
        print(f"   Got:      {outputs}")
        print("   Please try different values of w1, w2, T.")
    print("="*50)

    attempt += 1