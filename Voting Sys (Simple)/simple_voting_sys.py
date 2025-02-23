candidates = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

def display_candidates():
    print("Candidates:")
    for candidate in candidates:
        print(f"- {candidate}")

def cast_vote():
    vote = input("Enter the name of the candidate you want to vote for: ").strip()
    if vote in candidates:
        candidates[vote] += 1
        print(f"Thank you for voting for {vote}!")
    else:
        print("Invalid candidate name. Please try again.")

def display_results():
    print("\nVoting Results:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")

def main():
    while True:
        print("\nVoting System Menu:")
        print("1. Display candidates")
        print("2. Cast vote")
        print("3. Display results")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '1':
            display_candidates()
        elif choice == '2':
            cast_vote()
        elif choice == '3':
            display_results()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
