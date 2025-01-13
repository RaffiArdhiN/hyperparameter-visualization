from flask import Flask, request, jsonify,  render_template
from gradient_descent import grad_descent
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compute', methods=['POST'])
def compute():
    try:
        data = request.json.get('data', [])
        initial_line = request.json.get('initial_line', [0, 0])
        learning_rate = request.json.get('learning_rate', 0.01)
        iterations = request.json.get('iterations', 100)
        
        print(f"Received data: {data}")
        print(f"Learning Rate: {learning_rate}, Iterations: {iterations}")
        
        history, final_m, final_c = grad_descent(data, initial_line, learning_rate, iterations)
        
        return jsonify({
            "m" : final_m,
            "c" : final_c,
            "positions" : history
        })
        
    except Exception as e:
        print(f"Error during /compute: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)