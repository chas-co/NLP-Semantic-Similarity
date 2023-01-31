import spacy

#load the model and assign a variable
nlp = spacy.load('en_core_web_sm')

#process the words
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

#display similarity
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#using for loop to compare similarty of multiple words
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#comparing similarities of sentences   
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


"""
Notes

The similarity was relavitely high between fruit & fruit(0.66) and animal & animal(0.59).
The similarity was quite low betwen fruit and animal except in the case of 
monkey-banana(about 0.4)

With the simpler language model ‘en_core_web_sm’ the similarity between the apple-cat and apple-monkey 
was highest(0.62). Cat-monkey also has a high similarity (about 0.56). The similarity between the banana 
and monkey reduced significantly(0.34).
"""