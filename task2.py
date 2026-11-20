import string 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
QST = {"What are your opening and closing hours?":"We are open from 6:00 AM to 10:00 PM on weekdays, and 8:00 AM to 8:00 PM on weekends.",
       "Do you offer a free trial day?": "Yes, you can try the gym for free for one day before joining.",
       "What level is this class?":"It is an all-levels class, so beginners are very welcome.",
       "What time of day do you usually exercise?":"I prefer working out in the morning before work.",
       "Are you training for a specific goal?":"Yes, I am trying to build muscle and improve my stamina.",
       "What muscle group are you training today?":"Today is leg day, so I'm focusing on squats and lunges.",
       "Do you prefer cardio or weightlifting?":"I prefer weightlifting, though I do 15 minutes of cardio to warm up.",
       "Do you take any supplements like protein powder?":"Yes, I usually drink a whey protein shake right after my workout.",
       "Is there a swimming pool or a sauna in this club?":"Yes, there is a heated pool, and the sauna is inside the locker room.",
 }
def clean_text(text):
    text=text.lower()
    text="".join(char for char in text if char not in string.punctuation)
    return text

question = list(QST.keys())
answers = list(QST.values())
cleaned_questions = [clean_text(q) for q in question]
vectorizer = TfidfVectorizer(stop_words='english')
question_vectors = vectorizer.fit_transform(cleaned_questions)



while True :
     user = input("YOU (or 'exit' to quit) :")
     if  user.lower() == 'exit' :
      print("goodbye")
      break
     clean_user = clean_text(user)
     vector_user = vectorizer.transform([clean_user])
     similarities = cosine_similarity(vector_user,question_vectors)
     best_match_index = similarities.argmax()
     best_score = similarities[0][best_match_index]
     if best_score < 0.2  :
      print("sorry, I don't understand that question")

     else :
       print (answers[best_match_index])



    
