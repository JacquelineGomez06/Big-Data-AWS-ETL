# Big-Data-AWS-ETL
An analysis of US Data job trends focused on standard salaries, remote vs non-remote, location, and companies.

Tools Used:
+ sqlalchemy
+ pandas
+ matplotlib
+ seaborn
+ sklearn

## Methodology

Connnect to AWS,query,save as pandas data frames

![extract](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/extract.png)

Join all 3 tables and save new data as csv

![join](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/join.png)

After some data cleaning, categorical data from the description_tokens columns was transformed into numerical data. Each of the skills listed were turned into columns with sklearn one-hot encoding.

![join](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/transform.png)

Data is now ready for visualizations and statistical testing

## Visuals

General standardized data salary shows right skewed data, with the peak between 90-100k

![salary](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/salary.png)

Non-remote jobs have a slightly higher median of around 90k as opposed to remote job salary  median of 80k

![remotevnon](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/remote%20vs%20nonremote.png)

In the top 5 skills are SQL, Tableau, Excel, Python, and Power BI
SQL has a significant presence surpassing the 1000 count

![skills](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/topskills.png)

So jobs are asking for SQL knowledge but does that mean more money?
The plots below show that jobs requiring SQL do indeed pay more than jobs that dont require SQL by at least $5,000

![sql](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/sql.png)

The medians for jobs not requiring and reuiring Tableau are really close to one another but having Tableau as a skill has a slightly higher salary

![tableau](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/acf91c1073967df106e1fc3e2725ea734e0ffb68/images/tableau.png)

As for Python,jobs requiring it as a skill pays more than jobs that dont require Python by at least $10,000. In all the instances requiring a data skill, on average, the salaries are higher.

![python](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/python.png)

In the top 3 paying companies we have Upwork, Cox Communications, and Edward Jones.

![topco](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/acf91c1073967df106e1fc3e2725ea734e0ffb68/images/topco.png)

## Results
This data job salary focused project tells us that most salries fall in between 70-120k. 
The top skills required for these data jobs are:
+ SQL
+ Tableau
+ Excel
+ Python
+ Power BI
When it comes to remote vs non-remote jobs, the data shows a slight salary drop for non-remote workers.

Top 3 Paying companies:
+ Upwork
+ Cox Communications
+ Edward Jones

Top 3 Locations (not  pictured but in EDA)
+ Anywhere
+ United States
+ Wichita, KS
 
## Next Actions

Most hist plots demonstrate right skewed data therefore we could remove outliers (likely senior level roles) to get closer to a normal distribution. This in turn would improve a linear regression model. For company information, recruiting and contracting firms could also be removed to have a more accurate idea of company salaries. Lastly, location data was not insightful since the top 2 locations are super general and the dataset is missing data from major cities like NY and LA.

To expand on this project more job posting data can be collected for analysis. A look at the relationships between skill and job roles could be interesting as well.
 