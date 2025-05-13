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

@app.route('/inference-qwen')
def about():
    from huggingface_hub import InferenceClient

    client = InferenceClient(
        provider="hf-inference",
        api_key="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",
    )
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    result = client.chat.completions.create( model="Qwen/Qwen3-235B-A22B", messages=[ {"role": "system", "content": "You are a precise answering machine, like automated computer with direct and brief answers. You are instructed to get similar sentences from the list of sentences in parentheses. Just give the sentences from list but you can also give 'null' (like computer does) for no similarity.  "}, { "role": "user", "content": "(The capital of France is paris, Paris is the capital of france, Paris isn't the capital of france, Manila is the capital of France?)" } ], max_tokens=200, )
    print(result)
    
    return 'Results inference'


@app.route('/inference-llama')
def about():
    from huggingface_hub import InferenceClient

    client = InferenceClient(
        provider="hf-inference",
        api_key="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",
    )
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    result = client.chat.completions.create( model="meta-llama/Llama-2-70b-chat-hf", messages=[ {"role": "system", "content": "You are a precise answering machine, like automated computer with direct and brief answers. You are instructed to get similar sentences from the list of sentences in parentheses. Just give the sentences from list but you can also give 'null' (like computer does) for no similarity.  "}, { "role": "user", "content": "(The capital of France is paris, Paris is the capital of france, Paris isn't the capital of france, Manila is the capital of France?)" } ], max_tokens=200, )
    print(result)
    
    return 'Results inference llama'

@app.route('/inference-model-a')
def about():
    from huggingface_hub import InferenceClient

    client = InferenceClient(
        provider="hf-inference",
        api_key="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",
    )
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    result = client.chat.completions.create( model="microsoft/Phi-3.5-mini-instruct", messages=[ {"role": "system", "content": "You are a precise answering machine, like automated computer with direct and brief answers. You are instructed to get similar sentences from the list of sentences in parentheses. Just give the sentences from list but you can also give 'null' (like computer does) for no similarity.  "}, { "role": "user", "content": "(The capital of France is paris, Paris is the capital of france, Paris isn't the capital of france, Manila is the capital of France?)" } ], max_tokens=200, )
    print(result)
    # mistralai/Mistral-7B-Instruct-v0.3
    return 'Results inference model phi'

@app.route('/inference-model-b')
def about():
    from huggingface_hub import InferenceClient

    client = InferenceClient(
        provider="hf-inference",
        api_key="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",
    )
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    result = client.chat.completions.create( model="mistralai/Mistral-7B-Instruct-v0.3", messages=[ {"role": "system", "content": "You are a precise answering machine, like automated computer with direct and brief answers. You are instructed to get similar sentences from the list of sentences in parentheses. Just give the sentences from list but you can also give 'null' (like computer does) for no similarity.  "}, { "role": "user", "content": "(The capital of France is paris, Paris is the capital of france, Paris isn't the capital of france, Manila is the capital of France?)" } ], max_tokens=200, )
    print(result)
    # mistralai/Mistral-7B-Instruct-v0.3
    return 'Results inference model misral'






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
