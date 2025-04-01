from flask import Flask, render_template, request
from agent import graph  # Import the compiled graph from agent.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data_description = request.form['data_description']
        # Run the agent workflow with the input
        initial_state = {"data_description": data_description}
        result = graph.invoke(initial_state)
        # Pass results to the result template
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)