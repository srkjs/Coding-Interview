# Password Strength

A password consists of lowercase English letters only and is valid only if it contains at least one vowel and at least one consonant. Vowels are the characters 'a', 'e', 'i', 'o' and 'u'. The rest are consonants. The strength of a password is defined as the maximum number of contiguous subsegments the entire password can be divided into such that each subsegment is a valid password.
<br />
<br />
Given a `password` string, find its strength. Return 0 if the password itself is not valid.
<br />
<br />
**Note:** A subsegment of a string is a segment composed of contiguous characters of the original string, taken in the same order.
<br />
<br />
> **Example**
<br />
`String password` = "thisisbeautiful"
<br />
<br />
This password can be divided into 6 subsegments: "this", "is", "be", "aut", "if" and "ul". Each segment contains at least one vowel and one consonant.
<br />
<br />


## **Test Cases**
<br />
1. Input - 'thisisbeautiful' | Output - 6 | Segments - ['thi', 'si', 'sbe', 'aut', 'if', 'ul']
2. Input - 'aeiou'           | Output - 0 | Segments - [] 
3. Input - 'rhythm'          | Output - 0 | Segments - []
4. Input - 'abcdfg'          | Output - 1 | Segments - ['abcdfg']
5. Input - 'zyxwvuu'         | Output - 1 | Segments - ['zyxwvuu']

<br />

## **Solution -**
```Python
def findPasswordStrength(password):
    containsVowel = False
    containsConstant = False
    vowels = 'aeiou'
    count = 0
    for char in password:
        if char in vowels:
            containsVowel = True
        else:
            containsConstant = True
        if containsVowel and containsConstant:
            count += 1
            containsVowel, containsConstant = False, False
    return count
```
## **Complexity -**
> Time : O(n), where n is the number of letters in password.
> Space : O(1), constant space.

<br />
To know how the password is split to find the strength, refer [solution](passwordStrength.py "Password Strength").


