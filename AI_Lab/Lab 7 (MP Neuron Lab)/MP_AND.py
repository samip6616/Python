print("="*50)
print("  MCP NEURON: AND GATE")
print("  Program by: Samip Khadka")
print("  Roll No: 36")
print("="*50)

# MCP Neuron Function - T is now dynamic
def mcp_and(x1, x2, T):
    w1 = 1
    w2 = 1
    yin = (x1 * w1) + (x2 * w2)
    if yin >= T:
        return 1
    else:
        return 0

# Let user set the threshold
T = float(input("Enter threshold value (T): "))

# Expected AND gate outputs for (0,0),(0,1),(1,0),(1,1)
target = [0, 0, 0, 1]

inputs = [(0,0), (0,1), (1,0), (1,1)]
outputs = []

print(f"\nUsing Threshold T = {T}")
print("\n  x1   x2  |  y")
print("-"*20)

for x1, x2 in inputs:
    y = mcp_and(x1, x2, T)
    outputs.append(y)
    print(f"  {x1}    {x2}   |  {y}")

print("\n" + "="*50)
if outputs == target:
    print(" AND Gate Implemented Successfully!")
else:
    print(" AND Gate NOT Implemented — output doesn't match target")
    print(f"   Expected: {target}")
    print(f"   Got:      {outputs}")
print("="*50)

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Title
ax.text(5, 7.5, 'MCP Neuron: AND Gate', fontsize=20, fontweight='bold',
        ha='center', va='center')
ax.text(5, 7.0, 'Program by: Samip Khadka | Roll No: 36',
        fontsize=12, ha='center', va='center', style='italic')

# Input Layer
ax.text(1.5, 6.0, 'INPUT LAYER', fontsize=14, fontweight='bold', ha='center')
circle1 = Circle((1.5, 5.0), 0.4, facecolor='lightblue', edgecolor='black', linewidth=2)
circle2 = Circle((1.5, 3.5), 0.4, facecolor='lightblue', edgecolor='black', linewidth=2)
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.text(1.5, 5.0, 'x₁', fontsize=14, fontweight='bold', ha='center', va='center')
ax.text(1.5, 3.5, 'x₂', fontsize=14, fontweight='bold', ha='center', va='center')

# Weights
ax.text(3.0, 5.7, 'w₁=1', fontsize=12, ha='center')
ax.text(3.0, 4.2, 'w₂=1', fontsize=12, ha='center')

# Arrows from inputs to summation
arrow1 = FancyArrowPatch((1.9, 5.0), (3.8, 4.7),
                         arrowstyle='->', mutation_scale=20, linewidth=2, color='blue')
arrow2 = FancyArrowPatch((1.9, 3.5), (3.8, 3.8),
                         arrowstyle='->', mutation_scale=20, linewidth=2, color='blue')
ax.add_patch(arrow1)
ax.add_patch(arrow2)

# Summation Node
ax.text(5.0, 6.0, 'SUMMATION', fontsize=14, fontweight='bold', ha='center')
sum_circle = Circle((5.0, 4.5), 0.7, facecolor='lightgreen', edgecolor='black', linewidth=2)
ax.add_patch(sum_circle)
ax.text(5.0, 4.5, 'Σ', fontsize=24, fontweight='bold', ha='center', va='center')
ax.text(5.0, 3.6, 'yin = x₁+x₂', fontsize=11, ha='center')

# Arrow to threshold
arrow3 = FancyArrowPatch((5.7, 4.5), (6.8, 4.5),
                         arrowstyle='->', mutation_scale=20, linewidth=2, color='green')
ax.add_patch(arrow3)

# Threshold
ax.text(7.8, 6.0, 'THRESHOLD', fontsize=14, fontweight='bold', ha='center')
threshold_box = FancyBboxPatch((7.0, 3.8), 1.6, 1.4,
                                boxstyle="round,pad=0.1",
                                facecolor='lightyellow', edgecolor='black', linewidth=2)
ax.add_patch(threshold_box)
ax.text(7.8, 4.8, 'T = 1.5', fontsize=14, fontweight='bold', ha='center', va='center')
ax.text(7.8, 4.2, 'if yin ≥ T', fontsize=11, ha='center')

# Arrow to activation
arrow4 = FancyArrowPatch((8.6, 4.5), (9.2, 4.5),
                         arrowstyle='->', mutation_scale=20, linewidth=2, color='orange')
ax.add_patch(arrow4)

# Output
ax.text(9.8, 6.0, 'OUTPUT', fontsize=14, fontweight='bold', ha='center')
output_circle = Circle((9.8, 4.5), 0.5, facecolor='lightcoral', edgecolor='black', linewidth=2)
ax.add_patch(output_circle)
ax.text(9.8, 4.5, 'y', fontsize=18, fontweight='bold', ha='center', va='center')

# Step function explanation
ax.text(9.8, 3.5, 'Step Function', fontsize=10, ha='center', style='italic')

# Truth Table
table_data = [
    ['x₁', 'x₂', 'yin', 'y'],
    ['0', '0', '0', '0'],
    ['0', '1', '1', '0'],
    ['1', '0', '1', '0'],
    ['1', '1', '2', '1']
]

table = ax.table(cellText=table_data, loc='bottom', bbox=[0.0, -0.1, 1.0, 0.2])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)

# Color the table header
for i in range(4):
    table[(0, i)].set_facecolor('#40466e')
    table[(0, i)].set_text_props(weight='bold', color='white')

# Highlight the last row
for i in range(4):
    table[(4, i)].set_facecolor('#90EE90')

plt.tight_layout()
plt.show()
