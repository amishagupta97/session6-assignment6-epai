# Assignment 6 Submission

Well this assignment made me learn Poker Game! Though I am not very sure of how poker is played and references which I found usually had poker game defined for a set of 5 cards,
I have modifies same rules for a set of 3 or 4 cards as well. So here's my definition of Poker Game :

### Royal Flush : 
A, K, Q, J, 10, all the same suit for 5 cards.
A, K, Q, J, all the same suit for 4 cards.
A, K, Q, all the same suit for 3 cards.

### Straight flush :
Cards in a sequence, all in the same suit.

### Four Of A Kind:
Four cards of the same rank.
This is not applicable to set of 3 cards.

### Full house :
Three of a kind with a pair.
This is not applicable to set of 3 or 4 cards.

### Flush :
Any cards of the same suit, but not in a sequence.

### Straight :
Cards in a sequence, but not of the same suit.

### Three Of A Kind :
Three cards of the same rank.

### Two Pair :
Two different pairs.
This is not applicable to set of 3 cards.

### One Pair :
Two cards of the same rank.

### High Card :
When you haven’t made any of the hands above, the highest card from both set is compared.

### deck_cards_using_single_expression :
function creates 52 cards in a deck with the help of lambda, zip and map functions

### deck_cards_using_normal_function :
function creates 52 cards in a deck with the normal function without using lambda, zip and map functions

### play_poker_game :
function evaluates which player has won poker game

### setValues :
stores number rank for each value of a card

### isRoyalFlush() :
checks if it a royal flush

### isStraightFlush() :
checks if it is a striaght flush

### isFourOfAKind():
checks if it is has four of a kind

### isFullHouse():
checks if it is a full house

### isFlush():
checks if it is a flush

### isStraight():
checks if it is a straight

### isThreeOfAKind():
checks if it has three of a kind

### isTwoPair()
checks if it has two pairs

### isOnePair()
checks if it has one pair

### check_hand_score()
checks which hand is applicable and returns score for that hand

## Test Cases Explanation

### test_readme_exists 
Checks if readme file exists.

### test_readme_contents
Checks if readme file has atleast 500 words.

### test_readme_proper_description
Checks if all functions implemented have been defined in readme

### test_readme_file_for_formatting
Checks if file is formatted properly using "#"

### test_indentations
Checks if four spaces multiple only have been used throughout the code

### test_function_name_had_cap_letter
Checks if no function name starts with capital letter

### test_all_functions_implemented
Checks if all functions have been implemented in code

### test_map_used / test_lambda_used / test_zip_used 
tests if map, lambda and zip have been used or not

### test_deck_cards_using_single_expression_docstring / test_deck_cards_using_normal_function_docstring / test_play_poker_game_docstring
checks if docstring is impl in this function

### test_deck_cards_using_single_expression_docstring_content / test_deck_cards_using_normal_function_docstring_content
checks if docstring length is more than 50

### test_deck_cards_using_single_expression_total_cards / test_deck_cards_using_normal_function_total_cards
checks if length of all combinations created is 52

### test_deck_cards_using_single_expression_compare_cards / test_deck_cards_using_normal_function_compare_cards
checks if all 52 combinations have been created

### test_deck_cards_using_single_expression_invalid_input / test_deck_cards_using_normal_function_invalid_input
checks if this function gives error fr giving input to function which doesnt require input

### test_play_poker_game_invalid_length_input
checks if invalid set of cards other than 3, 4 or 5 have been given as input

### test_play_poker_game_length_mismatch
both set of cards given as input doesnt match length

### test_play_poker_game_Royal_Flush / test_play_poker_game_Royal_Flush_4cards / test_play_poker_game_Royal_Flush_3cards
Checks if Royal Flush is identified by game for set of 5, 4, 3 cards

### test_play_poker_game_Straight_Flush / test_play_poker_game_Straight_Flush_4cards / test_play_poker_game_Straight_Flush_3cards
Checks if Straight Flush is identified by game for set of 5, 4, 3 cards

### test_play_poker_game_Four_Of_A_Kind / test_play_poker_game_Four_Of_A_Kind_4cards
Checks if Four of a Kind is indentified by game for set of 5, 4 cards

### test_play_poker_game_Full_House
Checks if Full House is identified by game for set of 5 cards

### test_play_poker_game_Flush / test_play_poker_game_Flush_4cards / test_play_poker_game_Flush_3cards
Checks if Flush is identified by game for a set of 5, 4, 3 cards

### test_play_poker_game_Straight / test_play_poker_game_Straight_4cards / test_play_poker_game_Straight_3cards
Checks if Straight is identified by game for a set of 5, 4, 3 cards

### test_play_poker_game_Three_Of_A_Kind / test_play_poker_game_Three_Of_A_Kind_4cards / test_play_poker_game_Three_Of_A_Kind_3cards
Checks if Three of a kind is identified by game for a set of 5, 4, 3 cards

### test_play_poker_game_Two_Pair / test_play_poker_game_Two_Pair_4cards
Checks if two pairs is identified by game for a set of 5, 4 cards

### test_play_poker_game_One_Pair / test_play_poker_game_One_Pair_4cards / test_play_poker_game_One_Pair_3cards
Checks if One pair is identified by game for a set of 5, 4, 3 cards

### test_play_poker_game_High_Card / test_play_poker_game_High_Card_4cards / test_play_poker_game_High_Card_3cards
Checks if High Card is identified by game for a set of 5, 4, 3 cards

### test_play_poker_game_Draw
Checks if both players have a draw in case both have same high card and no hand



