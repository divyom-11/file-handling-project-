quiz_data = [
    {"question": "What does a data scientist do primarily?", "choices": ["A) Develops hardware", "B) Writes content", "C) Analyzes and interprets complex data", "D) Designs clothing"], "answer": "C"},
    {"question": "Which programming language is most commonly used for data analysis?", "choices": ["A) Java", "B) Ruby", "C) Python", "D) HTML"], "answer": "C"},
    {"question": "Which of the following is a popular library for data manipulation and analysis in Python?", "choices": ["A) NumPy", "B) Pandas", "C) Matplotlib", "D) Scikit-learn"], "answer": "B"},
    {"question": "Which algorithm is commonly used for classification in data science?", "choices": ["A) K-means", "B) Linear Regression", "C) Decision Tree", "D) Apriori"], "answer": "C"},
    {"question": "What is the purpose of a confusion matrix in data science?", "choices": ["A) To measure the accuracy of a model", "B) To store data", "C) To manipulate datasets", "D) To visualize data"], "answer": "A"}
]

def take_quiz(quiz):
    score = 0
    for item in quiz:
        print(item["question"])
        for choice in item["choices"]:
            print(choice)
        answer = input("Enter the correct option (A/B/C/D): ")
        if answer.upper() == item["answer"]:
            score += 1
    return score

def save_score(score, filename="quiz_scores.txt"):
    with open(filename, "a") as file:
        file.write(f"Score: {score}\n")

def main():
    print("Welcome to the Data Science Quiz App!")
    score = take_quiz(quiz_data)
    print(f"Your score is: {score}/{len(quiz_data)}")
    save_score(score)
    print("Your score has been saved.")

if __name__ == "__main__":
    main()
