first_name = "nick"
last_name = "adair"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}, how are you today?")

name = "chad adair" 
second_name = "nick adair"
print(f"Hello {name.title()}, how are you today?")
print(f"Hello {name.upper()} and {second_name.title()}, how are you today?")

#my favorite quote
author_name = "seals"
line_1 = "Instead of saying \"I dont have the time.\""
line_2 = "Try saying, \"it's not a priority.\""
line_3 = "This will change the way you think."
line_4 = "All of the sudden those things you \"don't have time for\" become a priority."
line_5 = "Stop being unproductive and do the important stuff that you always put off."
line_6 = "Remember that there is always someone who is busier or less advantaged working harder harder than you."
message = (f"The {author_name.upper()} say, {line_1} {line_2} {line_3} {line_4} {line_5} {line_6}") 
print(message)

name = " nick "
print(name)
print(name.rstrip())
print(name.strip())