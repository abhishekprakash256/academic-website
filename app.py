"""
The flask application to rnder the website.
"""



from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve the main index.html on the route you want

STATIC_DIR = '/Users/abhi/academic-website'

@app.route('/')
def serve_index():
    #print("Serving index.html")
    return send_from_directory(STATIC_DIR, 'index.html')

# Serve any other static file from the same folder
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True, port=5100)

