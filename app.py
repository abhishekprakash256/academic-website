"""
The flask application to rnder the website.
"""



from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)

# Serve the main index.html on the route you want

## For local development, you can set the STATIC_DIR to the path where your static files are located. -- /Users/abhi/academic-website

## For Production use the path where your static files are located. -- /home/ubuntu/academic-website

STATIC_DIR = '/home/ubuntu/academic-website'

# Serve index.html
@app.route('/academic-website/')
def serve_index():
    return send_from_directory(STATIC_DIR, 'index.html')

# Serve static assets (CSS, JS, etc.)
@app.route('/academic-website/<path:filename>')
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

# API endpoint
#https://api.meabhi.me/{microservice}/v{version}/{resource}/{optional-action}
@app.route('/academic-website/v1/page', methods=['GET'])
def get_page_data():
    return jsonify({"message": "Hello from /academic-website/api/v1/page"})



# Gunicorn will use this
app_wsgi = app



if __name__ == '__main__':
    app.run(debug=True, port=5100)

