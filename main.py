def add_flashcard(flashcards):
    question = input("Enter a Question: ")
    answer = input("Enter the Answer: ")
    flashcards.append({"question": question, "answer": answer})
    print("Flashcard added")

def review_flashcards(flashcards):
    num_correct = 0

    for i, flashcard in enumerate(flashcards):
        print(f"Flashcard {i} of {len(flashcards)}")
        print(f"Question: {flashcard['question']}")
        user_answer = input(f"Your answer: ").strip()
        answer = flashcard["answer"]

        if user_answer.lower() == answer.lower():
            print("Correct!")
            num_correct += 1
        else:
            print(f"Incorrect. The correct answer is {answer}")

    print(f"You've completed the deck. You scored {num_correct} out of {len(flashcards)}")

def main():
    flashcards = []

    while True:
        print("\n --- Welcome to FlashCards! ---")
        print("1. Add a new Flashcard")
        print("2. Review Flashcards")
        print("3. Exit")

        choice = input(f"Please select an option (1, 2, or 3): ").strip()

        if choice == '1':
            add_flashcard(flashcards)
        elif choice == '2':
            review_flashcards(flashcards)
        elif choice == '3':
            print("Exiting. Have a wonderful day!")
            break
        else:
            print("I'm sorry that's not a choice. Please enter 1, 2, or 3")

if __name__ == "__main__":
    main()
