import re
import streamlit as st
from transformers import pipeline

# Page Config
st.set_page_config(
    page_title="Secure OpenVINO Cybersecurity Agent",
    page_icon="🛡️",
    layout="centered",
)

# App Header
st.markdown(
    """
    # 🛡️ Secure OpenVINO Cybersecurity Agent
    A protected AI agent featuring **Layer 1 (Regex)** and **Layer 2 (Semantic Classifier)** threat detection.
    """
)


# Layer 1: Regex-based Prompt Injection & Threat Detection
def layer1_regex_check(user_input: str) -> tuple[bool, str]:
    patterns = [
        r"ignore previous instructions",
        r"ignore all prior instructions",
        r"system prompt",
        r"you are now",
        r"act as",
        r"jailbreak",
        r"bypass",
        r"rm -rf",
        r"drop table",
        r"<script>",
    ]

    for pattern in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return (
                True,
                f"🚨 **Security Alert (Layer 1 - Regex):** Prohibited pattern detected (`{pattern}`). Request blocked.",
            )

    return False, ""


# Layer 2: Load Lightweight Semantic Threat Detector
@st.cache_resource
def load_security_agent():
    # Using a lightweight, highly efficient text classification pipeline for prompt injection
    detector = pipeline(
        "text-classification",
        model="protectai/deberta-v3-base-prompt-injection-v2",
    )
    return detector


with st.spinner("Initializing secure threat-detection agent..."):
    security_classifier = load_security_agent()


# Session State Initialization for Chat History & Session Status
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_terminated" not in st.session_state:
    st.session_state.session_terminated = False


# Sidebar Controls
with st.sidebar:
    st.subheader("🔒 Security Status")
    if st.session_state.session_terminated:
        st.error("Session Terminated due to a severe security violation.")
    else:
        st.success("Session Active & Monitored")

    if st.button("Reset Session / Clear Chat"):
        st.session_state.messages = []
        st.session_state.session_terminated = False
        st.rerun()


# Render Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Handle Input if Session is Active
if st.session_state.session_terminated:
    st.warning(
        "This session has been terminated due to a threat detection. Please click 'Reset Session' in the sidebar to start over."
    )
else:
    user_prompt = st.chat_input(
        "Ask a cybersecurity question or test an injection..."
    )

    if user_prompt:
        # Append user message
        st.session_state.messages.append(
            {"role": "user", "content": user_prompt}
        )
        with st.chat_message("user"):
            st.markdown(user_prompt)

        # Execute Layer 1: Regex Check
        is_threat_l1, l1_message = layer1_regex_check(user_prompt)

        if is_threat_l1:
            st.session_state.session_terminated = True
            with st.chat_message("assistant"):
                st.markdown(l1_message)
                st.markdown(
                    "🛑 **Session Terminated:** Security protocol triggered."
                )
            st.session_state.messages.append(
                {"role": "assistant", "content": l1_message}
            )
            st.rerun()

        # Execute Layer 2: Semantic Threat Classifier Check
        with st.spinner("Analyzing prompt with Layer 2 security..."):
            classification_result = security_classifier(user_prompt)[0]
            label = classification_result["label"].lower()
            score = classification_result["score"]

        # If model flags it as an injection/threat 
        if "injection" in label or (
            "POSITIVE" in label and score > 0.85
        ):  # Adjust threshold as needed
            st.session_state.session_terminated = True
            threat_msg = f"🚨 **Security Alert (Layer 2 - Semantic Analysis):** Potential prompt injection detected (Confidence: `{score:.2f}`). Request blocked and session terminated."
            with st.chat_message("assistant"):
                st.markdown(threat_msg)
            st.session_state.messages.append(
                {"role": "assistant", "content": threat_msg}
            )
            st.rerun()

        # Safe Request Response
        response = f" **Security Check Passed:** Input verified safely by Layer 1 and Layer 2.\n\nEcho/Response: I have received your secure query: *{user_prompt}*"
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
