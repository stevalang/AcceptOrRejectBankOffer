### Destiption:
Predict if the client will subscribe to direct marketing campaign for a banking institution Problem Statement: The data is related to direct marketing campaigns of a Portuguese banking institution. Predict if the client will subscribe to a term deposit based on a marketing campaign-Data Set Download: https://archive.ics.uci.edu/ml/datasets/Bank+Marketing. Data Set Information: The data is related to direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed. There are four datasets: 1. bank-additional-full.csv with all examples (41188) and 20 inputs, ordered by date (from May 2008 to November 2010), very close to the data analyzed in [Moro et al., 2014] 2. bank-additional.csv with 10% of the examples (4119), randomly selected from 1), and 20 inputs. 3. bank-full.csv with all examples and 17 inputs, ordered by date (older version of this dataset with fewer inputs). 4. bank.csv with 10% of the examples and 17 inputs, randomly selected from 3 (older version of this dataset with fewer inputs). The smallest datasets are provided to test more computationally demanding machine learning algorithms Goal:- The classification goal is to predict if the client will subscribe (yes/no) a term deposit (variable y).

### Overview
Investigation if the client’s offer for term deposit will be accepted or rejected based on provided information.

### Data
I found the dataset on https://archive.ics.uci.edu/ml/datasets/Bank+Marketing. (from May 2008 to November 2010)
The variable name, the data type and a brief description of each variable is found in the table below:


### Problem

The data is related to direct marketing campaigns of a Portuguese banking institution. Predict if the client will subscribe to a term deposit based on a marketing campaign
The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be (‘yes’) or not (‘no’) subscribed.

Dataframe contains:
* 41188 rows (clients)
* 20 columns (information for each client)


### Goal:
The classification goal is to predict if the client will subscribe (yes/no) a term deposit.

### Exploratory Data Analysis

Categorical Variables:
I first start the exploratory analysis of the categorical variables and see what are the categories and are there any missing values for these categories. I created few the bar graphs.

![plot](https://github.com/stevalang/AcceptOrRejectBankOffer/blob/master/images/age_frequency.png)
![plot](/Users/stevalang/Galvanize/0002_capstones/capstone1/accept_reject_bank_offer/images/age_frequency.png)




## Hypothesis Testing
Hypothesis testing was conducted to determine whether the clients between age 40-50 are more likely to subscribe for a term deposit based on the marketing campain compare to those in age bracket of 50-60.

Null Hypothesis: There is no difference between clients in age group 40-50 and those in 50-60 for subscribing a term deposit.

Alternative Hypothesis: There is a significant difference between the acceptance rate of a term deposit between custumers in age group 40-50 compare to those in age group 50-60.

Assumptions:
Each phone call is an independent event.

Two Samples:
Clients between 40-50 years old
Clients between 50-60 years old


Test: A two-tailed Welch's t-test was chosen, since we are interested in both ends of the distribution.
Alpha: A significance level of 0.05 was chosen for this test, since this is generally standard and the outcome of this hypothesis testing is not.


For this hypothesis test:
Degrees of Freedom for Welch's Test: 5258.58
p-value: 0.9890



## Technologies Used
* Numpy
* Pandas
* Matplotlib
* Seaborn

### Conclusion
### Next Steps

### Citations
This dataset is public available for research. The details are described in [Moro et al., 2011].
  Please include this citation if you plan to use this database:

  [Moro et al., 2011] S. Moro, R. Laureano and P. Cortez. Using Data Mining for Bank Direct Marketing: An Application of the CRISP-DM Methodology.
  In P. Novais et al. (Eds.), Proceedings of the European Simulation and Modelling Conference - ESM'2011, pp. 117-121, Guimarães, Portugal, October, 2011. EUROSIS.

  Available at: [pdf] http://hdl.handle.net/1822/14838
                [bib] http://www3.dsi.uminho.pt/pcortez/bib/2011-esm-1.txt
