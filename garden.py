import spacy

nlp = spacy.load("en_core_web_sm")

# (1)
sent_1 = "The old Indian man the American boat."
sent_2 = "The complex houses married and single soldiers and their 30 families."
sent_3 = "The horse Jonanthan raced past the barn fell."
sent_4 = "Is the fact that you are well known by the public?"
sent_5 = "Until the police arrest the drug dealers control the street."

garden_path_sentences = [sent_1, sent_2, sent_3, sent_4, sent_5]

#(2)
for s in garden_path_sentences:
    d = nlp(s)
    print([(token.orth_) for token in d])
    print([(ele, ele.label_, ele.label) for ele in d.ents])
    
#(3)
"""I have added some countries, a name and a number to the sentences to make the entity recognition work.
Otherwise, it just gives empty lists because the ents method will only recognise certain types without
training."""

#(4)
"""CARDINAL means just a cardinal number (i.e. an integer with natural size that doesn't fall under another
type). NORP stands for: nationalities or religious or political groups. The latter seems an odd 
categorisation and provides little linguistic subtlty - I wasn't expecting this."""