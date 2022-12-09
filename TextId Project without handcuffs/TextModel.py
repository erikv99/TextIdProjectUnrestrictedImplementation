#
# textmodel.py
#
# Opdracht: Tekstidentificatie
#
# Naam: Erik Veenstra

# NOTE
"""
    This version is exactly the same project with the same functionality as school wants
    except for the fact that all the (ineffective) constraints are taken off.

    This version is just how i would write it. (mostly)

    I basically use csharp styling, 
    
    Functions:
    _functionName = private function
    FunctionName = public function
    
    Class properties/vars:
    _var = private variable
    Var = public variable (property)
    
    all vars except public class properties:
    camelCase.

    Classes, Interfaces etc etc starting with a Kapital letter.
"""

# imports
from os.path import exists
import string

class TextModel:
    
    # Class properties

    # Static
    pathToText = "test.txt"

    # Dynamic
    sentences = []
    words = {}
    wordLengths = {}
    stems = {}
    sentenceLengths = {}
    numericCount = {}

    """
        Names speak for itself but here is some elaboration
            
        wordCount: Amount of words used in the model (om woorden te tellen)
        wordLengths: Length of the words (om woordlengtes te tellen)
        stems: stems (om stammen te tellen)
        sentenceLenghts: lengths of the sentences
        numericCount: Amount of used numbers (0 - 9) 
    """

    def __init__(self):
        """
            Create a TextModel.
        """

        print("TextModel creation started.")

        # Getting sentences from file
        self.sentences = self._readSentencesFromFile(self.pathToText);
        
        # Getting words from sentences
        self.words = self._getWords(self.sentences)

        # Cleaning the words
        self.words = self._cleanWords(self.words)

        # Getting the amount of words in each sentence (sentenceLengths)
        self.sentenceLengths = self._getSentenceLenghts(self.words);

        # Getting the amount of chars in each word (wordLengths)
        self.wordLengths = self._getWordLengths(self.words);


    def __repr__(self):
        """
            Display the contents of a TextModel in a readable manner
        """
        
        return "Amount of words: " + str(self.wordLengths) + "\n" \
            + "Word lengths:\n" + str(self.wordLengths) + "\n" \
            + "Stems:\n" + str(self.stems) + "\n" \
            + "Sentence lengths:\n" + str(self.sentenceLengths) + "\n" \
            + "Amount of used numbers: " + str(self.numericCount)

    def _readSentencesFromFile(self, path): 
        """
            Attempts to read sentences from given path in to a list of sentences.
        """

        # Checking if the file exists, if not printing a log and returning.
        if not exists(path):
            
            print("Given path '{}' is not valid".format(path))
            return

        try:

            # Opening the file with a context manager so we're no longer responsible for closing it.
            with open(path) as inputFile:

                # Reading content line by line (more or less), each line will be a list element.
                sentences = inputFile.read().splitlines()

        # Catching unhandled exceptions.
        except:
            print("Exception occurred while trying to read file content for path: " + path)
            return

        # Checking if the file contains any content else sending a log and returning.
        if len(sentences) == 0:

            print("File at given path '{}' is empty!".format(path))
            return

        return sentences;

    def _getWords(self, sentences):
        """
            Will return a dictionary with key: sentence number and value a list containing all words for this sentence.
        """

        words = {}

        for index in range(len(sentences)):

            sentence = sentences[index]

            # We can get the words by splitting on space.
            wordsForSentence = sentence.split("")

            # Adding the words for this sentence to the dictionary. 
            # Key is the sentence number, not the index so index + 1
            words[index + 1] = wordsForSentence;

        return words;

    def _getSentenceLenghts(self, words):
        """
            Returns a dictionary containing every sentence length (amount of words in a sentce)
            and how many times this specific length occurred in the text.

            arg sentences: list of all sentences of the text.
            returns dictionary.
        """

        sentenceLengths = {}

        for wordsForSentence in words.values():

            # Getting the amount of words in the current sentence. (element)
            sentenceLength = len(wordsForSentence)

            # Checking if added earlier 
            if sentenceLength in sentenceLengths:

                # Increasing already present entry for current length
                sentenceLengths[sentenceLength] += 1

            # if not present yet
            else:

                # Adding it 
                sentenceLengths[sentenceLength] = 1

        return sentenceLengths

    def _cleanWord(self, word):
        """
            Cleans the given word. removes kapital letters and punctuations
            Returns the cleaned word.
        """

        # Making word lowercase and using translate to remove any punctuation.
        return word.lower().translate(str.maketrans('', '', string.punctuation));

    def _cleanWords(self, words):
        """
            Removes all kapital letters and punctuations from all words.
            returns words but cleaned up (rest stays the same.)
        """

        # clean version of words.
        cleanWords = {}

        # looping through each key value pair in the words dict
        for sentenceNumber, wordsForSentence in words:
            
            # Here we will store all the cleaned words for the current sentence.
            cleanedWords = []
            
            for word in wordsForSentence:
                    
                # Adding the clean version of current word to the list
                cleanedWords.append(self._cleanWord(word));

            # Adding the cleanedWords list back to the cleanWords dict, key stays the same.
            cleanWords[sentenceNumber] = cleanedWords

    def _getWordLengths(self, words):
        """
            Returns a dictionary containing every word length (amount of chars in a word)
            and how many times this specific length occurred in the text.

            arg words: dictionary of sentence numbers and all words for each sentence number.
            returns dictionary.
        """

        wordLengths = {}

        for wordsForSentence in words.values():
            for word in wordsForSentence:

                # Getting length of current word.
                wordLength = len(word)

                # Checking if added earlier 
                if wordLength in wordLengths:

                    # Increasing already present entry for current length
                    wordLengths[wordLength] += 1

                # if not present yet
                else:

                    # Adding it 
                    wordLengths[wordLength] = 1

        return wordLengths  






