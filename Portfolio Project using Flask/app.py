from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Sample project data - replace with your own
    projects = [
        {
            'title': 'Project 1',
            'description': 'A responsive web application built with Flask and SQLAlchemy.',
            'technologies': ['Python', 'Flask', 'SQLAlchemy', 'HTML', 'CSS']
        },
        {
            'title': 'Project 2',
            'description': 'An e-commerce platform with user authentication and payment integration.',
            'technologies': ['Python', 'Flask', 'PostgreSQL', 'Stripe']
        },
        {
            'title': 'Project 3',
            'description': 'A real-time chat application using WebSocket technology.',
            'technologies': ['Python', 'Flask', 'WebSocket', 'JavaScript']
        }
    ]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)