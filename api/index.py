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
    result = client.chat.completions.create( model="Qwen/Qwen3-235B-A22B", messages=[ { "role": "user", "content": "Give two similar or closely related sentence pair among these (The capital of France is paris, Paris is the capital of france, Paris isn't the capital of france, Manila is the capital of the Philippines?)" } ], max_tokens=50, )
    print(result)
    
    return 'Results inference'


# # from huggingface_hub import InferenceClient
# completion = client.chat.completions.create(
#     model="Qwen/Qwen3-235B-A22B",
#     messages=[
#         {
#             "role": "user",
#             "content": "What is the capital of France?"
#         }
#     ],
#     max_tokens=512,
# )

# print(completion.choices[0].message)
