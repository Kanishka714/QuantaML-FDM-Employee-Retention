from flask import Flask, render_template, request, jsonify
from helper import get_predictions

app = Flask(__name__)

# Initialize state variables
state = {
    'positive': 0,
    'negative': 0
}

@app.route("/")
def index():
    # Prepare data for rendering
    total = state['positive'] + state['negative']
    data = {
        'positive': state['positive'],
        'negative': state['negative'],
        'total': total
    }
    return render_template('index.html', data=data)

@app.route("/", methods=['POST'])
def my_post():
    # Retrieve form data
    city_development_index = request.form['city_development_index']
    relevent_experience = request.form['relevent_experience']
    education_level = request.form['education_level']
    total_experience = request.form['total_experience']
    last_new_job_gap = request.form['last_new_job_gap']

    # Get prediction from the helper function
    prediction = get_predictions(city_development_index, relevent_experience, education_level, total_experience, last_new_job_gap)

    # Update counts based on prediction
    if prediction == 1:
        state['positive'] += 1  # looking for a job change
    else:
        state['negative'] += 1  # not looking for a job change 

    total = state['positive'] + state['negative']
    return jsonify({
        'prediction': prediction,
        'total': total,
        'positive': state['positive'],
        'negative': state['negative']
    })

if __name__ == "__main__":
    app.run()
