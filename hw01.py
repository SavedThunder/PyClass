"""The Game of Hog."""

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.
"""Higher Order Functions used for simulations of dice rolls.

Definition: An n-sided dice function takes no arguments and always returns an int from 1 to n, inclusive.

Types of n-sided dice functions:
 -  Randomized: a randomized dice function can be fair, meaning that ir produce each possible outcome 
    from 1 to n with equal probability. Examples: four_sided, six_sided
 -  Deterministic: a deterministic dice function will be used for testing.  Deterministic test dice functions always cycle
    through a fixed sequence of n values. 
 -  We write a make_fair_dice higher-order function to return a fair, randomized n-sided dice function.
 -  We write a make_test_dice higher-order function that will return a deterministic, testing n-sided dice function.
"""

from random import randint

def make_fair_dice(n):
    """Returns an n-sided fair dice function."""
    assert type(n) == int and n >= 1, 'Illegal value for number of sides'
    def dice():
        return randint(1,n)
    return dice

four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)

def make_test_dice(*outcomes):    
    """Return an n-sided dice function that cycles deterministically through outcomes - a rest parameter.

    >>> dice = make_test_dice(4, 1, 3)
    >>> dice(), dice(), dice(), dice()
    (4, 1, 3, 4)
    
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice
######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Must roll at least once.'
    # BEGIN Question 1
    tempNum = 0
    total = 0
    while(num_rolls > 0):
        tempNum = dice()
        if(tempNum == 1):
            return 1
        total += tempNum
        num_rolls -= 1
    return total
    # END Question 1


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2

    score = roll_dice(num_rolls,dice);
    if(num_rolls == 0):
        if(opponent_score < 10):
            score = 1 + opponent_score
        else:
            num_str = str(opponent_score)
            first = num_str[0]
            second = num_str[1]
            score = 1 + max(int(first),int(second))
    return score
    # END Question 2

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if((score + opponent_score)%7 == 0):
        return four_sided
    else:
        return six_sided

    # END Question 3

def is_swap(score0, score1):
    """Return True if ending a turn with SCORE0 and SCORE1 will result in a
    swap.

    Swaps occur when the last two digits of the first score are the reverse
    of the last two digits of the second score.
    """
    # BEGIN Question 4
    player0 = score0
    player1 = score1
    player0_str = str(score0)
    player1_str = str(score1)
    if(score0 >= 100 or score1 >= 100):
        larger = max(score0, score1)
        smaller = min(score0, score1)
        smallNumStr = str(smaller)
        highNumStr = str(larger)
        if(smaller < 10):
            smallNumStr = '0' + smallNumStr
        if(highNumStr[2] == smallNumStr[0]):
            if(highNumStr[1] == smallNumStr[1]):
                return True
    if(score0 < 10):
        player0_str = '0' + player0_str
    if(score1 < 10):
        player1_str = '0' + player1_str            
    if(player0_str[0] == player1_str[1]):
        if(player0_str[1] == player1_str[0]):
            return True
    return False

    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    while score0 < goal and score1 < goal:
        print("Score0: " + str(score0))
        print("Score1: " + str(score1))
        dice = select_dice(score0,score1)
        if(who == 0):
            score0 += take_turn(strategy0(score0,score1),score1,dice)
            if(is_swap(score0,score1)):
                print("The scores have been switched!")
                score0,score1 = score1, score0
        else:
            score1 += take_turn(strategy1(score0,score1),score0,dice)
            if(is_swap(score0,score1)):
                print("The scores have been switched!")
                score0,score1 = score1, score0

    # END Question 5
    return score0, score1


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

