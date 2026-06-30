#Content Recommendation System 
import json

class ContentRecommendationSystem:
    def __init__(self):
        self.content_library = {
            "Movies": {
                "Action": ["Mad Max", "John Wick", "Avengers"],
                "Comedy": ["The Hangover", "Superbad", "Step Brothers"],
                "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
            },
            "Music": {
                "Pop": ["Blinding Lights", "Shape of You", "Uptown Funk"],
                "Rock": ["Bohemian Rhapsody", "Hotel California", "Stairway to Heaven"],
                "Hip-Hop": ["Sicko Mode", "Lose Yourself", "God's Plan"]
            }
        }
        self.user_data = {}
        self.load_user_data()

    def load_user_data(self, filename='_media/_content/user_data.json'):
        try:
            with open(filename, 'r') as file:
                self.user_data = json.load(file)
        except FileNotFoundError:
            self.user_data = {}
        
    def save_user_data(self, filename='_media/_content/user_data.json'):
        with open(filename, 'w') as file:
            json.dump(self.user_data, file, indent=4)
    
    def watch_history(self, user_id, category, genre, content_title):
        if user_id not in self.user_data:
            self.user_data[user_id] = {
                "Movies" : {},
                "Music" : {}
            }
        if genre not in self.user_data[user_id][category]:
            self.user_data[user_id][category][genre] = []
        if content_title not in self.user_data[user_id][category][genre]:
            self.user_data[user_id][category][genre].append(content_title)
        self.save_user_data()
        return self.user_data[user_id]

    def recommend_content(self, user_id, category):
        if user_id not in self.user_data:
            return f"User {user_id} does not have watch history."
        user_genres = self.user_data[user_id].get(category, {})
        recommendations = []
        for genre, watched_content in user_genres.items():
            available_content = set(self.content_library[category].get(genre, [])) - set(watched_content)
            recommendations.extend(available_content)
        return recommendations if recommendations else "No new content"
    
system = ContentRecommendationSystem()
# print(system.watch_history("User001", "Movies", "Action", "John Wick"))
# print(system.watch_history("User001", "Movies", "Action", "Mad Max"))
# print(system.watch_history("User002", "Music", "Pop", "Blinding Lights") )
# print(system.recommend_content("User001", "Movies"))
# print(system.recommend_content("User001", "Music"))
# print(system.recommend_content("User011", "Movies"))

