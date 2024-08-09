from transformers import pipeline

# Query Answering Function
def answer_query(text, query):
    qa_pipeline = pipeline("question-answering")
    answer = qa_pipeline(question=query, context=text)
    return answer["answer"]

def get_query_main(query, text):
    answer = answer_query(text, query)
    return answer
