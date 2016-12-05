
from TrainingSetsUtil import *
from sys import argv


# c is an experimentally obtained value
def classify(message, training_set, prior = 0.5, c = 3.7e-4):
    
    """
    Returns the probability that the given message is of the given type of
    the training set.
    """
    
    msg_terms = get_words(message)
    
    msg_probability = 1
    
    for term in msg_terms:        
        if term in training_set:
            msg_probability *= training_set[term]
        else:
            msg_probability *= c
            
    return msg_probability * prior