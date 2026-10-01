# ============================================================
# McCULLOCH-PITTS NEURON - XOR GATE (Multi-Layer)
# XOR = AND(NAND(x1,x2), OR(x1,x2))
# Program by: Samip Khadka
# Roll No: 36
# ============================================================

print("="*50)
print("  MCP NEURON: XOR GATE (Multi-Layer)")
print("  Program by: Samip Khadka")
print("  Roll No: 36")
print("="*50)

# Layer 1: NAND Gate (Hidden Neuron 1)
def nand_gate(x1, x2):
    w1 = -1
    w2 = -1
    T = -1.5
    yin = (x1 * w1) + (x2 * w2)
    return 1 if yin >= T else 0

# Layer 1: OR Gate (Hidden Neuron 2)
def or_gate(x1, x2):
    w1 = 1
    w2 = 1
    T = 0.5
    yin = (x1 * w1) + (x2 * w2)
    return 1 if yin >= T else 0

# Layer 2: AND Gate (Output Neuron)
def and_gate(x1, x2):
    w1 = 1
    w2 = 1
    T = 1.5
    yin = (x1 * w1) + (x2 * w2)
    return 1 if yin >= T else 0

# XOR Function using Multi-Layer MCP
def xor_gate(x1, x2):
    # Step 1: Calculate hidden layer outputs
    nand_out = nand_gate(x1, x2)    # NAND(x1, x2)
    or_out = or_gate(x1, x2)        # OR(x1, x2)
    
    # Step 2: Calculate output using AND gate
    return and_gate(nand_out, or_out)  # AND(NAND, OR)

print("\n XOR Truth Table:")
print("   x1   x2  |  NAND  OR  |  XOR")
print("   " + "-"*35)

inputs = [(0,0), (0,1), (1,0), (1,1)]
for x1, x2 in inputs:
    nand_out = nand_gate(x1, x2)
    or_out = or_gate(x1, x2)
    xor_out = xor_gate(x1, x2)
    
    print(f"   {x1}    {x2}   |   {nand_out}     {or_out}   |   {xor_out}")

print("\n" + "="*50)
print(" XOR Gate Implemented Successfully!")
print("   Using: XOR = AND(NAND(x1,x2), OR(x1,x2))")
print("="*50)

# Additional Validation
print("\n Validation with different weight combinations:")
print("   XOR Formula: XOR = (x1 NAND x2) AND (x1 OR x2)")
print("   This works because NAND gives 1 except when both are 1,")
print("   and OR gives 1 when at least one is 1.")
print("   AND of these two gives 1 only when both are 1,")
print("   which correctly implements XOR!")