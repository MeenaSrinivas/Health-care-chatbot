from nltk.chat.util import Chat,reflections
pairs = [
    [
        r"hi|hello|hey",
        ["Hello there!! Welcome to Health Care Chatbot.What can I do for you!!","I,m glad to reach out..\nI'm here to answer all your queries...😊😊","Heyy, How can I help you today?",]
    ],
    
    [
        r"(?=.*fever)",
        ["Stay in bed and rest.\nKeep yourself hydrated. ... TAke Combliflam Medicine.\nIf not getting well in 5 hours contact Dr. Ramesh 9952347899",]
    ],
    
    [
        r"ok|okay|kk|okk",
        ["Take care:),have a nice day",]
    ],
    
    [
        r"(.*headache.*)",
        ["Take a deep breath","Get enough sleep.","Don't skip meals.","Exercise regularly.","Reduce stress.","Reduce caffeine.",]
    ],
    
    [
        r"cold|flu",
        ["Expert doctor for Flu Or Cold.Contact for for info.. 9898986523",]
    ],
    
    [
        r"Diarrhea",
        ["Keep yourself hydrated\n And Best medicine for diarrhea... donstal",]
    ],
    
    [
        r"Skin Infections",
        ["Apply cold compresses to your skin several times a day to reduce itching and inflammation.","Take over-the-counter antihistamines to decrease itching.","\nUse topical creams and ointment to reduce itching and discomfort."]
    ],
    
    [
        r".*Appointments",
        ["For appointments contact betwwen 9 AM - 6 PM ",]
    ],
    
    [
        r"Emergency",
        ["Call At 0265-58568",]
    ],
    
    [
        r"(?=.*maleria)",
        ["Consume ginger as much possible or ginger juice...",]
    ],
    
    [
        r"thank you|thankuhh|thanks|thanx|tq|thank u",
        ["You are Welcome😊,Take Care..",]
    ],
    
    [
        r"quit",
        ["Bye","Have a nice day","Good day..😊",]
    ],
]

def chatty():
    print("I am chatbot.Based on ur symptoms i will tell disease and suggest treatments,doctors,diet..😊😊")
    chat = Chat(pairs,reflections)
    chat.converse()
    
if __name__ == "__main__":
    chatty()
