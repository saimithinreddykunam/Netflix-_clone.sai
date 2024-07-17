from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import sqlite3
app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/')
def index():
    conn = get_db_connection()
    videos = conn.execute('SELECT * FROM videos').fetchall()
    conn.close()
    return render_template('index.html', videos=videos)
@app.route('/video/<int:video_id>')
def video(video_id):
    conn = get_db_connection()
    video = conn.execute('SELECT * FROM videos WHERE id = ?', (video_id,)).fetchone()
    conn.close()
    if video is None:
        return redirect(url_for('index'))
    return render_template('video.html', video=video)
@app.route('/static/videos/<filename>')
def video_file(filename):
    return send_from_directory('static/videos', filename)
if __name__ == '__main__':
    app.run(debug=True)
