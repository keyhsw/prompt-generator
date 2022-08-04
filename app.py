from transformers import pipeline, set_seed
import gradio as grad
import random

gpt2_pipe = pipeline('text-generation', model='succinctly/text2image-prompt-generator')


def generate(starting_text):
    seed = random.randint(1, 100000)
    set_seed(seed)
    response = gpt2_pipe(starting_text, max_length=30, num_return_sequences=random.randint(5, 15))
    response_list = "\n".join(response)
    return response_list


txt = grad.Textbox(lines=1, label="English", placeholder="English Text here")
out = grad.Textbox(lines=5, label="Generated Text")

grad.Interface(fn=generate,
               inputs=txt, 
               outputs=out,
               allow_flagging='never',
               cache_examples=False,
               theme="default").launch(enable_queue=True, debug=True)
