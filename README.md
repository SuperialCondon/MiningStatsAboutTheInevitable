PROJECT: Mining Stats About The Inevitable

AUTHORS:
Derek Gorthy 
Michael Condon 
Bryce Melvin 


DESCRIPTION:
The purpose of this project is to data mine the 2014 data set for deaths from the Center of Disease Control and Prevention. The first section of this project focused on reproducing the conclusions found by the CDC and other major secondary organizations. The second section of this project is adding data from outside sources. Research of death trends is only focused on temporal relationships; this project is focused on identifying trends in the CDC's dataset and other factors.


QUESTIONS:
Can we reproduce the findings of the CDC and other primary sources?

  This question was capable of being answered after pre-processing the data in order to ride of unecessary data to speed up the process. After finishing pre-processing, we developed scripts in order to calculate the same findings that CDC had listed in their 2014 death set report. We were able to produce results, establishing a basis for further research.

Can we replicate the results of studies conducted by secondary analysts?

  Other analysts would discover findings in regards to suicide rate for males compared to females. We developed additional scripts that calculate Bayesian values. We were able to replicate the conclusions of secondary analysts; we focused on suicide research as this is the most readily available. It was essential that we were capable of replicating findings from both the main and secondary analysts in order to proceed with any other further questions.

Can we provide evidence for our unconventional cause of death assumptions?

  This was the most open-ended question that we posed. There is no basis for confirming our findings, so our discretion concerning the validity of our findings is most important. Because we had to estimate the date of each death, sensativity analysis is essential to confirming any conclusion that we found. Two of the major findings are explained below.

  	Positive relationship between sun spot number and number of natural deaths: Determined by running the simple counting script after removing the outliers in the sun spot set. The variation in this set means that the positive relationship would likely not be reflected in other CDC sets.

  	Higher chance on suicide given the presence of a full moon: Initially, we found that there was nearly a 10% higher chance of a suicide given that there is a full moon. This was calculated using our Bayesian calculation script. When running sensitivity analysis, we found that this 10% difference was likely attributed to chance.


APPLICATION:
We found additional interesting results in the conventional analysis (explained in the video below). The generalized conclusion that we drew from this was that additional conclusions can be draw from commonly-studied datasets. 

Additionally, the importance of determining a missing attribute's distribution is very important. Once a distribution is determined, understanding how to perform sensitivity analysis shows how accurate a statistic is. This was essential in our project, because each unconventional test was based off the underlying assumption that the dates were estimated accurately.

Finally, our project shows the importance of thinking outside the box when it comes to looking for the impact of an unconventional attribute on another. In our case, we were able to disprove, at least of 2014, that a factor like the S&P 500 performance influences the number of suicides in a day. 


VIDEO OF RESULTS DESCRIPTION:
** Note: this is in the .swf file format, check for program compatibility **
https://github.com/SuperialCondon/MiningStatsAboutTheInevitable/blob/master/4_CorrelationsInCauseofDeath_Part5.swf


FORMAL RESEARCH PAPER:
https://github.com/SuperialCondon/MiningStatsAboutTheInevitable/blob/master/4_CorrelationsInCauseofDeath_Part4.pdf
