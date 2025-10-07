# 1. Slicing & Methods
log_line = "ERROR 2024-10-06 14:35:01 Database connection failed"
print(log_line[0:5], log_line[26:52])

# 2. Formatting using .format()
log_level = log_line[0:5]
message = log_line[26:52]

summary = "[{}] -> {}".format(log_level, message)
print(summary)


# 3. Validation & Search
def find_all_emails(text):
    words = text.split()
    emails = []
    for word in words:
        if "@" in word:
            emails.append(word)
    return emails

sample_text = "For signing in, log in your name@isu.edu.ph"
print(find_all_emails(sample_text))


# 4. Complex Manipulation
def convert_to_title_case(text):
    words = text.split('_')
    title_case = ' '.join(word.capitalize() for word in words)
    return title_case

print(convert_to_title_case("customer_account_id"))
