import math
from collections import Counter

def entropy(labels):
    counts = Counter(labels)
    total = len(labels)
    return -sum((count/total) * math.log2(count/total) for count in counts.values() if count > 0)

def information_gain(data, labels, feature_idx):
    total_entropy = entropy(labels)
    feature_values = [row[feature_idx] for row in data]
    unique_values = set(feature_values)
    
    weighted_entropy = 0
    for value in unique_values:
        subset_labels = [labels[i] for i, row in enumerate(data) if row[feature_idx] == value]
        weighted_entropy += (len(subset_labels) / len(labels)) * entropy(subset_labels)
    
    return total_entropy - weighted_entropy

def build_tree(data, labels, features, depth=0, max_depth=3):
    if len(set(labels)) == 1 or depth >= max_depth:
        return Counter(labels).most_common(1)[0][0]
    
    best_feature = max(range(len(features)), 
                      key=lambda i: information_gain(data, labels, i))
    
    tree = {features[best_feature]: {}}
    feature_values = set(row[best_feature] for row in data)
    
    for value in feature_values:
        subset_data = [row for row in data if row[best_feature] == value]
        subset_labels = [labels[i] for i, row in enumerate(data) if row[best_feature] == value]
        
        if subset_data:
            tree[features[best_feature]][value] = build_tree(
                subset_data, subset_labels, features, depth + 1, max_depth)
    
    return tree

def predict(tree, sample, features):
    if not isinstance(tree, dict):
        return tree
    
    feature = list(tree.keys())[0]
    feature_idx = features.index(feature)
    feature_value = sample[feature_idx]
    
    if feature_value in tree[feature]:
        return predict(tree[feature][feature_value], sample, features)
    else:
        return "Unknown"

# Example usage
if __name__ == "__main__":
    # Weather data: [outlook, temperature, humidity, wind] -> play
    data = [
        ['sunny', 'hot', 'high', 'weak'],
        ['sunny', 'hot', 'high', 'strong'],
        ['overcast', 'hot', 'high', 'weak'],
        ['rain', 'mild', 'high', 'weak'],
        ['rain', 'cool', 'normal', 'weak'],
        ['overcast', 'cool', 'normal', 'strong']
    ]
    labels = ['no', 'no', 'yes', 'yes', 'yes', 'yes']
    features = ['outlook', 'temperature', 'humidity', 'wind']
    
    tree = build_tree(data, labels, features)
    print("Decision Tree:", tree)
    
    test_sample = ['sunny', 'cool', 'high', 'strong']
    prediction = predict(tree, test_sample, features)
    print(f"Prediction for {test_sample}: {prediction}")