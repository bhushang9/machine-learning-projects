from flask import Flask, render_template, request
import pickle
import difflib
import pandas as pd

app = Flask(__name__)

# Load pickled models/data
try:
    similarity = pickle.load(open('models/similarity.pkl', 'rb'))
    courses_df = pickle.load(open('models/courses.pkl', 'rb'))
    course_list_dicts = pickle.load(open('models/course_list.pkl', 'rb'))
except Exception as e:
    print(f"Model loading error: {e}")
    exit()

course_names = courses_df['course_name'].tolist()

def recommend(user_input):
    # Try to find the closest course name
    matches = difflib.get_close_matches(user_input, course_names, n=1, cutoff=0.3)
    if not matches:
        return []
    
    matched_course = matches[0]
    index = courses_df[courses_df['course_name'] == matched_course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_courses = []
    for i in distances[1:21]:  # Fetch more than 6 to allow for show-more
        course_name = courses_df.iloc[i[0]].course_name
        course_url = courses_df.iloc[i[0]].course_url
        recommended_courses.append({'name': course_name, 'url': course_url})

    return recommended_courses

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended_courses = []
    selected_course = ""
    if request.method == 'POST':
        selected_course = request.form.get('course_name', '')
        recommended_courses = recommend(selected_course)
    return render_template('index.html', courses=course_names, recommendations=recommended_courses, selected_course=selected_course)

if __name__ == '__main__':
    app.run(debug=True)