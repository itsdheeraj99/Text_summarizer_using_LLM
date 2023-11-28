# Text Summarizer using LLM
This project is designed to leverage LLMs to summarize textual content. <br>
The model employed and fine-tuned here is T5.

## Overview
In NLP, T5 stands out as one of the powerful models in handling number of language tasks, including summarization. This summarizer has the vanilla transformer architecture encode and decoder to extract the information from long documents and articles. <br>
This summarizer is an abstractive text summarization. 

## Key-features
Abstractive Summarization: Benefit from abstractive summarization, allowing the model to generate human-like summaries that capture the core ideas of the input text.

Integration-friendly: It can integrated into your applications, projects, or workflows to improve text summarization capabilities. 


## Usage 
This model is deployed as a web-application. It can be accessed [here.](https://summar-ease.streamlit.app/)
It can be run a local machine as well.
- Download the files ``app.py`` and `requirements.txt` into a directory.
- In terminal directing to the project directory, run the command `pip install -r requirements.txt` 
- Also install the streamlit framework by running the command line `pip install streamlit` 
- For launching the app run `streamlit run app.py`.

## Inference in code
Besides the app, the model is stored on HuggingFace transformers hub which can be accessed by following these steps. <br>
To do the inference, 
- Install the transformers framework into your environment by running this command in terminal, `pip install transformers`.
- Import the `transformers` and, `pipeline` API using, `from transformers import pipeline`
- Download the model into your notebook by running,  `summarizer = pipeline("summarization", model="dheeraj-kj/T5_Model")` 
- Prefix the input text with `summarize:` 
- Pass the prefixed input text as an argument into our model object `summarizer()`

## Reference
- ["Attention is all you need"](https://arxiv.org/abs/1706.03762) paper.
- [Hugging Face Transformers](huggingface.co) 
