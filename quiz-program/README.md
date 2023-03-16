# This code is a simple quiz game that asks the user a set of multiple-choice questions and checks their answers against a predefined set of correct answers.

1. This code creates a dictionary called `quiz` that contains sets of questions and answers. Each set of questions and answers is defined as a nested dictionary with keys question and answer.

2. After that, a variable called `score` is initialized to `0`.

3. The code then loops through each set of questions and answers in the `quiz` dictionary using a `for` loop. For each set of questions and answers, it prints the question and waits for user input to answer the question.

4. If the user's answer matches the corresponding answer in the `quiz` dictionary (case-insensitive), the code prints "Correct" and increments the `score` by `1`. If the user's answer does not match the corresponding answer in the quiz dictionary, the code prints "Wrong!" and displays the correct answer, along with the user's current score.

5. After all questions have been asked, the code prints the user's final score and percentage based on the number of questions answered correctly.
