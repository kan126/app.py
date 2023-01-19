import streamlit as st

# Quiz questions and answers
questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the symbol for sodium on the periodic table?"
]
answers = [
    "Paris",
    "Jupiter",
    "Na"
]

# Create a function to run the quiz
def run_quiz():
    score = 0
    for i, question in enumerate(questions):
        # Ask the question
        answer = st.text_input(question)

        # Check if the answer is correct
        if answer == answers[i]:
            score += 1
            st.success("Correct!")
        else:
            st.error("Incorrect. The correct answer is '{}'.".format(answers[i]))

    # Show the final score
    st.write("You got a score of {} out of {}".format(score, len(questions)))

st.title("Quiz App")
run_quiz()
