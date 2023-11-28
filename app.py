import streamlit as st
from transformers import pipeline
from transformers import AutoTokenizer
#import torch


#@st.cache_data()
def load_model():
    model = pipeline("summarization", model="dheeraj-kj/T5_Model")
    return model

tokenizer = AutoTokenizer.from_pretrained("t5-small")


summarizer = load_model()
st.title("TextSnap")
input_text = st.text_area("Enter your text here...", height = 100)
#st.caption("Enter your text here...")
button = st.button("Summarize")

prefix = "summarize: "
text = prefix + input_text 
with st.spinner("Generating Summary..."):
    if input_text and button:
        res = summarizer(text)
        summary = "".join([summ['summary_text'] for summ in res])
        st.write(summary)
    