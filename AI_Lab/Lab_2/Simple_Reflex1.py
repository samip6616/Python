def simple_reflex_agent(location, status):
    # location: 'A' or 'B', status: 'Dirty' or 'Clean'
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move to B"
    elif location == "B":
        return "Move to A"
    else:
        return "NoOp"

print("********** Simple Reflex Agent **********\n")
print("Program by Samip Khadka")
print("Roll No. 36")

print("\nThe percept sequence is (A, Dirty)")
action = simple_reflex_agent("A", "Dirty")
print("Action:", action)

print("\nThe percept sequence is (A, Clean)")
action = simple_reflex_agent("A", "Clean")
print("Action:", action)

print("\nThe percept sequence is (B, Dirty)")
action = simple_reflex_agent("B", "Dirty")
print("Action:", action)


print("\nThe percept sequence is (B, Clean)")
action = simple_reflex_agent("B", "Clean")
print("Action:", action)
