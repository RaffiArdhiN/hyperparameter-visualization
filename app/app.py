from flask import Flask, request, jsonify
from gradient_descent import grad_descent

app = Flask(__name__)

@app.route('/compute', methods=['POST'])
def compute():
    try:
        data = request.json.get('data', [])
        initial_line = request.json.get('initial_line', [0, 0])
        learning_rate = request.json.get('learning_rate', 0.01)
        iterations = request.json.get('iterations', 100)
        
        if not data or not isinstance(data, list):
            # raise ValueError("Invalid data")
            return jsonify({"error": "Invalid data"}), 400
        
        final_m, final_c = grad_descent(data, initial_line, learning_rate, iterations)
        
        return jsonify({"m": final_m, "c": final_c})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)