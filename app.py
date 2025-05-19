import streamlit as st
from langchain.chat_models import init_chat_model

# # Initialize model (only do this once to save resources)
model = init_chat_model("gpt-4o-mini", model_provider="openai")

# Define the prompt template
prompt_template = """
You are an assignment grader. Compare the student's answer with the teacher's ideal answer. If the student's answer fully matches the teacher's, award 10 marks. Otherwise, assign partial marks from 0 to 9, based on how closely the student's answer aligns with the ideal answer.

Provide your evaluation in the following format:

## Question  
{question}  
## IdealAnswer  
{ideal_answer}  
## StudentAnswer  
{student_answer}  
## Marks:{{marks}}  
## Marks Explanation  
{{reason_for_deduction}}  

Be fair and specific in your evaluation. Focus on correctness, completeness, and relevance of the student’s answer when comparing it to the ideal answer.
"""

# Streamlit App UI
st.title("📘 Assignment Grader")

# Collect inputs from user
question = st.text_area("Enter the question")
ideal_answer = st.text_area("Enter the ideal answer from the teacher")
student_answer = st.text_area("Enter the student's answer")

# Button to trigger grading
if st.button("Grade Answer"):
    if question and ideal_answer and student_answer:
        with st.spinner("Grading in progress..."):
            # Fill the prompt with user inputs
            prompt = prompt_template.format(
                question=question,
                ideal_answer=ideal_answer,
                student_answer=student_answer
            )

            # Invoke the model
            response = model.invoke(prompt)
            st.markdown(response.content)
    else:
        st.warning("Please fill out all fields before grading.")
