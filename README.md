Comment Checker
===================
A tool for the problem setting team to identify whether some user is trying to share code in the discussion forum of an on going contest or discuss the solution.

----------
#### <i class="icon-refresh"></i> Identifying the Code
-------------
The code is easy to identify if placed in a code snippet within triple backticks.
But not all users place their code within code snippet, which makes the process a little harder.
![]( https://github.com/ishan-nitj/Comment-Checker/blob/master/1.png?raw=true)

#### <i class="icon-pencil"></i>A Probabilistic Model

This is a probabilistic model which works by identifying the keywords, operators and other symbols in a comment and then assigns a probability that a comment contains a code from a particular language. Currently, this model supports three languages:C++,Python and Java.

#### <i class="icon-file"></i>Not all comments which contain keywords are codes

Consider the comment
> is this True 

Although all three words in this comment are keywords in Python, this comment is not a code.So we cannot discretely specify whether a comment will be a  code.

----------
#### <i class="icon-refresh"></i> Running the Code
-------------
- Run python main.py and provide the comment in file testing

----------
#### <i class="icon-refresh"></i> Dependencies
-------------
- sudo pip install nltk
- python> nltk.download()































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































