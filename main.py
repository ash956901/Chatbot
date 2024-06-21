import streamlit as st
import time as t
import cohere


st.title("Chat Bot")
cont=st.container()

##Setting api key
co=cohere.Client(api_key=st.secrets["COHERE_API_KEY"])

if "messages" not in st.session_state:
    st.session_state["messages"]=[]

with cont:
    for m in st.session_state["messages"]:
        if m["role"]=='user':
            st.chat_message("user").write(m["content"])
        if m["role"]=="assistant":
            st.chat_message("assistant").write(m["content"])

prompt=st.chat_input("Enter your message:")

if prompt:
    st.session_state["messages"].append({
        "role":"user",
        "content":prompt
    })
    st.chat_message("user").write(prompt)

    stream=co.chat_stream(message=prompt)
    
    asst=st.chat_message("assistant")
    res_cont=asst.empty()

    res=""

    for event in stream:
        if event.event_type=="text-generation":
            res+=event.text
            res_cont.write(res)
            t.sleep(0.02)

    st.session_state["messages"].append({
        "role":"assistant",
        "content":res 
    })

st.markdown(
    """
    <style>
    /* Adjust padding for the container */
    .st-emotion-cache-1eo1tir {
        padding-left: 0px; /* Adjust padding as needed */
        padding-right:0px
    }
    </style>
    """,
    unsafe_allow_html=True
)
