# My Art Cave App

This is work in progress. Currently only a skeleton of the code is written and some basic functionalities.

The purpose of this App is to improve and enhance a person's interaction with Art. It aims at enabling two main capabilities:
1. Allow the user to learn more about and track the art works that he/she encounters over time and allow to answer questions like:
- Which art works have I seen in which galleries? 
- Where can I see more work of an artist?
- How do the works that I've seen/liked relate to each other (e.g. based on art period, art school)?
- Which artists/art movements have I seen most often?
They will also be able to give inputs about how they feel about the art works (e.g. inspiration, loneliness, connection).
Furthermore the users will be able to share and connect with friends.

2. Allow the users to enhance their art experience through Machine Learning, e.g. by using the following functionalities:
- Generate a poem from an image (ref. https://github.com/researchmm/img2poem)
- Classify an art work to an art movement 

## Technologies

The App is written in Python using the library Kivy. Based on the input for an artist name, it queries the API of WikiArt to retrieve artist details. This details are then stored in a DB.


### Installing
Clone the GitHub and run 
```
pipenv install
```



## Authors

* **Simona Doneva** - *Initial work* 

