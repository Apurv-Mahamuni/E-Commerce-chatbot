import streamlit as st
from pathlib import Path
from router import router
from faq import ingest_faq_data,faq_chain
from sql import sql_chain
from small_talk import small_talks_query


fqas_path = Path(__file__).resolve().parent / "resources" / "faq_data.csv"
ingest_faq_data(fqas_path)

def ask(question):
    route = router(question).name
    if route == "faq":
        return faq_chain(question)
    elif route == "sql":
        return sql_chain(question)
    elif route == "small_talk":
        return small_talks_query(question) 
    else:
        return f"Route {route} not implemented yet"


st.title("E-commerce Chatbot")

query = st.chat_input("Write your Query")

if "message" not in st.session_state:
    st.session_state["message"] = []

for message in st.session_state.message:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
if query:
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.message.append({"role":"user", "content":query})

    response = ask(query)
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.message.append({"role":"assistant", "content":response})

