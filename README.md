# strand Library

This libary contains functions to generate random strings, sentences, and paragraphs using Python.

### Notes

##### Importing
import *strand*

##### Getting single values
If you want a single character, simply put use a minWordLength and maxWordLength of 1 and a single character will be generated. By setting three of the character types to False and keeping one as True, you can specifically generate a lowercase letter, symbol, etc.

The same can be done for a one-word sentece. Set minWords & maxWords to 1 and a single word, with a capitalized first character and period will be generated.

### Functions

##### strand.getString(*int minWordLength, int maxWordLength, bool lowercase, bool uppercase, bool symbols, bool numbers*)

Returns a random string of specified characters. By setting lowercase, caps, symbols, and numbers to True or False,
you can control which characters your string will be comprised of. 

##### strand.getSentence(*int minWords, int maxWords, int minWordLength, int maxWordLength, bool lowercase, bool uppercase, bool symbols, bool numbers*)

Returns a random sentence with a length between minWords and maxWords. All other parameters are used to define the characters used for the strings in the sentence. Sentences will be returned with a capital letter and period.

##### strand.getParagraph(*int minSentences, int maxSentences, int minWords, int maxWords, int minWordLength, int maxWordLength, bool lowercase, bool uppercase, bool symbols, bool numbers*)

Returns a random paragraph with a number of sentences between minSentences and maxSentences. All other parameters are used in the calling of the getSentence and getString functions. Paragraphs are returned with a line break at the end, so you can call this function multiple times to create a full text with multiple paragraphs.

### Default Values
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

### Definitions
The four character types specified above are lowercase, uppercase, symbols, and numbers.

Lowercase includes any of the following characters: abcdefghijklmnopqrstuvwxyz

Uppercase includes any of the following characters: ABCDEFGHIJKLMNOPQRSTUVWXYZ

Numbers includes any of the following characters: 1234567890

Symbols includes any of the following characters: !@#$%^&*()~`,./<>?;:'"[]{}-=_+


### To Do:

-Validation for if user enters a min number larger than a max value

-What happens if a user enters all bool parameters as false?

-What happens when lowercase is set to false?