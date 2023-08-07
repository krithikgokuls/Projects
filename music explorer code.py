from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample music data (replace this with your actual data source)
music_data = [
    {"title": "Song 1", "artist": "Artist 1", "genre": "Pop"},
    {"title": "Song 2", "artist": "Artist 2", "genre": "Rock"},
    # ... more data
]

# Define a route to get music recommendations
@app.route('/get_recommendations', methods=['GET'])
def get_recommendations():
    user_preferences = request.args.get('preferences')  # Get user preferences from query parameter

    # Here you can implement your recommendation logic based on user preferences
    # For simplicity, let's just filter the music_data based on genre
    recommended_songs = [song for song in music_data if user_preferences.lower() in song['genre'].lower()]

    return jsonify(recommended_songs)

if __name__ == '__main__':
    app.run(debug=True)
