import os
import requests  
import json 
from flask import Flask, request
from flask_cors import CORS, cross_origin
from huggingface_hub import InferenceClient

os.environ["SERPER_API_KEY"] = "4fb86c3b2a34c0110e8b9f7ff24d42e983d49876"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
 
app = Flask(__name__) 

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/inference')
def about():
    from huggingface_hub import InferenceClient

    client = InferenceClient(
        provider="hf-inference",
        api_key="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",
    )

    result = client.table_question_answering(inputs={ "query": "How many stars does the transformers repository have?", "table": { "Repository": ["Transformers", "Datasets", "Tokenizers"], "Stars": ["36542", "4512", "3934"], "Contributors": ["651", "77", "34"], "Programming language": [ "Python", "Python", "Rust, Python and NodeJS" ] } }, model="google/tapas-base-finetuned-wtq",  )

    print(result)
    
    return 'Results inference'


# from huggingface_hub import InferenceClient

# client = InferenceClient(
#     provider="hf-inference",
#     api_key="hf_xxxxxxxxxxxxxxxxxxxxxxxx",
# )

# result = client.table_question_answering(
#     inputs={
#     "query": "How many stars does the transformers repository have?",
#     "table": {
#         "Repository": ["Transformers", "Datasets", "Tokenizers"],
#         "Stars": ["36542", "4512", "3934"],
#         "Contributors": ["651", "77", "34"],
#         "Programming language": [
#             "Python",
#             "Python",
#             "Rust, Python and NodeJS"
#         ]
#     }
# },
#     model="google/tapas-base-finetuned-wtq",
# )
