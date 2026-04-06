from loader import loadSplit
from retriever import getRetriever  
from chain import buildChain

def main():
    pdfPath = input("Enter your PDF path: ")
    print("Loading and splitting PDF")
    chunks = loadSplit(pdfPath)

    print("Creating vectorstore")
    retriever = getRetriever(chunks)

    print("Building chain")
    chain = buildChain(retriever)

    while True:
        question = input("You: ")
        if question.lower() == 'exit':
            break
        
        for chunk in chain.stream(question):
            print(chunk, end = "", flush = True)
        print()

        answer = chain.invoke(question)
        print(f"Bot: {answer}")

if __name__ == "__main__":
    main()