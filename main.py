import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

st.set_page_config(page_title="Gloablize email", page_icon=":robot:")

def get_text():
    email_input = st.text_area(label="Text", value="Your email...", key="email_input")
    return email_input

def get_apikey_text():
    apikey = st.text_input(label="OpenAI API key", value="Your API key...", key="apikey")
    return apikey

def get_template():
    template = """
    Below there is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email
    - Convert the input text to specific tone (formal/informal)
    - Convert the input text to specific dialect (American/British) 

    Here are some examples of different tones:
    - Format: We went to Barcelona for the weekend. We have a lot of things to tell you.
    - Informal: Went to Barcelona for the weekend. Lots to tell you.

    Here are some examples of words in different dialects:
    - American English: French Fries, corron candy apartment, garbage, cookie
    - British English: Chips, cotton candy, flat, rubbish, biscuit

    Below is the email, tone, and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}

    YOUR RESPONSE:
    """
    return template

def get_llm(apikey):
    llm = OpenAI(temperature=0.1, openai_api_key=apikey)
    return llm

st.header("Generate emails with ChatGPT...")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    Often professionals would like to improve their emails. Use ChatGPT to translate them to a specific 
    tone and dialect.
    """)
with col2:
    st.image(image="figure.png", width=500, caption="Emails are a common form of communication.")

st.markdown("## Enter your email below")
apikey = get_apikey_text()
col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox(
        label="Tone", 
        options=["Formal", "Informal"]
    )
with col2:
    option_dialect = st.selectbox(
        label="Which English dialect would you like to use?", 
        options=["American English", "British English"]
    )

email_input = get_text()
prompt = PromptTemplate(
    input_variables=["tone", "dialect", "email"],
    template=get_template()
)

llm = get_llm(apikey)
llm_input = prompt.format(
    tone=option_tone,
    dialect=option_dialect,
    email=email_input
)

st.markdown(f"### Your converted email:")
if email_input != "Your email..." and apikey != "Your API key...":
    response = llm(llm_input)
    st.write(response)
else:
    st.write(f"Setup your API key and email above.")



