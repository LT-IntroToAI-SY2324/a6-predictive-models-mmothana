# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?

The accuracy is .6 and this is most likely because the data is not standerdized anymore so the model has harder time dealing with the data.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.

The accuracy of the model now is .86. I think it is accurate enough for the given use case because the r-sqaured is cloes to one and there are only two outcomes.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

The model would be correct 5 times out of 6 at a time. So the pattern was that it would in incorrect once every 5-6 tries.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

No, a 34 year old female who makes 56000 a year would not buy an SUV.

