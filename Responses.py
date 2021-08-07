from datetime import datetime

def sample_responses(input_text):
    user_messege = str(input_text).lower()

    
    if user_messege in ("hello", "hi", "sup",):
       return "Hey! How's it going?" 

    if user_messege in ("Who are you", "who are you?", "sup",):
       return "I am ABC bot!" 

    if user_messege in ("time", "time?", "sup"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I don't understand you."
