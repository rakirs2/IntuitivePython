# Understanding Files

The goal of this exercise is to get a bit of understanding of how a lot of commands in a terminal work. This is especially relevant in the days of AI coding where, quite often, the tool just greps over the repository to find a file.

The rules of engagement are pretyt simply. Just use standard python libararies. There will be recursion or iteration. Take your pick.

## Exercise 1: Find a file within a repository.
The executable should look something like 
```
python fileFinder.py path/To/Folder
```
Testing on this could be quite instructive. There should be unit tests for multiple levels of depth. The goal here is to understand how tedious this can get but also how important it can be.

## Exercsie 2: Create a template setup for every location where certain conditinos are met. 

An example of something like this is adding an AGENTS.md or CLAUDE.md for every Git Repo you have. 
The executable should look like
```
python setupRepository.py path/To/Folder
```
