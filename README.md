# Quantum-Password-generator
The Quantum Password Generator is a web-based application that generates highly secure passwords using principles of quantum computing. Instead of relying on traditional pseudo-random algorithms, this project uses quantum-inspired randomness (via simulation) to create unpredictable and strong passwords. 
It combines a **Python Flask backend**, **quantum circuit simulation**, and a **modern frontend UI** to deliver a complete, interactive experience.

---

##  Features

*  Quantum-inspired random password generation
*  Customizable password length
*  Toggle options:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
*  Fast generation using backend API
*  Clean and modern UI
*  Strong and unpredictable passwords

---

##  How It Works

1. User selects password preferences (length, character types).
2. Request is sent to the backend (Flask server).
3. Quantum circuit is created using **Qiskit**:

   * Qubits are initialized
   * Hadamard gates create superposition
   * Measurement produces random bits
4. Generated **bitstring** is converted into numbers.
5. Numbers are mapped to characters.
6. Final password is generated and displayed.

---

##  Tech Stack

### Backend

* Python
* Flask
* Qiskit (Quantum Simulation)

### Frontend

* HTML
* CSS
* JavaScript

---

##  Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/quantum-password-generator.git
cd quantum-password-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Qiskit Aer (Important Fix)

```bash
pip install qiskit-aer
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

## Example Output

```
Generated Password: A9#kL2@pZ
```

Each password is generated using quantum randomness, making it highly secure and unpredictable.

---

## Advantages

* Better randomness than classical generators
* Stronger security
* Customizable and user-friendly
* Demonstrates real-world use of quantum computing

---

## Limitations

* Uses simulation (not real quantum hardware)
* Slightly slower than basic generators
* Not integrated with authentication systems

---

## Future Scope

* Integration with real quantum hardware
* Add password strength analyzer
* Build browser extension
* Integrate with password managers
* Mobile app version


---
