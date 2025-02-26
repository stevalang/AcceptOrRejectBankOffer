### Overview
Predict if the client will subscribe to direct marketing campaign for a banking institution Problem Statement: The data is related to direct marketing campaigns of a Portuguese banking institution. Predict if the client will subscribe to a term deposit based on a marketing campaign-Data Set Download: https://archive.ics.uci.edu/ml/datasets/Bank+Marketing. Data Set Information: The data is related to direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

### Data
I found the dataset on https://archive.ics.uci.edu/ml/datasets/Bank+Marketing.
The variable name, the data type and a brief description of each variable is found in the table below:

![table](https://github.com/stevalang/AcceptOrRejectBankOffer/blob/master/images/dataframe.png)

Dataframe contains:
* 41188 rows (clients)
* 20 columns (information for each client)

### Problem
The data is related to direct marketing campaigns of a Portuguese banking institution. Predict if the client will subscribe to a term deposit based on a marketing campaign
The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be (‘yes’) or not (‘no’) subscribed.

### Goal:
Investigation if the client’s offer for term deposit will be accepted or rejected based on provided information.

### Exploratory Data Analysis
Categorical Variables:
I first start the exploratory analysis of the categorical variables and see what are the categories and are there any missing values for these categories. I created few the bar graphs.

![plot](images/hist_num_cols.png)
![plot](images/age_frequency.png)
![plot](images/age_frequency_.png)

### Hypothesis Testing
**Scientific question:**
Hypothesis testing was conducted to determine whether the clients between age 40-50 are more likely to subscribe for a term deposit based on the marketing campain compare to those in age bracket of 50-60.

**Null Hypothesis:**
There is no difference between the acceptance rate of a term deposit between customers in age group 40-50 compare to those in age group 50-60.

**Alternative Hypothesis:**
There is a significant difference between the acceptance rate of a term deposit between custumers in age group 40-50 compare to those in age group 50-60.

**Alpha level:**
The significance level that will be used for this test is $\alpha = 0.05$.

**Assumptions:**
Each phone call is an independent event.

**Two Samples:**
Clients between 40-50 years old
Clients between 50-60 years old


Test: A two-tailed z-test was chosen, since we are interested in both ends of the distribution.
Alpha: A significance level of  $\alpha =0.05 was chosen for this test, since this is generally standard and the outcome of this hypothesis testing is not.


### Conclusion

*Difference in sample proportions: -0.00214

*p-value for accepting term deposit frequency comparison: 0.70

*Welch Test Statistic: -0.52

*Degrees of Freedom for Welch's Test: 18005.67


For this hypothesis test we have pvalue=0.70 which is above our $\alpha =0.05 so I fail to reject the null hypothesis, which means that there isn't a statistically significant difference between the two age groups.


## Technologies Used
* Numpy
* Pandas
* Matplotlib
* Seaborn

### Next Steps
Create classification model to predict if the client will subscribe (yes/no) a term deposit.

### Citations
This dataset is public available for research. The details are described in [Moro et al., 2011].
  Please include this citation if you plan to use this database:

  [Moro et al., 2011] S. Moro, R. Laureano and P. Cortez. Using Data Mining for Bank Direct Marketing: An Application of the CRISP-DM Methodology.
  In P. Novais et al. (Eds.), Proceedings of the European Simulation and Modelling Conference - ESM'2011, pp. 117-121, Guimarães, Portugal, October, 2011. EUROSIS.

  Available at: [pdf] http://hdl.handle.net/1822/14838
                [bib] http://www3.dsi.uminho.pt/pcortez/bib/2011-esm-1.txt
