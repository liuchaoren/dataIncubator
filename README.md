# dataIncubator

In the following, we select all restaurants in Pittsburgh and group the restaurants by food styles, like "American food", "Chinese food", "Mexican food", etc. 
We want to know the popularity of each kinds of food, which is obtained by the average number of reviews on each kind of food. 
Here we assume that the more popular the food is, the more review it receives. 
The average rating (0-5) of a kind of food is an indicator of customer satisfaction level. 5 stars mean customers are very satisfied and 0 star means customers are not satisfied at all. 
When starting a new restaurant, we need to decide what kinds of food is on-high demanding while current restaurants fail to satisfy customers. 
In the next, we plot the ratio between popularity and rating as a function of food styles. We can find that the Belgian food, German food, and Spanish food have high 
popularity/rating ratio. These results tell that it is probably wise to investigate Belgian food, German food, or Spanish food. The plot is shown below. 
![alt text](https://github.com/liuchaoren/dataIncubator/blob/master/byreviewnum.png "investigation interest 1")

The number of reviews is not the best indicator for popularity. A better indicator is the number of reviews plus the number of vote on the reviews. The votes can
find the review be "useful", "funny", or "cool". 
To improve the model, we redefine the popularity as the number of reviews plus the number of votes on the reviews. 
An updated result is shown as below. 
![alt text](https://github.com/liuchaoren/dataIncubator/blob/master/byvote.png "investigation interest 2")


