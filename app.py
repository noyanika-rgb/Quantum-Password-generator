from flask import Flask, render_template, jsonify, request
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import string

app = Flask(__name__)

def generate_quantum_bits(n_bits):
    qc = QuantumCircuit(n_bits, n_bits)

    qc.h(range(n_bits))
    qc.measure(range(n_bits), range(n_bits))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts()

    bitstring = list(counts.keys())[0]
    return bitstring


def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"

    bits = generate_quantum_bits(length * 6)

    password = ""
    for i in range(length):
        chunk = bits[i*6:(i*6)+6]
        index = int(chunk, 2) % len(characters)
        password += characters[index]

    return password


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    length = int(data.get("length", 8))

    password = generate_password(length)

    return jsonify({
        "password": password
    })


if __name__ == "__main__":
    app.run(debug=True)