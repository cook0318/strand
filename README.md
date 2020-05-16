# strand Library

This libary contains functions to generate random strings, sentences, and paragraphs using Python.

## Notes

##### Importing
I'm not 100% sure how to make my Library easily installable. The best way I can think of is as follows:

*Find where your Python Libraries folder is. If you don't know where it is, the easiest way to find it is:
    
    *Run Python either from your CMD line or directly the Python program.
    
    *Import a package you know you have. For me, I use "import random", because this library uses it anyway.
    
    *After importing, type "package.__file__" where pacakge is the package you imported. That's the package name,
    a period, two underscores, the word file, and two more underscores.
    
    *Go to the folder where the package file is located. In my case, its "C:\\Users...Programs\\Python\\Python37-32\\lib\\random.py",
    so we will be doing the rest of the steps in the /lib folder.

*Create a new file called strand.py

*[Open the raw code](https://raw.githubusercontent.com/cook0318/strand/master/library/strand.py), copy it and save the file.

*You should now be able to write `import strand` in any Python file on your machine and have access to the library.

Note that any time there is an update, you will have to open the raw code and repeat the steps again, replacing it in your directory. If anyone has an easier way to do this, please let me know.

##### Getting single values
If you want a single character, simply put use a minWordLength and maxWordLength of 1 and a single character will be generated. By setting three of the character types to False and keeping one as True, you can specifically generate a lowercase letter, symbol, etc.

The same can be done for a one-word sentece. Set minWords & maxWords to 1 and a single word, with a capitalized first character and period will be generated.

## Functions

##### strand.getString(*int minWordLength, int maxWordLength, bool lowercase, bool uppercase, bool symbols, bool numbers*)

Returns a random string of specified characters. By setting lowercase, caps, symbols, and numbers to True or False,
you can control which characters your string will be comprised of. 

##### strand.getSentence(*int minWords, int maxWords, int minWordLength, int maxWordLength, bool lowercase, bool uppercase, bool symbols, bool numbers*)

Returns a random sentence with a length between minWords and maxWords. All other parameters are used to define the characters used for the strings in the sentence. Sentences will be returned with a capital letter and period.

##### strand.getParagraph(*int minSentences, int maxSentences, int minWords, int maxWords, int minWordLength, int maxWordLength, bool lowercase, bool uppercase, bool symbols, bool numbers*)

Returns a random paragraph with a number of sentences between minSentences and maxSentences. All other parameters are used in the calling of the getSentence and getString functions. Paragraphs are returned with a line break at the end, so you can call this function multiple times to create a full text with multiple paragraphs.

## Default Values
-lowercase : True

-uppercase: False

-symbols: False

-numbers: False

-minWordLength: 3

-maxWordLength: 10

-minWords: 3

-maxWords: 10

-minSentences: 3

-maxSentences: 10

## Definitions
The four character types specified above are lowercase, uppercase, symbols, and numbers.

Lowercase includes any of the following characters: abcdefghijklmnopqrstuvwxyz

Uppercase includes any of the following characters: ABCDEFGHIJKLMNOPQRSTUVWXYZ

Numbers includes any of the following characters: 1234567890

Symbols includes any of the following characters: !@#$%^&*()~`,./<>?;:'"[]{}-=_+


## To Do:
-Code should ordered the same format for every method.

-User cannot pass Bool values if no min/max values have been written. Maybe possible to take generic inputs (a,b,c,d,e,f) and convert them? IE, if a is found to be a Bool value, we know it is for lowercase, etc.

-Could eventually put validation into own function.