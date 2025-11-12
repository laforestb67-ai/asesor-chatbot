import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="static")
CORS(app)

@app.get("/")
def root():
    return send_from_directory("static", "index.html")

@app.get("/health")
def health():
    return jsonify({"ok": True})

@app.post("/chat")
@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "").strip().lower()
    if not question:
        return jsonify({"reply": "No escuché nada."})

    if "ahorro" in question:
        reply = "Ahorrar es separar una parte de tus ingresos para el futuro."
    elif "crédito" in question:
        reply = "Un crédito es dinero que te presta un banco y debes devolver con intereses."
    elif "presupuesto" in question:
        reply = "Un presupuesto es una planificación de tus ingresos y gastos para mantener el equilibrio financiero."
    else:
        reply = "Puedo hablarte de ahorro, crédito, presupuesto o deudas. ¿Qué tema te interesa?"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

