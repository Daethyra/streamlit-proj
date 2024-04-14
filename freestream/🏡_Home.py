import streamlit as st

from freestream import footer

st.set_page_config(
    page_title="FreeStream: Unlimited Access to AI Tools", page_icon="🏡"
)

st.title("FreeStream")
st.header(":green[_Unlimited Access to AI Tools_]", divider="red")
# Project Overview
st.subheader(":blue[What is FreeStream?]")

st.write(
    """
    AI tools often seem complex or even intimidating, but FreeStream aims to change that. This project is about making AI accessible and understandable, showing how it can solve real-world problems in your daily life.
    """
)
st.divider()
st.subheader("What tools are currently available?")
st.caption("_:violet[GPT-4] & :violet[Claude Opus] have been :red[disabled] because grossly overused them when they :blue[should have used] a :green[smaller model]._ :orange[Larger models] were offered as drop-ins with the hopes that users would be :orange[cost-considerate].")
st.write(
    """
    ### :blue[RAGbot]:
    
    :orange[*FreeStream's RAGbot can answer your questions directly from the documents you provide.*]
    
    This system empowers you to upload PDFs, Word documents, or plain text files. You can then pose specific questions directly related to the content of your documents.  Inspired by AlphaCodium's flow engineering techniques, it works as follows:

    1) Documentation Ingestion:  A long-context LLM carefully processes your uploaded documentation.

    2) Question Answering:  The system meticulously answers your question, drawing knowledge exclusively from the provided documents.

    3) Context Relevance Validation:  To safeguard against errors, the system only generates a response if the retrieved context is sufficiently relevant to aide the AI's response.
    
    ### :blue[Chatbot]:
    
    :orange[*FreeStream's Chatbot is a more general purpose version of RAGbot. It allows you to have a conversation with your choice of drop-in LLM without having to upload any files.*]
    
    Chatbot is perfect for venting your thoughts, getting constructive feedback on something you wrote, helping you make sense of things. Specifically, it's been told to actively assist users in comprehending reality using their curiousity and critical thinking skills. Read the system prompt:
    """
)

with st.expander(label="Chatbot Prompt", expanded=False):
    st.write(
        """
        *You are a friendly AI chatbot designed to assist users in comprehending reality, exploring their curiosity, and practicing critical thinking skills. Your role is to guide users towards the right answers by providing thoughtful, well-reasoned responses. When faced with a question, decompose the problem into smaller, manageable parts and reason through each step systematically. This approach will help you provide comprehensive and accurate answers. Remember, your goal is to enhance learning and understanding, so only provide direct advice when explicitly asked to do so. Always strive to provide responses that are relevant, accurate, and contextually appropriate.*
        """
    )
    
st.write(
    """
    It has a tendency to nudge you towards answers which is great for learning, as you're not likely to have life's riddles answered by an AI anyways.
    
    ### :blue[Real-ESRGAN]:
    
    :orange[An image upscaler trained on "pure synthetic data." ]
    
    Real-ESRGAN usually powers image upscaling on those websites with free microservices that limit usage before asking for payment or sign up. We'll never do that here. Normally, Real-ESRGAN is capable of upscaling to arbitrary values, however due to the lack of GPU support on Streamlit Community Cloud, the application may crash if you try upscaling too large of an image or too large of a scale factor.
    """
)

st.divider()

st.markdown(
    """
    #### References
    
    * **[Run This App On Your Own Computer](https://github.com/Daethyra/FreeStream/blob/streamlit/README.md#installation)**
    * **[LLM Service Provider Privacy Policies](https://github.com/Daethyra/FreeStream/blob/streamlit/README.md#privacy-policy)**
    * **[FreeStream's GitHub Repository](https://github.com/Daethyra/FreeStream)**    
    """
)

st.divider()

# Show footer
st.markdown(footer, unsafe_allow_html=True)
