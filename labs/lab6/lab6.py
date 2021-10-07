"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input('enter a name her in first then last order: ')
    name = name.split()
    print(name[1] + ', ' + name[0])

def company_name():
    domain = input('enter a domain in "www.<domain name>.<exstention>"')
    domain = domain.split('.')
    print('this is the company name: ' + domain[1])

def initials():
    num_of_names = eval(input('How many names will you input?: '))
    for i in range(num_of_names):
        first_name = input('what is the persons first name?: ')
        last_name = input('what is the persons last name?: ')
        print(first_name + "'s initals are: " + first_name[0] + last_name[0])

def names():
    name_list = input('enter a list of first and last names where each name is seperated by commas here: ')
    name_list = name_list.split(',')
    for name in name_list:
        parts = name.split()
        print((parts[0][0]) + (parts[1][0]))

def thirds():
    num_sent = eval(input('how many sentences do you want to compute?: '))
    for i in range(num_sent):
        sentence = input("what is the sentence you want to calculate?: ")
        print(sentence[2:-1:3])

def word_average():
    sentence = input('what is the sentence you would like to find the average of?:')
    words = sentence.split()
    acc = 0
    for word in words:
        word_len = len(word)
        acc = acc + word_len
    word_avg = acc / len(words)
    print('the average length in words is: ' , word_avg)

def pig_latin():
    x = input("what sentence would you like to translate ?: ")
    x = sentence.lower()
    x = x.split()
    for word in x:
        print(word[1:] + word[0] + 'ay' , end=' ')

def main():
    #name_reverse()
    #company_name()
    #initials()
    #names()
    #thirds()
    #word_average()
    pig_latin()
    # add other function calls here


main()
