# Re-import pandas as the code execution state was reset
import pandas as pd

# Reload the DataFrame from the CSV file due to the reset state
file_path = 'CCS.csv'
df = pd.read_csv(file_path)


# Re-define the function to parse the data without the Instructor column and adjust the Number column accordingly
def parse_row_robust(row):
    # Initialize default values for each field
    title, number, instructor, prerequisite, comments = "", "", "", "", ""

    try:
        # Attempt to split the row based on known labels
        parts = row.split("Prerequisite:")
        title_and_number = parts[0].strip()
        prerequisite = parts[1].split("Enrollment Comments:")[0].strip() if len(parts) > 1 else ""
        comments = parts[1].split("Enrollment Comments:")[1].strip() if len(parts) > 1 and "Enrollment Comments:" in \
                                                                        parts[1] else ""

        # Further split title and number, handling variations in formatting
        title_parts = title_and_number.split("\n")
        title = title_parts[0].strip() if title_parts else ""
        number_and_instructor = " ".join(title_parts[1:]).strip() if len(title_parts) > 1 else ""
        number = " ".join(number_and_instructor.split()[:2]) if number_and_instructor else ""
        instructor = " ".join(number_and_instructor.split()[2:]) if number_and_instructor else ""
        # Append "STAFF" to number if present
        number = number + " " + instructor if "STAFF" in instructor else number
    except IndexError:
        # Handle rows that don't match the expected format gracefully
        title, number, prerequisite, comments = "Error parsing", "", "", ""

    return pd.Series([title, number, prerequisite, comments])


# Apply the adjusted parsing function to each row of the DataFrame and drop the original column
df[['Title', 'Number', 'Prerequisite', 'Comments']] = df['字段1'].apply(lambda x: parse_row_robust(x))
df_cleaned = df.drop(['字段1', 'Instructor'], axis=1, errors='ignore')  # errors='ignore' to handle column not found

# Display the first few rows of the adjusted DataFrame to verify the changes
df_cleaned[['Title', 'Number', 'Prerequisite', 'Comments']].head()
