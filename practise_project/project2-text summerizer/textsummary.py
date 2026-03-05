
import torch
import gradio as gr
import os
from transformers import pipeline

# Set cache directory to E: drive (more space available)
os.environ['HF_HOME'] = 'E:\\dataScience and ai -Quest innovative\\.cache'

# Using a tiny model that requires ~400MB instead of 1.2GB
text_summary = pipeline("summarization", model="sshleifer/distilbart-cnn-6-6",torch_dtype=torch.bfloat16)
text="Wikipedia gained early contributors from Nupedia, Slashdot postings, and web search engine indexing. Language editions were created beginning in March 2001, with a total of 161 in use by the end of 2004.[W 5][W 6] Nupedia and Wikipedia coexisted until the former's servers were taken down permanently in 2003, and its text was incorporated into Wikipedia. The English Wikipedia passed the mark of 2 million articles on September 9, 2007, making it the largest encyclopedia ever assembled, surpassing the Yongle Encyclopedia made in China during the Ming dynasty in 1408, which had held the record for almost 600 years.[25]"
print(text_summary(text))
def summary(input):
    output = text_summary(input)
    return output[0]['summary_text']
gr.close_all()
#iface = gr.Interface(fn=summary, inputs="text", outputs="text", title="Text Summarizer")

demo = gr.Interface(fn=summary, inputs=[gr.Textbox(label="Input to summarize",lines=6)], outputs=[gr.Textbox(label="summarized text",lines=4)], title="Text Summarizer",description="Enter text to summarize and get a concise summary")
demo.launch(share=True)

import torch
import gradio as gr
import os
from transformers import pipeline

# Set cache directory to E: drive (more space available)
os.environ['HF_HOME'] = 'E:\\dataScience and ai -Quest innovative\\.cache'

# Using a tiny model that requires ~400MB instead of 1.2GB
text_summary = pipeline("summarization", model="sshleifer/distilbart-cnn-6-6",torch_dtype=torch.bfloat16)
text="Wikipedia gained early contributors from Nupedia, Slashdot postings, and web search engine indexing. Language editions were created beginning in March 2001, with a total of 161 in use by the end of 2004.[W 5][W 6] Nupedia and Wikipedia coexisted until the former's servers were taken down permanently in 2003, and its text was incorporated into Wikipedia. The English Wikipedia passed the mark of 2 million articles on September 9, 2007, making it the largest encyclopedia ever assembled, surpassing the Yongle Encyclopedia made in China during the Ming dynasty in 1408, which had held the record for almost 600 years.[25]"
print(text_summary(text))
def summary(input):
    output = text_summary(input)
    return output[0]['summary_text']
gr.close_all()
#iface = gr.Interface(fn=summary, inputs="text", outputs="text", title="Text Summarizer")

demo = gr.Interface(fn=summary, inputs=[gr.Textbox(label="Input to summarize",lines=6)], outputs=[gr.Textbox(label="summarized text",lines=4)], title="Text Summarizer",description="Enter text to summarize and get a concise summary")
demo.launch(share=True)

