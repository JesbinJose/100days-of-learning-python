
with open(r"./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

with open(r"./Input/Names/invited_names.txt") as names_file:
    names = [name.strip() for name in names_file.readlines()]


for name in names:
    new_letter = letter_contents.replace("[name]", name)
    with open(f"./output/ReadyToSend/letter_for_{name}.docx", mode="w") as completed_letter:
        completed_letter.write(new_letter)
