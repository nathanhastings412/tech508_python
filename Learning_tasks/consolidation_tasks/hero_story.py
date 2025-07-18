from time import process_time_ns

story_1 = {
    "start" : "Bowser kidnapped Peach",
    "middle" : "Mario fought monsters and siege castles",
    "end" : "Mario saved Peach",
}

print(story_1)
print(type(story_1))
print(story_1.keys())
print(story_1.values())
print(story_1["start"])
print(story_1["middle"])
print(story_1["end"])
story_1["character"] = "mario"
print(story_1)
print(f"the end. I hope you enjoyed the story about {story_1['character']}")