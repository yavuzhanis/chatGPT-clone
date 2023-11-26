from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        data = {
            "result": "Merhaba! Ancak ben bir dil modeliyim ve fiziksel varlığım yok. Sadece metin tabanlı sorulara cevap verebilirim. Eğer bir konuda yardım ya da bilgi istiyorsanız, sormaktan çekinmeyin!"
        }
        return jsonify(data)
    data = {
        "result": "Merhaba! Ancak ben bir dil modeliyim ve fiziksel varlığım yok. Sadece metin tabanlı sorulara cevap verebilirim. Eğer bir konuda yardım ya da bilgi istiyorsanız, sormaktan çekinmeyin!"
    }
    return jsonify(data)


app.run(debug=True)
