import random
class WrongOrderException(Exception):
    pass

class NoTrueCharacterSetsException(Exception):
    pass

class ImproperParameterType(Exception):
    pass

def getString(minWordLength=3, maxWordLength=10, lowercase=True, uppercase=False, symbols=False, numbers=False):
    # Validate inputs: lengnths must be ints, min must be larger than max, character sets must be boolean, and atleast one set of characters must be set to true.
    try: 
        test = 1 + minWordLength
        test = 1 + maxWordLength
    except:
        raise ImproperParameterType("Lengths and Counts must by Integers.")
    if type(minWordLength) == bool or type(maxWordLength) == bool:
        raise ImproperParameterType("Lengths and Counts must by Integers.")
    if type(lowercase) != bool or type(uppercase) != bool or type(symbols) != bool or type(numbers) != bool:
        raise ImproperParameterType("Character set parameters must be True or False.")
    if maxWordLength < minWordLength:
        raise WrongOrderException("Minimum value must be smaller or equal to Maximum value.")
    if lowercase==False and uppercase==False and symbols==False and numbers==False:
        raise NoTrueCharacterSetsException("You must set at least one character set to true. Default values are: lowercase=True, uppercase=False, symbols=False, numbers=False.")

    # Define characters.
    lowercaseString = "abcdefghijklmnopqrstuvwxyz"
    uppercaseString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numsString= "1234567890"
    symbolsString = r"""!@#$%^&*()~`,./<>?;:'"[]{}-=_+"""

    # Add characters specified in parameters to main character string.
    charString  = ""
    if lowercase:
        charString = charString + lowercaseString
    if uppercase:
        charString = charString + uppercaseString
    if symbols:
        charString = charString + symbolsString
    if numbers:
        charString = charString + numsString
    
    # Turn it to list for ease of accessing index, use random.randint to get a length between users parameters.
    charList = list(charString)
    length = random.randint(minWordLength, maxWordLength)

    # Add random characters to string until string is as long as length.
    returnList = []
    l = 0
    while l < length:
        r = random.randint(0, len(charList)-1)
        returnList.append(charList[r])
        l+=1
    
    # Join list into return string.
    string = ''.join(returnList)
    return string



def getSentence(minWords=3, maxWords=10, minWordLength=3, maxWordLength=10, lowercase=True, uppercase=False, symbols=False, numbers=False):
    # Validate inputs: lengnths must be ints, min must be larger than max, character sets must be boolean, and atleast one set of characters must be set to true.
    try: 
        test = 1 + minWordLength
        test = 1 + maxWordLength
        test = 1 + minWords
        test = 1 + maxWords
    except:
        raise ImproperParameterType("Lengths and Counts must by Integers.")
    if type(minWords) == bool or type(maxWords) == bool or type(minWordLength) == bool or type(maxWordLength) == bool:
        raise ImproperParameterType("Lengths and Counts must by Integers.")
    if type(lowercase) != bool or type(uppercase) != bool or type(symbols) != bool or type(numbers) != bool:
        raise ImproperParameterType("Character set parameters must be True or False.")
    if maxWordLength < minWordLength:
        raise WrongOrderException("Minimum value must be smaller or equal to Maximum value.")
    if lowercase==False and uppercase==False and symbols==False and numbers==False:
        raise NoTrueCharacterSetsException("You must set at least one character set to true. Default values are: lowercase=True, uppercase=False, symbols=False, numbers=False.")

    # Get a random number of words to make between users parameters, using random.randint.
    numWords = random.randint(minWords, maxWords)
    listOfStrings = []

    # Using getString, add strings to sentence until its number of words reaches specified length above.
    w = 0
    while (w<numWords):
        string = getString(minWordLength, maxWordLength, lowercase, uppercase, symbols, numbers)
        listOfStrings.append(string)
        w+=1

    # To make the sentence seem more realistic, we will capitalize the first letter (if it's a letter) and add a period at the end.
    # Turn the first string to a list.
    firstString = listOfStrings[0]
    firstStringAsList = list(firstString)

    # If the first character of the first string can be made into uppercase, do it. Otherwise, we will generate a random 1 character
    # string from the list of uppercase letters.
    try:
        firstStringAsList[0] = firstStringAsList[0].upper()
    except Exception:
        firstStringAsList[0] = getString(1,1, False, True, False, False)
    
    # Now that the first character has been capitalized, we can turn it back to a string and add it back to the listOfStrings variable.
    firstString = ''.join(firstStringAsList)
    listOfStrings[0] = firstString
    
    # Join all strings into a sentence.
    sentence = ' '.join(listOfStrings)

    # Add a period at the end.
    sentence = sentence + "."
    
    return sentence



def getParagraph(minSentences=3, maxSentences=10, minWords=3, maxWords=10, minWordLength=3, maxWordLength=10, lowercase=True, uppercase=False, symbols=False, numbers=False):
    # Validate inputs: lengnths must be ints, min must be larger than max, character sets must be boolean, and atleast one set of characters must be set to true.
    try: 
        test = 1 + minWordLength
        test = 1 + maxWordLength
        test = 1 + minWords
        test = 1 + maxWords
        test = 1 + minSentences
        test = 1 + maxSentences
    except:
        raise ImproperParameterType("Lengths and Counts must by Integers.")
    if type(minSentences) == bool or type(maxSentences) == bool or type(minWords) == bool or type(maxWords) == bool or type(minWordLength) == bool or type(maxWordLength) == bool:
        raise ImproperParameterType("Lengths and Counts must by Integers.")
    if type(lowercase) != bool or type(uppercase) != bool or type(symbols) != bool or type(numbers) != bool:
        raise ImproperParameterType("Character set parameters must be True or False.")
    if maxWordLength < minWordLength:
        raise WrongOrderException("Minimum value must be smaller or equal to Maximum value.")
    if lowercase==False and uppercase==False and symbols==False and numbers==False:
        raise NoTrueCharacterSetsException("You must set at least one character set to true. Default values are: lowercase=True, uppercase=False, symbols=False, numbers=False.")
    
    # Validate inputs: min must be larger than max, and atleast one set of characters must be set to true.
    if maxWordLength < minWordLength or maxWords < minWords or maxSentences < minSentences:
        raise WrongOrderException("Minimum value must be smaller or equal to Maximum value.")

    if lowercase==False and uppercase==False and symbols==False and numbers==False:
        raise NoTrueCharacterSetsException("You must set at least one character set to true. Default values are: lowercase=True, uppercase=False, symbols=False, numbers=False.")
    
    # Randomly chose the number of sentences between the users parameters using random.randint.
    numSentences = random.randint(minSentences,maxSentences)

    # Call getSentence for however many sentences we need to create.
    s = 0
    paragraph = []
    while s < numSentences:
        sentence = getSentence(minWords=3, maxWords=10, minWordLength=3, maxWordLength=10, lowercase=lowercase, uppercase=uppercase, symbols=symbols, numbers=numbers)
        sentence = sentence + " "
        paragraph.append(sentence)
        s+=1

    # Join the list of sentences into one string.
    paragraph = ''.join(paragraph)

    # Add a line break at the end.
    paragraph = paragraph + "\n"

    return paragraph