class authorModeli():

    #initialize empty lists for different characteristics and then use basetext for initial model
    #characterized on function words,syntax, complexity measures, unstable words, idiosyncrasies
    #word measures are an average percentage of representation in whole texts for now. Distributions?
    #implement function words and ngrams first as koppel noted suprising accuracy
    def __init__(self, name, basetext):
        self.functionWords = {articles:0,pronouns:0,adpositions:0,conjunctions:0,auxiliaryVerbs:0,particles:0,proSentences:0,expletives:0, numbers:0, interjections:0, determiners:0}}
        self.complexityTests={}
        self.syntax={}
        self.ngrams={}

    #edit all dicts of measures
    def analyze(text):



    #implement SVM first, perhaps other models later
    #construct vector from text given
    def predict(text):

    #bundle dicts into single vector for use by svm
    def bundle():

