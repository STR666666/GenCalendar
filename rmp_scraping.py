import ratemyprofessor


def get_professor_data(school_name, professor_name):
    school = ratemyprofessor.get_school_by_name(school_name)
    professor = ratemyprofessor.get_professor_by_school_and_name(school, professor_name)
    if professor is not None:
        return {
            "name": professor.name,
            "department": professor.department,
            "rating": professor.rating,
            "difficulty": professor.difficulty,
            "num_ratings": professor.num_ratings,
            "would_take_again": round(professor.would_take_again,
                                      1) if professor.would_take_again is not None else "N/A"
        }
    else:
        return None


# Ask user for input
user_input = input("Enter the names of professors (separated by commas): ")
professor_names = [name.strip() for name in user_input.split(',')]

# School name - assuming it's the same for all professors
school_name = "University of California Santa Barbara"

# Fetch data for each professor
professor_data_list = []
for name in professor_names:
    professor_data = get_professor_data(school_name, name)
    if professor_data:
        professor_data_list.append(professor_data)
    else:
        print(f"Professor {name} not found.")


# Function to calculate the weighted score
def calculate_score(rating, difficulty, rating_weight, difficulty_weight):
    normalized_difficulty = 5 - difficulty  # Inverting the difficulty score
    score = rating * rating_weight + normalized_difficulty * difficulty_weight
    return score


# Ask for user preferences
rating_weight = float(input("Enter your preference weight for rating (0-100): "))
difficulty_weight = float(input("Enter your preference weight for difficulty (0-100): "))

# Ensure weights sum to 100
if rating_weight + difficulty_weight != 100:
    print("Error: The weights must sum up to 100.")
else:
    # Calculate scores for each professor and determine the best
    best_professor = None
    highest_score = -1

    for professor in professor_data_list:
        score = calculate_score(professor['rating'], professor['difficulty'], rating_weight / 100,
                                difficulty_weight / 100)
        if score > highest_score:
            highest_score = score
            best_professor = professor

    if best_professor:
        print(
            f"The best professor based on your preferences is {best_professor['name']} with a score of {highest_score:.2f}")
    else:
        print("No suitable professor found based on the criteria.")


'''# Fetch and display data for each professor
for name in professor_names:
    professor_data = get_professor_data(school_name, name)
    if professor_data:
        print(f"{professor_data['name']} works in the {professor_data['department']} Department of {school_name}.")
        print(f"Rating: {professor_data['rating']} / 5.0")
        print(f"Difficulty: {professor_data['difficulty']} / 5.0")
        print(f"Total Ratings: {professor_data['num_ratings']}")
        print(f"Would Take Again: {professor_data['would_take_again']}")
    else:
        print(f"Professor {name} not found.")
'''

