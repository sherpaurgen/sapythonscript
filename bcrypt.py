    Example of bcrypt hash function/algorithm
    
>>> import bcrypt
>>> from bcrypt import hashpw,gensalt
>>> hashed = hashpw("urgensh",gensalt())
>>> print hashed
$2b$12$PaBTav0bYrNHKSKIaX210eg/o0lhSByRua4ALiVbB9JpDuKcWl9ry
>>> hashed = hashpw("urgensh",gensalt())
>>> print hashed
$2b$12$Q7fExBSv5qHIpli7tUFOsu0y9hqWFpHyGDwRF9sNPo6LYMWDKf6he
>>> def checkme(x):
...     if hashpw(x,hashed) == hashed:
...         print "it matched"
...     else:
...         print "password fail"
... 
>>> checkme("urgensh")
it matched
>>> checkme("urgenshd")
password fail

