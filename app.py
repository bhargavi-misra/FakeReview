'''from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("fake_review_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route('/')
def home():
    print("Home route triggered!")
    return render_template('index.html')

#@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    review = request.form['review']
    review_vector = vectorizer.transform([review])
    prediction = model.predict(review_vector)[0]  # prediction is 0 or 1

    if prediction == 1:
        result = "This review is genuine ✅"
    else:
        result = "This review is fake ❌"

    return render_template('index.html', prediction=result)


if __name__ == '__main__':
    app.run(debug=True)'''
import streamlit as st
import joblib

# Load the trained model and vectorizer
model = joblib.load("fake_review_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# App Title
st.title("🕵️‍♀️ Fake Review Detector")
st.write("Enter a product review below and find out if it's fake or genuine!")

# Text input
review = st.text_area("📝 Enter your review:")

# Button
if st.button("Predict"):
    if review.strip():
        # Vectorize and predict
        review_vector = vectorizer.transform([review])
        prediction = model.predict(review_vector)[0]

        # Display result
        if prediction == 1:
            st.success("✅ This review is **genuine**!")
        else:
            st.error("❌ This review is **fake**.")
    else:
        st.warning("Please enter a review first.")

# Optional footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
