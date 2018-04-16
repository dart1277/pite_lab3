[![Build Status](https://travis-ci.org/phpl/pite_lab3.svg?branch=master)](https://travis-ci.org/phpl/pite_lab3)
[![Coverage Status](https://coveralls.io/repos/github/phpl/pite_lab3/badge.svg?branch=master)](https://coveralls.io/github/phpl/pite_lab3?branch=master)
## Games - Client/Server Edition
This application can be easily ported to be run as a web service on Apache server and regular web browser JavaScript client.
Games implemented:
* TicTacToe
* Intervals
### TicTacToe
Simple implementation of game using sockets. Game uses 3x3 grid to play and fields are numerated 0-8. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
### Intervals
Simple implementation of Intervals game. Player has to guess number in 0-100 range. After writing number player gets a hint if word is lower or higher than secret number. Player can also see his previous guesses.
## Usage
1. Run OXServer.py
2. Run game.py
3. Select game:
* 0 - TicTacToe
* 1 - Intervals
4. Write players nicknames
5. Have fun!
