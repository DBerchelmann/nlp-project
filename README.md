<h1> Individual Project - Employee Classification </h1>

Hi there,

Welcome to the README file for my individual project covering <b>classification of gender based on 2016 San Antonio City Employee Compensation</b>

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



-------------

<h3><u>Data Dictionary</u></h3>
    
-  Please use this data dictionary as a reference for the variables used within in the data set.



|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
|  repo |Object    | name of the github repository   |
|   language  | Object |dominant programming language that makes up the repository |
|  readme_contents  | Object |text that makes up the README file |






-------------------
 <h3><u>Hypothesis and Questions</u></h3>




--------------------
 <h3><u>How To Recreate This Project</u></h3>
 
 To recreate this project you will need use the following files:
 
 - acquire.py
 - prepare.py
 - explore.py
 - model.py 
 
 Your target variable will be langue which is defined in the above data dictionary. Please visit my final notebook to see this variable being used.
 
 <b>Step 0.</b> Clone this repo to your local machine with the above files.
 
 <b>Step 1.</b> Import all necessary libraries to run functions. These can be found in each corresponding .py file
 
 <b>Step 2.</b> Use pd.read to bring in the csv file from your local folder. 
 
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



<b>Recommendations & next steps</b>:


-----