<h1> NLP Project - Predicting Repository Languages </h1>

Hi there,

Welcome to the README file for my NLP project covering <b>the prediction of programming language of github repositories based on README files.</b>

In here, you will find expanded information on this project including goals, how I will be working through the pipeline and a data dictionary to help offer more insight to the variables that are being used.



-------------------
<h3><u>The Goal</u></h3>

<font color = blue>**Why are we here?**</font>

* <font color = red>Problem:</font> <i>Can a repository's programming language be determined by a model built off of natural language processing?o</i>

* <font color = red>Goal:</font> <i>Create a predictive model using natural language processing that can determine the dominant programming language used in github repositories based on the text of the README files.</i>


-------------------
<h3><u>Where Is Our Data Coming From?</u></h3>

* This data is has been pulled from git hub repository's focusing on Formula 1.
 

* The data set can be accessed via .csv, which is located within this repository.

------------------
<H3><u> Project Planning </u></H3>

- Plan project out
    - Thurs-Friday (planning/acquiring/cleaning)
    - Saturday-Monday afternoon (exploring/modeling/finalnotebook)
    - Monday afternoon/evening (Complete slide presentation/Practice presentation 3 times, with 2 recordings)

Other to-dos

- Determine Git Hub Search Parameter
- Create acquire function to acquire data
- Create functions to clean the data
- Create unique word clouds



-------------

<h3><u>Data Dictionary</u></h3>
    
-  Please use this data dictionary as a reference for the variables used within in the data set.



|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
|  repo |Object    | name of the github repository   |
|   language  | Object |dominant programming language that makes up the repository |
|  readme_contents  | Object |text that makes up the README file |
|  written_language  | Object |native language that README was written in |
|  readme_length  | Int64 |total length of words of README|





-------------------
 <h3><u>Hypothesis and Questions</u></h3>

- Do README's in other languages affect the accuracy of the model?

- What are the median lengths of README's based on programming languages?

- Do certain programming languages have noticible unique words that are only common to their specific language?


--------------------
 <h3><u>How To Recreate This Project</u></h3>
 
 To recreate this project you will need use the following files:
 
 - acquire.py
 - wrangle.py
 - explore.py
 - model.py 
 
 Your target variable will be langue which is defined in the above data dictionary. Please visit my final notebook to see this variable being used.
 
 <b>Step 0.</b> Clone this repo to your local machine with the above files.
 
 <b>Step 1.</b> Import all necessary libraries to run functions. These can be found in each corresponding .py file
 
 <b>Step 2.</b> Use pd.read to bring in the csv file from your local folder. Use the f1_readmes.csv file located in this repository 
 
 <b>Step 3.</b> To see the the cleaned data set before training do the following:
 
`

After you have gotten to know the data set, run the following to gather the train, validate, test data


    
 
 <b>Step 4.</b> Verify that your data has been prepped using df.head()
 
 <b>Step 5.</b>. Explore
 
 <b>Step 6.</b> Evaluate and model the data using different regression algorithms. 
         
         
 ```
 { 
 from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz
from graphviz import Graph
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
 }
 ```
 
<b>Step 7.</b> After you have found a model that works, test that model against out of sample data using the function in my notebook.
 
 For a more detailed look, please visit my final notebook for employee classification for further assistance.
 
--------------------



<h3>Key Takeaways, Recommendations, & Next Steps</h3>


Through this classification project I came away with the following <b> key takeways</b>:

- The higher the number of repositories with a certain language, the better the model is at predicting it
     - We saw this with the high accuracies for our top 3 languages by value_counts (JavaScript, Python, HTML)
- JS, Python, & HTML also each had repositories in different languages so it's hard to make an argument that language played a factor as those language specific stopwords were accounted for in the cleaning of the data
- I thought having repositories in different langauages would affect the accuracy but as it turns out, that didn't seem to be an issue as the top 3 languages (JS, Python, HTML) all had repositories in multiple languages.

<b>Recommendations & next steps</b>:

- More repositories will increase the sample size and will allow for greater accuracy
- Going with repositories that focused on Formula 1 was off the main path and it lead to issues with not only empty repositories but poorly constructed README files as well.
- Going forward, this model could be improved further by limiting the number of languages to a top 5 


-----
