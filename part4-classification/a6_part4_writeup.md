# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
 The model only has an accuracy of .57, likely because the data is no longer scaled which causes there to be many outliers that mess up the data.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
The model is very accurate with the StandardScaler. It is also accurate for the given use case based on it showing high correlation.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model was very accurate, however, just the repetition of one or more zeros many times in a row caused the model to make mistakes.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

No