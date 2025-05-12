"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

# Once upon a time 👦 went to the park and they play with 🐈
# 0(once) 2(upon) 7(a) 9(time) 1(👦) 15(went) 10(to) 8(the) 4(park) 14(and) 19(they) 17(play) 6(with) 12(🐈)

story = [words[0], words[2], words[7], words[9], words[1], words[15], words[10], words[8], words[4], words[14], words[19], words[17], words[6], words[12]]

# Create a story using the words in the list

# Display the story to the user
print(' '.join(story))