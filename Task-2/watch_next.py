import spacy

#we specify the model we want to use
nlp = spacy.load('en_core_web_md')

#declare and initialise a dictionary to hold movies and their desciptions
movies_dict ={}

#open the movie file and read its content into the dictionary
with open("movies.txt","r") as movie_file:
    movies = movie_file.readlines()
    for line in movies:
        movie = line.split(":")
        movies_dict[movie[0].strip(" ")] = movie[1].strip(" ")

#the description of the movie we want to find similar movies to
test_desc = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
        
# Recommender function
def watch_next(desc):
    #we tokenise the description of previously watched movie
    token_ = nlp(desc)
    #create a dictionary to store similarity scores
    similarity_score = {}
    #loop through all the movies from the file tokenise the descriptions and compute the similarity
    for key in movies_dict:
        token = nlp(movies_dict[key])
        similarity_score[key] = token_.similarity(token)
        
    #find the max score and the key associated to it
    max_score = max(similarity_score.values())        
    value = {i for i in similarity_score if similarity_score[i] == max_score}

    #tell the user what to watch next
    print("We recommend you watch",value)


watch_next(test_desc)