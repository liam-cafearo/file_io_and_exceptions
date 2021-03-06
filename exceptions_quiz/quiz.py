import sys


def get_questions():
    with open('quiz.txt') as f:
        lines = f.readlines()

    return [(lines[i], lines[i + 1].strip()) for i in range(0, len(lines), 2)]


# don't understand this part down to next comment
def within2Characters(s1, s2):
    if len(s1) != len(s2):
        return False
    
    difference = 0
    for s1_letter, s2_letter in zip(s1, s2):
        if s1_letter != s2_letter:
            difference += 1
    
    return difference < 3

def load_riddles():
    # populates riddles variable
    try:
        return get_questions()
    except IOError:
        print 'Error reading questions file: %s' % e
        sys.exit()
    except IndexError:
        print 'Error: All questions in the questions file must have answers.'
        sys.exit()

def run_game(riddles):
    # Starts interaction with user
    score = 0
    total = len(riddles)

    for question, answer in riddles:
        tries = 3

        while tries > 0:
            guess = raw_input(question)
            tries -= 1
            if guess == "":
                print 'Enter was hit'
                guess = raw_input(question)
            
            if within2Characters(guess, answer):
                score += 1
                break
            elif tries > 0:
                print 'Nope. %s more tries' % tries
            else:
                print 'Better luck next time'

    print 'You got %s out of %s questions correct' % (score, total)


if __name__ == '__main__':
    riddles = load_riddles()
    run_game(riddles)