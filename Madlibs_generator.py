with open ("story.txt","r") as f:
    story= f.read()

start ="<"
end=">"
start_of_index=-1

words = set()
for i,char in enumerate(story):
    if char==start:
        start_of_index=i
    if char== end and start_of_index !=-1:
        word = story[start_of_index:i+1]
        words.add(word)
        start_of_index=-1


#print(words)

answers={}
for char in words:
    answer=input("Enter your answer for"+char+": ")
    answers[char]=answer
    story=story.replace(char,answer)

#print(answers)
print(story)

