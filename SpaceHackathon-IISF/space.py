from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from collections import Counter
import csv

def read_csv_to_list(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = "C:\\Users\\sanja\\Desktop\\data.csv"
data = read_csv_to_list(file_path)

# Convert the dataset to a list of strings (rows)
text_data = [' '.join(row) for row in data]

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(text_data)

# Perform k-means clustering
num_clusters = 4  # You can adjust the number of clusters as needed (k value)
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Assign cluster labels to each row
cluster_labels = kmeans.labels_

# Add cluster labels to the original data
for i, row in enumerate(data):
    row.append(cluster_labels[i])

# Display clusters and their contents
clusters = {}
for i, label in enumerate(cluster_labels):
    if label not in clusters:
        clusters[label] = [data[i][:-1]]
    else:
        clusters[label].append(data[i][:-1])

# Labels for training data (cluster labels)
labels = kmeans.labels_

# Train a text classification model (Naive Bayes)
model = make_pipeline(TfidfVectorizer(stop_words='english'), MultinomialNB())  # Use TF-IDF for classification
model.fit(text_data, labels)

# Function to suggest moves based on user input dataset
def suggest_moves(user_input_data):
    # Convert the user input data to a string (row)
    user_input = ' '.join(user_input_data)
    
    # Predict the cluster label for the user input
    predicted_label = model.predict([user_input])[0]

    # Retrieve probabilities for each cluster
    probabilities = model.predict_proba([user_input])[0]

    # Sort cluster indices based on probabilities in descending order
    sorted_indices = probabilities.argsort()[::-1]

    # Flatten the list of lists in the selected cluster
    flattened_actions = [action for sublist in clusters[sorted_indices[0]] for action in sublist]

    # Count the occurrences of each action in the cluster
    action_counts = Counter(flattened_actions)

    # Get the top 5 recommended actions based on frequency
    recommended_actions = [action for action, _ in action_counts.most_common(5)]

    return recommended_actions

# Example usage with user input dataset
csv_file_path = 'C:\\Users\\sanja\\Documents\\Coding\\SpaceHCK\\log_events.csv'  # Replace 'your_file.csv' with the actual file path

# Initialize an empty list to store the second column values
user_input_data = []

# Open the CSV file and read its contents
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    cc=3
    for row in csv_reader:
        user_input_data.append(row[1])
        cc=cc-1
        if(cc<=0):
            break
#user_input_data = ['Contact and Latest Updates', 'Visualization', 'Terms']
recommendations = suggest_moves(user_input_data)

print("User Input Dataset:", user_input_data)
print("Recommended Actions:", recommendations)
