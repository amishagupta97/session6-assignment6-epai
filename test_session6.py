import pytest
import random
import string
import session6
import os
import inspect
import re
import math
import decimal
from decimal import Decimal
import cmath

Deck_Cards = [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), 
              ('3', 'spades'), ('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), 
              ('4', 'spades'), ('4', 'clubs'), ('4', 'hearts'), ('4', 'diamonds'), 
              ('5', 'spades'), ('5', 'clubs'), ('5', 'hearts'), ('5', 'diamonds'), 
              ('6', 'spades'), ('6', 'clubs'), ('6', 'hearts'), ('6', 'diamonds'), 
              ('7', 'spades'), ('7', 'clubs'), ('7', 'hearts'), ('7', 'diamonds'), 
              ('8', 'spades'), ('8', 'clubs'), ('8', 'hearts'), ('8', 'diamonds'), 
              ('9', 'spades'), ('9', 'clubs'), ('9', 'hearts'), ('9', 'diamonds'), 
              ('10', 'spades'), ('10', 'clubs'), ('10', 'hearts'), ('10', 'diamonds'), 
              ('jack', 'spades'), ('jack', 'clubs'), ('jack', 'hearts'), ('jack', 'diamonds'),
              ('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'),
              ('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'), 
              ('ace', 'spades'), ('ace', 'clubs'), ('ace', 'hearts'), ('ace', 'diamonds')]


README_CONTENT_CHECK_FOR = [
    'deck_cards_using_single_expression',
    'deck_cards_using_normal_function',
    'Poker Game',
    'Royal Flush',
    'Straight Flush',
    'Four Of A Kind',
    'Full House',
    'Flush',
    'Straight',
    'Three Of A Kind',
    'Two Pair',
    'One Pair',
    'High Card'
]

CHECK_FOR_FUNCT_IMPL = [
  'deck_cards_using_single_expression',
  'deck_cards_using_normal_function',
  'play_poker_game'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_all_functions_implemented():
    code_lines = inspect.getsource(session6)
    FUNCS_IMPL = True
    for c in CHECK_FOR_FUNCT_IMPL:
        if c not in code_lines:
            print(c)
            FUNCS_IMPL = False
            pass
    assert FUNCS_IMPL == True, 'You forgot to implement all functions! Try again!'

def test_map_used():
    code_lines = inspect.getsource(session6)
    assert 'map' in code_lines, 'Map is not used!'

def test_lambda_used():
    code_lines = inspect.getsource(session6)
    assert 'lambda' in code_lines, 'Lambda is not used!'

def test_zip_used():
    code_lines = inspect.getsource(session6)
    assert 'zip' in code_lines, 'Zip is not used!'

def test_deck_cards_using_single_expression_docstring():
    docstring = session6.deck_cards_using_single_expression.__doc__
    assert docstring

def test_deck_cards_using_single_expression_docstring_content():
    docstring = session6.deck_cards_using_single_expression.__doc__
    assert len(docstring)>50

def test_deck_cards_using_single_expression_total_cards():
    result = session6.deck_cards_using_single_expression()
    assert len(result) == 52

def test_deck_cards_using_single_expression_compare_cards():
    result = session6.deck_cards_using_single_expression()
    for card in Deck_Cards:
        if card not in result:
            assert False

def test_deck_cards_using_single_expression_invalid_input():
    with pytest.raises(TypeError):
        session6.deck_cards_using_single_expression(2,3,5)

def test_deck_cards_using_normal_function_docstring():
    docstring = session6.deck_cards_using_normal_function.__doc__
    assert docstring

def test_deck_cards_using_normal_function_docstring_content():
    docstring = session6.deck_cards_using_normal_function.__doc__
    assert len(docstring)>50

def test_deck_cards_using_normal_function_total_cards():
    result = session6.deck_cards_using_normal_function()
    assert len(result) == 52

def test_deck_cards_using_normal_function_compare_cards():
    result = session6.deck_cards_using_normal_function()
    for card in Deck_Cards:
        if card not in result:
            assert False

def test_deck_cards_using_normal_function_invalid_input():
    with pytest.raises(TypeError):
        session6.deck_cards_using_normal_function(2,3,5)

def test_play_poker_game_docstring():
    docstring = session6.play_poker_game.__doc__
    assert len(docstring)>50

def test_play_poker_game_invalid_length_input():
    Card1 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades'), ('2', 'diamonds')]
    Card2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs'), ('2', 'diamonds')]
    with pytest.raises(ValueError):
        session6.play_poker_game(Card1, Card2)
    
def test_play_poker_game_length_mismatch():
    Card1 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    Card2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs')]
    with pytest.raises(ValueError):
        session6.play_poker_game(Card1, Card2)

def test_play_poker_game_Royal_Flush():
    Card1 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    Card2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Royal Flush"

def test_play_poker_game_Straight_Flush():
    Card1 = [('ace', 'clubs'), ('king', 'clubs'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    Card2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a Straight Flush"
    
def test_play_poker_game_Four_Of_A_Kind():
    Card1 = [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), ('3', 'spades')]
    Card2 = [('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('2', 'spades'), ('2', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Four Of A Kind"

def test_play_poker_game_Full_House():
    Card1 = [('2', 'spades'), ('3', 'clubs'), ('7', 'hearts'), ('8', 'diamonds'), ('3', 'spades')]
    Card2 = [('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('2', 'spades'), ('2', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a Full House"

def test_play_poker_game_Flush():
    Card1 = [('2', 'spades'), ('3', 'spades'), ('7', 'spades'), ('8', 'spades'), ('3', 'spades')]
    Card2 = [('3', 'clubs'), ('4', 'hearts'), ('8', 'diamonds'), ('9', 'spades'), ('2', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Flush"

def test_play_poker_game_Straight():
    Card1 = [('2', 'spades'), ('3', 'hearts'), ('7', 'diamonds'), ('8', 'hearts'), ('3', 'spades')]
    Card2 = [('3', 'clubs'), ('4', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('7', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a Straight"

def test_play_poker_game_Three_Of_A_Kind():
    Card1 = [('2', 'spades'), ('2', 'hearts'), ('2', 'diamonds'), ('8', 'hearts'), ('3', 'spades')]
    Card2 = [('3', 'clubs'), ('8', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('7', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Three Of A Kind"

def test_play_poker_game_Two_Pair():
    Card1 = [('2', 'spades'), ('4', 'hearts'), ('2', 'diamonds'), ('8', 'hearts'), ('4', 'spades')]
    Card2 = [('3', 'clubs'), ('8', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('7', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Two Pair"

def test_play_poker_game_One_Pair():
    Card1 = [('2', 'spades'), ('4', 'hearts'), ('2', 'diamonds'), ('8', 'hearts'), ('7', 'spades')]
    Card2 = [('3', 'clubs'), ('8', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('7', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a One Pair"

def test_play_poker_game_High_Card():
    Card1 = [('2', 'spades'), ('4', 'hearts'), ('3', 'diamonds'), ('8', 'hearts'), ('7', 'spades')]
    Card2 = [('3', 'clubs'), ('10', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('7', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a High Card"

# Testing for set of 4 cards

def test_play_poker_game_Royal_Flush_4cards():
    Card1 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
    Card2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Royal Flush"

def test_play_poker_game_Straight_Flush_4cards():
    Card1 = [('ace', 'clubs'), ('king', 'clubs'), ('queen', 'spades'), ('jack', 'spades')]
    Card2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a Straight Flush"
    
def test_play_poker_game_Four_Of_A_Kind_4cards():
    Card1 = [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds')]
    Card2 = [('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('2', 'spades')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Four Of A Kind"

# Full House not applicable to set of 4 cards

def test_play_poker_game_Flush_4cards():
    Card1 = [('2', 'spades'), ('3', 'spades'), ('7', 'spades'), ('8', 'spades')]
    Card2 = [('3', 'clubs'), ('4', 'hearts'), ('8', 'diamonds'), ('9', 'spades')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Flush"

def test_play_poker_game_Straight_4cards():
    Card1 = [('2', 'spades'), ('3', 'hearts'), ('7', 'diamonds'), ('8', 'hearts')]
    Card2 = [('3', 'clubs'), ('4', 'hearts'), ('5', 'diamonds'), ('6', 'spades')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a Straight"

def test_play_poker_game_Three_Of_A_Kind_4cards():
    Card1 = [('2', 'spades'), ('2', 'hearts'), ('2', 'diamonds'), ('8', 'hearts')]
    Card2 = [('3', 'clubs'), ('8', 'hearts'), ('5', 'diamonds'), ('6', 'spades')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Three Of A Kind"

def test_play_poker_game_Two_Pair_4cards():
    Card1 = [('2', 'spades'), ('4', 'hearts'), ('2', 'diamonds'), ('4', 'spades')]
    Card2 = [('3', 'clubs'), ('8', 'hearts'), ('5', 'diamonds'), ('6', 'spades')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Two Pair"

def test_play_poker_game_One_Pair_4cards():
    Card1 = [('2', 'spades'), ('4', 'hearts'), ('2', 'diamonds'), ('8', 'hearts')]
    Card2 = [('3', 'clubs'), ('8', 'hearts'), ('5', 'diamonds'), ('6', 'spades')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a One Pair"

def test_play_poker_game_High_Card_4cards():
    Card1 = [('2', 'spades'), ('4', 'hearts'), ('3', 'diamonds'), ('8', 'hearts')]
    Card2 = [('3', 'clubs'), ('10', 'hearts'), ('5', 'diamonds'), ('6', 'spades')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a High Card"


# Testing for set of 3 cards

def test_play_poker_game_Royal_Flush_3cards():
    Card1 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades')]
    Card2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Royal Flush"

def test_play_poker_game_Straight_Flush_3cards():
    Card1 = [('ace', 'clubs'), ('king', 'clubs'), ('queen', 'spades')]
    Card2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a Straight Flush"
    
# Four Of A Kind not applicable to set of 3 cards

# Full House not applicable to set of 3 cards

def test_play_poker_game_Flush_3cards():
    Card1 = [('2', 'spades'), ('3', 'spades'), ('7', 'spades')]
    Card2 = [('3', 'clubs'), ('4', 'hearts'), ('8', 'diamonds')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Flush"

def test_play_poker_game_Straight_3cards():
    Card1 = [('2', 'spades'), ('3', 'hearts'), ('7', 'diamonds')]
    Card2 = [('3', 'clubs'), ('4', 'hearts'), ('5', 'diamonds')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a Straight"

def test_play_poker_game_Three_Of_A_Kind_3cards():
    Card1 = [('2', 'spades'), ('2', 'hearts'), ('2', 'diamonds')]
    Card2 = [('3', 'clubs'), ('8', 'hearts'), ('5', 'diamonds')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Three Of A Kind"

# Two Pair not applicable to set of 3 cards

def test_play_poker_game_One_Pair_3cards():
    Card1 = [('2', 'spades'), ('4', 'hearts'), ('2', 'diamonds')]
    Card2 = [('3', 'clubs'), ('8', 'hearts'), ('5', 'diamonds')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a One Pair"

def test_play_poker_game_High_Card_3cards():
    Card1 = [('2', 'spades'), ('4', 'hearts'), ('7', 'diamonds')]
    Card2 = [('3', 'clubs'), ('10', 'hearts'), ('5', 'diamonds')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a High Card"

def test_play_poker_game_Draw():
    Card1 = [('2', 'spades'), ('4', 'hearts'), ('10', 'diamonds')]
    Card2 = [('3', 'clubs'), ('10', 'hearts'), ('5', 'diamonds')]
    result = session6.play_poker_game(Card1, Card2)
    assert result == "Again it's a draw! Both players have same High Card"





