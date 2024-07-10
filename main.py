from flask import Flask, request, jsonify, render_template, redirect
import math

app = Flask(__name__)

extra_functions = {
    "sqrt": lambda x: x**0.5,
    "cos": math.cos,
    "sin": math.sin,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "pow": math.pow,
    "abs": abs,
    "ceil": math.ceil,
    "floor": math.floor,
    "round": round,
    "pi": math.pi,
    "e": math.e,
    "cosd": lambda x: math.cos(math.radians(x)),
    "sind": lambda x: math.sin(math.radians(x)),
    "tand": lambda x: math.tan(math.radians(x)),
    "cbrt": lambda x: x**(1/3),
    "hypot": lambda x, y: math.hypot(x, y),
    "atan": math.atan,
    "acos": math.acos,
    "asin": math.asin,
    "atan2": math.atan2,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
    "asinh": math.asinh,
    "acosh": math.acosh,
    "atanh": math.atanh,
    "degrees": math.degrees,
    "radians": math.radians,
    "lgamma": math.lgamma,
    "comb": math.comb,
    "perm": math.perm,
    "gcd": math.gcd,
    "isfinite": math.isfinite,
    "isinf": math.isinf,
    "isnan": math.isnan,
    "modf": math.modf,
    "trunc": math.trunc,
    "frexp": math.frexp,
    "fmod": math.fmod
}

def calculate(expression):
    try:
        result = eval(expression, {"__builtins__": None}, extra_functions)
        return result
    except KeyError as e:
        raise ValueError(f"Invalid function or operator: {str(e)}")
    except Exception as e:
        raise ValueError(f"Invalid query: {str(e)}")


@app.route('/')
def index():
    return redirect('/calculator')


@app.route('/calculator')
def calculator():
    return render_template('index.html')
@app.errorhandler(404)
def not_found(e):
  return redirect(404)

@app.route('/404')
def custom_404():
    return render_template('404.html'), 404
@app.route('/query', methods=['GET'])
def query():
    expression = request.args.get('calc')
    if not expression:
        return jsonify({"error": "No expression provided"}), 400

    try:
        result = calculate(expression)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)