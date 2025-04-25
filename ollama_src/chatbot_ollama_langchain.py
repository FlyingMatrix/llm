#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    AI chatbot based on langchain and ollama
"""

# !pip install langchain langchain-ollama ollama
# !ollama run mistral

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template =  """
                Answer the question below.
                Here is the conversation history: {context}
                Question: {question}
                Answer:
            """

model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():

    context = ""
    print("\033[1;32m" +
          r"""
          ／＞--フ
         | 　_　_|     ------------------------------------
       ／` ミ＿xノ    | *** Welcome to the AI ChatBot! *** |
      /　　　　 |      ------------------------------------
     /　 ヽ　　 ﾉ
    │　　|　|　|
   ／￣|　　 |　|　)  
  (＼ヽ＿_ヽ_)__)   
   ＼二)            
          """ 
          + "\033[0m")

    while True:
        user_input = input("\033[1;33m# Please enter your question (press q to quit): \033[0m")
        if user_input.lower() == "q":
            break

        result = chain.invoke({"context": context, "question": user_input})
        print("\n\033[1;34m# AI ChatBot: \033[0m" + str(result) + "\n")
        context += f"\nUser: {user_input}\nAI: {result}"


if __name__ == "__main__":

    handle_conversation()
