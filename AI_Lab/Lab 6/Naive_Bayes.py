import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    'Outlook': ['Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Sunny', 'Overcast',
                'Rainy', 'Rainy', 'Sunny', 'Rainy', 'Overcast', 'Overcast', 'Sunny'],
    'Temp': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
             'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal',
                 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['FALSE', 'TRUE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'TRUE',
             'FALSE', 'FALSE', 'FALSE', 'TRUE', 'TRUE', 'FALSE', 'FALSE'],
    'Rain': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes',
             'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)
print(f"Dataset size: {df.shape[0]} rows × {df.shape[1]} columns")
df

features = ['Outlook', 'Temp', 'Humidity', 'Wind']
today = {'Outlook': 'Sunny', 'Temp': 'Hot', 'Humidity': 'Normal', 'Wind': 'FALSE'}

today_df = pd.DataFrame([today])
print("Today's weather conditions:")
print(today_df.to_string(index=False))

# Prior probabilities
class_counts = df['Rain'].value_counts()
total = len(df)
p_yes = class_counts['Yes'] / total
p_no = class_counts['No'] / total

print("\nPRIOR PROBABILITIES")
print(f"P(Rain=Yes) = {class_counts['Yes']}/{total} = {p_yes:.4f}")
print(f"P(Rain=No)  = {class_counts['No']}/{total} = {p_no:.4f}")

# Conditional probability helper

def conditional_probability(feature, value, target):
    class_rows = df[df['Rain'] == target]
    count = (class_rows[feature] == value).sum()
    probability = count / len(class_rows)
    return count, len(class_rows), probability

# Calculate conditional probabilities for today's features
conditional = {}
for target in ['Yes', 'No']:
    conditional[target] = {}
    print(f"\nFor Rain = {target}:")
    for feature in features:
        count, denominator, probability = conditional_probability(
            feature, today[feature], target
        )
        conditional[target][feature] = probability
        print(f"P({today[feature]} | {target}) = {count}/{denominator} = {probability:.4f}")

# Apply Naive Bayes formula
likelihood_yes = 1
likelihood_no = 1

for feature in features:
    likelihood_yes *= conditional['Yes'][feature]
    likelihood_no *= conditional['No'][feature]

joint_yes = p_yes * likelihood_yes
joint_no = p_no * likelihood_no

p_features = joint_yes + joint_no
posterior_yes = joint_yes / p_features
posterior_no = joint_no / p_features

print("\nBAYES THEOREM CALCULATION")
print(f"P(Yes ∩ Features) = {joint_yes:.6f}")
print(f"P(No  ∩ Features) = {joint_no:.6f}")
print(f"P(Features)       = {p_features:.6f}")
print(f"P(Yes | Features) = {posterior_yes:.4f} ({posterior_yes:.2%})")
print(f"P(No  | Features) = {posterior_no:.4f} ({posterior_no:.2%})")

# Manual prediction
manual_prediction = 'Yes' if posterior_yes > posterior_no else 'No'

print("\nMANUAL PREDICTION")
print(f"Predicted class: {manual_prediction}")
print(f"Confidence: {max(posterior_yes, posterior_no):.2%}")

# Plot Posterior Probabilities
plt.figure(figsize=(6, 4))
classes = ['Yes', 'No']
probabilities = [posterior_yes, posterior_no]
colors = ['#2ECC71', "#ff66e5"]
bars = plt.bar(classes, probabilities, color=colors, edgecolor='black')
plt.title('Posterior Probabilities')
plt.ylabel('Probability')
plt.ylim(0, 1)
# Add percentage labels on top of bars
for bar, prob in zip(bars, probabilities):
    plt.text(bar.get_x() + bar.get_width()/2,
    prob + 0.02,
    f'{prob:.1%}',
    ha='center',
    fontweight='bold'
)
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
