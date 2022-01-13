punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = []
with open('positive_words.txt','r') as fileR:
    L = fileR.readlines()
    for i in L:
        positive_words+=i.split()

negative_words = []
with open('negative_words.txt','r') as fileR:
    L = fileR.readlines()
    for i in L:
        negative_words += i.split()

def remove_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s=s.replace(i,'')
    return s

def get_positive_words(s):
    my = s.split()
    count = 0
    for i in my:
        if i in positive_words:
            print('Positive Words Are:  ',i)
            count+=1
    return count

def get_negative_words(s):
    count = 0
    my=s.split()
    for i in my:
        if i in negative_words:
            count+=1
            print('Negative Words Are:  ',i)
    return count


p=0
n=0

with open('Input Data.txt','r') as fileR:
    L=fileR.readlines()
    for i in L:
        remove_punctuation(i)
        p+=get_positive_words(i)
        n+=get_negative_words(i)
    print('Total Postive Words In The Data: {}'.format(p))
    print('Total Negative Words In The Data: {}'.format(n))