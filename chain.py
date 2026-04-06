from langchain_groq import ChatGroq                        # ye groq ki api ko humara prompt bhejta hai and goes to llm for response
from langchain_core.prompts import ChatPromptTemplate      # this is prompt answer {context} like this
from langchain_core.output_parsers import StrOutputParser  # ye isko response.choices[0].message.content replacement hai
from langchain_core.runnables import RunnablePassthrough   # this help to use chain pipes | withoout this we have to write in old method
from config import GroqAPIKey, modelName

def buildChain(retriever):
    llm = ChatGroq(api_key = GroqAPIKey, model = modelName)
    prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful assistant. Answer the questions based on the context below.
        Context : {context}
        Question : {question}
        """)
    
    def formatDocs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context" : retriever | formatDocs, "question" : RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
)
    return chain

