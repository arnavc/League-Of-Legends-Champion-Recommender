# League of Legends Champion Recommender 

Capstone Project for Galvanize Data Science Immersive Program

# Introduction

League of Legends is the most played online PC videogame in the world with over 100 million players monthly according to [Forbes](https://www.forbes.com/sites/insertcoin/2016/09/13/riot-games-reveals-league-of-legends-has-100-million-monthly-players/#1ad9ebb65aa8). The game is designed to be a Multiplayer Online Battle Arena (MOBA) which pits a team of five players versus another team of five players. Each player is able to control one champion of their choice throughout the entirety of the game and the goal is to destroy the other team's base. The game currently has 138 playable champions with many more planned for release. On average, a player never gets to master more than 20-30 champions despite playing the game for years and years. 

With so many potential champions to choose from, a problem that plagues novice and veteran players is: which champion that I haven't tried would I have fun playing? The goal of this project is to create a recommender system that can address said struggle by recommending champions that the user will enjoy. A system like this is valuable to the player because since champions take so long to master, players will find more value in recommendations that have a personalized bias for their playing tendencies. 

A recommendation system also holds an inherent business value for Riot Games. Given that League of Legends is a free-to-play game, users are able to play all champions at a zero dollar cost. However, Riot allows players to buy different customizations for a champion and alter the champion's appearance. With this microtransaction model in mind, it is extremely beneficial to introduce players champions that they can get hooked to because hand in hand with this is the higher possibility of them investing to customize their champion. Establishing a player connection to the identity of a champion is crucial to Riot's business model and improving this is one of the aims of my project.

- - - - - -  IMAGE - - - - - - 

# The Data

The data set I worked with was provided on [Kaggle](https://www.kaggle.com/xenogearcap/league2016). Values in this dataset had been aggregated using Riot's API and included information on 130,000 summoner ids and a list of all the champions the players associated with those ids had played over the 2016 ranked season. This data was initially presented in an unorganized manner. 

In order to proceed with building a recommender system, I needed my data in a specific format. Pre-processing involved counting how many times a user had played each champion and then transferring that into a new matrix. This proved to be surprisingly difficult to do in an algorithmically efficient manner and actually being able to do it took a few days. I reformatted my data to have SummonerIDs as rows and all the 135 champions they could potentially have played as columns. I termed this to be my utility frequency matrix and as you can observe below, it was sparse as most users had not interacted with most champions. 

- - - - - - IMAGE OF DATA TABLE - - - - - -

# Method

Building a recommender system usually involves one of the following approaches: Collaborative Filtering, Content-Based Filtering, or a Hybrid Recommendation System. Collaborative Filtering is a technique that relies on a massive data set w
