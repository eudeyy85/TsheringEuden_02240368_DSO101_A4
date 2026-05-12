from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def serve_home():
    # Read and render the HTML file
    html_path = os.path.join('.', 'webpage.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    return html_content

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
