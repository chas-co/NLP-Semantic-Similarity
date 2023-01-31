import spacy

nlp = spacy.load('en_core_web_md')

descriptions = []
movies_dict ={}
with open("movies.txt","r") as movie_file:
    movies = movie_file.readlines()
    for line in movies:
        movie = line.split(":")
        movies_dict[movie[0].strip(" ")] = movie[1].strip(" ")

test_desc = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
        
#print(movies_dict)
def watch_next(desc):
    token_ = nlp(desc)
    similarity_score = {}
    for key in movies_dict:
        token = nlp(movies_dict[key])
        similarity_score[key] = token_.similarity(token)
        max_score = max(similarity_score.values())
        value = {i for i in similarity_score if similarity_score[i]==max_score}
    print(similarity_score)
    print("We recommend you watch",value)


watch_next(test_desc)