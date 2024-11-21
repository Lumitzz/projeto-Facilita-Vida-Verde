from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
app = Flask(__name__)
CORS(app)

chave_api = os.getenv("CO_API_KEY")
modelo = ChatCohere(model="command-r-plus")
parser = StrOutputParser()

template_mensagens = ChatPromptTemplate.from_messages([
    ("system", "Responda a perguntas sobre chás, ervas e seus benefícios"),
    ("user", "{texto}"),
])

@app.route('/chat', methods=['POST'])
def responder_pergunta():
    data = request.json
    pergunta = data.get('pergunta', '')

    if not pergunta: 
        return jsonify({"error": "Pergunta vazia"}), 400

    mensagens = [HumanMessage(pergunta)]
    chain = template_mensagens | modelo | parser
    resposta = chain.invoke(mensagens)

    return jsonify({"resposta": resposta})

if __name__ == '__main__':
    app.run(debug=True)