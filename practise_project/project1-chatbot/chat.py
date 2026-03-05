import streamlit as st
import ollama
def generate_llm_response(prompt,model="llama3.2"):
    messages=[
        {
            'role': 'user',
            'content': prompt,
        }
    ]
    response=ollama.chat(model=model,messages=messages)
    return response['message']['content']
#streamlit application layout
st.title("LLM TEXT Generator")
st.write("Interact with a large language model (LLM ) and generate responses based on your input.")
# test input for the user prompt
user_prompt = st.text_area("Enter your prompt here:")

#button to generate response
if st.button("Generate Response"):
    if user_prompt.strip() != "":
        with st.spinner("Generating response..."):
            try:
                #generate response from the LLM
                response=generate_llm_response(user_prompt)
                st.success("Response generated successfully!")
                st.text_area("LLM Response:", value=response, height=200)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a prompt before generating a response.")
