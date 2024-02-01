import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Example dataset
data = data = [
    [
      '2024-01-17 22:27:27', 'Home', 'Home', 'NRSC', 'Application Sectors', 'Collaborators', 'Search', 'Collaborators', 'Collaborators',
      'Application Sectors', 'NRSC', 'mini map', 'Contact and Latest Updates', 'Collaborators', 'Store', 'Application Sectors',
      'Application Sectors', 'Application Sectors', 'E - Governance', 'Decentralised Planning', 'Decentralized Initiatives',
      'Decentralized Planning Redirect: https://bhuvanpanchayat.nrsc.gov.in/', 'E - Governance', 'Maps & OGC Services', 'Bhuvan 3D',
      'Bhuvan 3D', 'Environmental Challenges', 'Climate & Environmental Issues', 'Climate & Environment Monitoring', 'Environmental Conditions & Forecast',
      'Central Ministries', 'Regional Administrative Applications', 'Regional Applications', 'Government Governance Dashboard', 'G Governance Dashboard',
      'Website Traffic', 'Contact Us', 'Connect with Us', 'Website Traffic', 'Files Downloaded', 'Registered User Count', 'Phone : +91-40-2388 4588/89',
      'Phone : +91-40-2388 4588/89', 'Email : bhuvan@nrsc.gov.in', 'Hyderabad - 500 037 INDIA.', 'National Administration of India',
      'Indian Space Exploration Agency', 'National Remote Sensing Centre', 'Bhuvan Geo Portal & Web Services Group (BGWSG)',
      'National Remote Sensing Centre', 'Indian Space Research Organisation', 'National Remote Sensing Centre',
      'Bhuvan Geo Portal & Web Services Group (BGWSG)', 'Bhuvan Geo Portal & Web Services Group (BGWSG)', 'Explore', 'Find',
      'Bhuvan User Handbook and Others', 'Explore', 'Bhuvan Geo Portal & Web Services Group (BGWSG)', 'National Remote Sensing Centre',
      'Indian Space Research Organisation', 'National Administration of India', 'Hyderabad - 500 037 INDIA.', 'Email : bhuvan@nrsc.gov.in',
      'Phone : +91-40-2388 4588/89', 'User Suggestions', 'Customer Feedback', 'User Opinions', 'Feedback', 'Feedback', 'Government Programs', 'Government Services',
      'User Opinions', 'Feedback'
    ],
    [
      '2024-01-17 22:37:47', 'Application Sectors', 'NRSC', 'NRSC', 'Home', 'Home', 'NRSC', 'Application Sectors', 'Application Sectors',
      'Application Sectors', 'Collaborators', 'Search', 'Store', 'Newsletter', 'WIKI', 'Contact and Latest Updates', 'Rotating Logos',
      'Application Sectors', 'E - Governance', 'E - Governance', 'Decentralised Planning', 'Decentralized Initiatives', 'Archaeology',
      'Tourism-GIS', 'Bhuvan 3D', 'Climate & Environmental Challenges', 'Climate & Environmental Issues', 'Bhuvan 3D', 'Climate & Environmental Monitoring',
      'Regional Administrative Applications', 'Regional Applications', 'Explore', 'Collaborators'
    ],
    [
      '2024-01-17 22:38:20', 'Contact and Latest Updates', 'Contact and Latest Updates', 'Application Sectors', 'Application Sectors',
      'Rotating Logos', 'Application Sectors', 'Forest Management', 'Telangana', 'Karnataka', 'Telangana WRIS', 'WBIS', 'Decentralised Planning',
      'Himachal Pradesh', 'Punjab Forest', 'Simplified Bhuvan', 'Simplified Bhuvan', 'Bhuvan Central Applications', 'Maps & OGC Services',
      'Bhuvan Central Applications', 'Maps & OGC Services', 'Visualization & Free Download', 'Visualization & Free Download', 'Bhuvan 3D',
      'Climate & Environmental Challenges', 'Climate & Environmental Issues', 'Application Sectors', 'Explore'
    ],
    [
      '2024-01-17 23:05:15', 'Maps & OGC Services', 'Bhuvan 3D', 'Bhuvan 3D', 'Climate & Environment', 'Climate & Environment', 'Climate & Environment', 'Climate & Environment',
      'Regional Administrations', 'State-wise Solutions', 'Regional Apps', 'G Governance Dashboard', 'G Governance Dashboard', 'Total Visitors', 'Contact Information', 'Contact Us',
      'Total Visitors', 'Total Documents Downloaded', 'Total Registered Members', 'Phone : +91-40-2388 4588/89', 'Phone : +91-40-2388 4588/89', 'Email : bhuvan@nrsc.gov.in', 'Hyderabad - 500 037 INDIA.',
      'Government of India', 'Indian Space Exploration Organization', 'National Remote Sensing Centre', 'Bhuvan Geo Portal & Web Services Group (BGWSG)',
      'National Remote Sensing Centre', 'Indian Space Research Organisation', 'National Remote Sensing Centre', 'Bhuvan Geo Portal & Web Services Group (BGWSG)',
      'Bhuvan Geo Portal & Web Services Group (BGWSG)', 'Explore', 'Search', 'Bhuvan User Guide and Additional Resources', 'Search', 'Bhuvan Geo Portal & Web Services Group (BGWSG)',
      'National Remote Sensing Centre', 'Indian Space Exploration Organization', 'Government of India', 'Hyderabad - 500 037 INDIA.', 'Email : bhuvan@nrsc.gov.in',
      'Phone : +91-40-2388 4588/89', 'User Feedback', 'User Feedback', 'User Feedback', 'User Feedback', 'User Feedback', 'Regional Applications', 'Regional Applications',
      'User Feedback', 'User Feedback'
    ],
    [
      '2024-01-17 23:20:45', 'G Governance Dashboard', 'G Governance Dashboard', 'Application Sectors', 'Collaborators', 'Collaborators', 'Search', 'Bhuvan 3D', 'Bhuvan 3D',
      'Environmental Challenges', 'Climate & Environment', 'Climate & Environment Monitoring', 'Climate & Environmental Issues', 'Regional Administrative Applications', 'Regional Apps', 'Explore',
      'Contact and Latest Updates', 'Website Traffic', 'Store', 'Store', 'Maps & OGC Services', 'E - Governance', 'E - Governance', 'Decentralised Planning',
      'Decentralized Initiatives', 'Archaeology', 'Tourism-GIS', 'Bhuvan Lite', 'Climate & Environmental Challenges', 'Climate & Environmental Issues', 'Application Sectors', 'Collaborators',
      'Total Hits', 'Connect with Us', 'Connect with Us', 'Total Hits', 'Files Downloaded', 'Registered User Count', 'Phone : +91-40-2388 4588/89', 'Phone : +91-40-2388 4588/89',
      'Email : bhuvan@nrsc.gov.in', 'Hyderabad - 500 037 INDIA.', 'National Administration of India', 'Indian Space Exploration Agency', 'National Remote Sensing Centre', 'Bhuvan Geo Portal & Web Services Group (BGWSG)',
      'National Remote Sensing Centre', 'Indian Space Research Organisation', 'National Remote Sensing Centre', 'Bhuvan Geo Portal & Web Services Group (BGWSG)', 'Bhuvan Geo Portal & Web Services Group (BGWSG)', 'Search', 'Explore',
      'Bhuvan User Handbook and Others', 'Search', 'Bhuvan Geo Portal & Web Services Group (BGWSG)', 'National Remote Sensing Centre', 'Indian Space Research Organisation', 'National Administration of India', 'Hyderabad - 500 037 INDIA.',
      'Email : bhuvan@nrsc.gov.in', 'Phone : +91-40-2388 4588/89', 'User Suggestions', 'Customer Feedback', 'User Opinions', 'Feedback', 'Feedback', 'Government Programs', 'Government Services',
      'User Opinions', 'Feedback'
    ],
    [
      '2024-01-17 23:40:30', 'Bhuvan 3D', 'Bhuvan 3D', 'Climate & Environment', 'Climate & Environment', 'Climate & Environment', 'Climate & Environment',
      'Regional Administrations', 'State-wise Solutions', 'Regional Apps', 'G Governance Dashboard', 'G Governance Dashboard', 'Total Visitors', 'Contact Information', 'Contact Us',
      'Total Visitors', 'Total Documents Downloaded', 'Total Registered Members', 'Phone : +91-40-2388 4588/89', 'Phone : +91-40-2388 4588/89', 'Email : bhuvan@nrsc.gov.in', 'Hyderabad - 500 037 INDIA.',
      'Government of India', 'Indian Space Exploration Organization', 'National Remote Sensing Centre', 'Bhuvan Geo Portal & Web Services Group (BGWSG)',
      'National Remote Sensing Centre', 'Indian Space Research Organisation', 'National Remote Sensing Centre', 'Bhuvan Geo Portal & Web Services Group (BGWSG)',
      'Bhuvan Geo Portal & Web Services Group (BGWSG)', 'Explore', 'Search', 'Bhuvan User Guide and Additional Resources', 'Search', 'Bhuvan Geo Portal & Web Services Group (BGWSG)',
      'National Remote Sensing Centre', 'Indian Space Exploration Organization', 'Government of India', 'Hyderabad - 500 037 INDIA.', 'Email : bhuvan@nrsc.gov.in',
      'Phone : +91-40-2388 4588/89', 'User Feedback', 'User Feedback', 'User Feedback', 'User Feedback', 'User Feedback', 'Regional Applications', 'Regional Applications',
      'User Feedback', 'User Feedback'
    ]
  ]

# Convert to DataFrame
df = pd.DataFrame(data, columns=['timestamp'] + [f'activity_{i}' for i in range(1, len(data[0]))])

# Flatten the dataset and encode activities
activities = df.drop('timestamp', axis=1).values.flatten()
label_encoder = LabelEncoder()
encoded_activities = label_encoder.fit_transform(activities)

# Reshape data back to sequence format
sequence_length = df.shape[1] - 1  # Number of activities per sequence
encoded_sequences = encoded_activities.reshape(-1, sequence_length)

# Prepare input and output data (X and y)
X = encoded_sequences[:, :-1]
y = encoded_sequences[:, -1]

# One-hot encode the output
y = pd.get_dummies(y).values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model parameters
vocab_size = len(label_encoder.classes_)
embedding_dim = 50

# Define the model
model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=sequence_length - 1))
model.add(LSTM(50, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy*100:.2f}%")

# Predict the next activity for a given sequence
def predict_next_activity(sequence):
    encoded_sequence = label_encoder.transform(sequence).reshape(1, -1)
    predicted = model.predict(encoded_sequence)
    predicted_activity_idx = np.argmax(predicted, axis=1)[0]
    return label_encoder.inverse_transform([predicted_activity_idx])[0]

# Example usage
example_sequence = ['Home', 'NRSC', 'Search']  # replace with real sequence
predicted_activity = predict_next_activity(example_sequence)
print(f"Next predicted activity: {predicted_activity}")
