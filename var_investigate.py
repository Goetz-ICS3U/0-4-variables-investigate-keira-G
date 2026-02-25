"""
author:keira
date:2026-02-10
Investigating Variables
"""

# Input
name = "keira"
grade = 11
favourite_exclamation = "huh"
least_favourite_colour = "orange"
is_cool = True
math_test_score = 87
sister_name = None

slope = 8
y_intercept = 3
x = 4
y = slope * x + y_intercept

# Processing / Output
print(
    f"Hey guys, my name is {name} and I am currently in grade {grade}. "
    + f"Yesterday, there was a spider in the classroom that made me yell {favourite_exclamation} whiile I was taking a math test with my {least_favourite_colour} pen :/ "
    + f"One of the questions on the test was wether or not I thought Elvis was cool, so I obviously put {is_cool} to get the answer right... "
    + f"Turns out that I only scored a {math_test_score} on the test. One of the qusetions was asking me to write the equation for a line "
    + f"with a slope of {slope} and a y-intercept of {y_intercept} so I wrote y = {slope}x + {y_intercept}, but I did not notice the x value of {x} in the question "
    + f"so I needed to, on the next line, say that the value of y was {y}. "
    + f"I told my sister {sister_name} about this and she just laughed at me 🙄"
    + "Anyway, that's the story of my math test."
)
