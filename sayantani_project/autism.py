from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
 
# 1. EXPANDED TRAINING DATASET
training_comments = [
    # Kind / Positive inputs (Label 1)
    "I really like your new dress!",
    "You did an amazing job today.",
    "Your project looks awesome!",
    "Hey friend, want to sit with us?",
    "You have a great smile.",
    "You are such a great listener.",
    "I love hanging out with you!",
    "That was a really smart idea.",
    "You are incredibly talented at this.",
    "Your haircut looks really cool today.",
    "Your drawing is absolutely beautiful.",
    "You did a fantastic job on your presentation!",
    # Mean / Negative inputs (Label 0)
    "That looks so ugly on you.",
    "Go away, we don't want you here.",
    "You are doing it completely wrong.",
    "Stop making that weird noise.",
    "Why are you acting like that?",
    "You are being so annoying."
    "Nobody asked for your opinion.",
    "You can't play with us."
]
 
# Labels: 1 = Kind, 0 = Mean
labels = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, # 12 positive items
    0, 0, 0, 0, 0, 0, 0, 0              # 8 negative items
]
 
# 2. VECTORIZATION & MODEL TRAINING
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(training_comments)
 
model = MultinomialNB()
model.fit(X_train, labels)
 
# 3. JAY'S EXPRESSIONS
responses = {
    1: {
        "label": "Positive / Kind 😊",
        "expression": "✨ Thank you for the compliment ✨",
        "meme": "[Meme: Happy Minion dancing with joy]"
    },
    0: {
        "label": "Negative / Mean 🛑",
        "expression": "🛑 I didn't like that unappropriate behaviour 🛑",
        "meme": "[Meme: Grumpy Cat saying 'NOPE']"
    }
}
 
# 4. PREDICTION FUNCTION
def analyze_comment(comment_text):
    # Transform user input to match trained features
    transformed_input = vectorizer.transform([comment_text])
    prediction = model.predict(transformed_input)[0]
    result = responses[prediction]
    print("\n" + "="*45)
    print(f"💬 Input Comment: \"{comment_text}\"")
    print(f"🤖 Analysis: {result['label']}")
    print(f"🎭 Jay's Expression: {result['expression']}")
    print(f"🖼️ Jay's Screen Output: {result['meme']}")
    print("="*45 + "\n")
 
# 5. INTERACTIVE LOOP (Taking input from the user)
print("--------------------------------------------------")
print("🤖 Jay's Machine Learning Assistant is Running!")
print("Type any sentence to test how Jay responds.")
print("Type 'exit' or 'quit' to stop the program.")
print("--------------------------------------------------\n")
 
while True:
    user_input = input("Enter a comment for Jay: ")
    # Exit condition
    if user_input.lower().strip() in ["exit", "quit"]:
        print("\nStopping program. Goodbye! 👋")
        break
    # Ignore empty inputs
    if not user_input.strip():
        print("Please enter a valid phrase.")
        continue
    analyze_comment(user_input)