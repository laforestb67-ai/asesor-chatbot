from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# Vérifier la clé dans les logs
print("OPENAI_API_KEY présent ?", bool(os.getenv("OPENAI_API_KEY")))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return "Chatbot en ligne."

@app.post("/chat")
def chat():
    try:
        data = request.get_json(force=True)
        message = data.get("message")

        if not message:
            return jsonify({"error": "Message manquant"}), 400

        # Debug dans les logs serveur
        print("Message reçu du client:", message)

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Assistant éducatif clair et rigoureux."},
                {"role": "user", "content": message}
            ]
        )

        answer = completion.choices[0].message.content
        print("Réponse générée par OpenAI:", answer)

        return jsonify({"answer": answer})

    except Exception as e:
        print("ERREUR SERVEUR chat():", e)
        return jsonify({"error": "Erreur interne du chatbot"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

