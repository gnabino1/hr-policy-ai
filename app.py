import streamlit as st
from hr_assistant.pipeline import build_hr_assistant, ask
from hr_assistant.logger import get_logger

logger= get_logger(__name__)
st.set_page_config(page_title="HR Policy Assistant", page_icon=":material/smart_toy:")
st.title("HR Policy Assistant")
st.caption("Ask me anything about the Company HR Policy Document")

@st.cache_resource(show_spinner="Setting up the assistant (only happens once)...")
def get_agent():
    return build_hr_assistant()

agent= get_agent()

if "messages" not  in st.session_state:
    st.session_state.messages=[]

# Show past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get a new question from the user
question= st.chat_input("Ask question about HR policy")
if question:
    logger.info("=== Streamlit run: new question received ===")
    st.session_state.messages.append({"role":"user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer= ask(agent, question)
        st.markdown(answer)
    st.session_state.messages.append({"role":"assistant", "content": answer})


