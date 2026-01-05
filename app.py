from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/version")
def version():
    return jsonify(service="automation-lab", version="1.0.0")

@app.errorhandler(404)
def not_found(_error):
    return jsonify(
        error="not_found",
        message="Route not found",
        path=request.path,
    ), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

