from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template ="""
answer the questioon below in spanish.

Here is contextof the conversation: 
{context}

question: {question}

answer:

"""

model = OllamaLLM(model="llama3", temperature=0.1, max_tokens=1000)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model



def chat():
    print("Bienvenido al chat. Escribe 'salir' para terminar la conversación.")
    context = ""
    while True:
        question = input("You: ")
        if question == "salir":
            print("Gracias por usar el chat. ¡Hasta luego!")
            break
        result = chain.invoke({"context": context, "question": question})
        print("Bot:", result)
        context += f"Bot: {result}\nYou: {question}\n"

if __name__ == "__main__":
    chat()

