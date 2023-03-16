quiz = {
    "question1": {
        "question": "The first foreigner to invite India was?",
        "answer": "Prasenajit",
    },
    "question2": {
        "question": "Which language was used in the literature of the Sangam period?",
        "answer": "Tamil",
    },
    "question3": {
      "question": "Lord Buddha was born in?", 
      "answer": "Lumbini"
    },
    "question4": {
        "question": "Who was the first Indian to crack the British Indian Civil Services Examination for the first time in Indian History?",
        "answer": "Satyendranath Tagore",
    },
    "question4": {
        "question": "Which is also called the Southernmost Himalayas?",
        "answer": "Siwaliks",
    },
    "question5": {
        "question": "Which is the popular name for the Indian islands on the Arabian Sea?",
        "answer": "Lakshadweep Islands",
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'],"\n")
    answer = input("Answer: ")
    
    if answer.lower() == value['answer'].lower():
        print("\nCorrect\n")
        score += 1
        print("Your score is:", score,"\n")
    
    else:
        print("\nWrong!\n")
        print("The answer is:",value['answer'],"\n")
        print("Your score is:",str(score),"\n")
        
print(f"You got {str(score)} out of {len(quiz)} questions correctly.")
print(f"\nYour percentage is {str(int(score/len(quiz)*100))}%.\n")
