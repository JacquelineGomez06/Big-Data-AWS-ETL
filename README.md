# Big-Data-AWS-ETL
An analysis of US Data job trends focused on standard salaries, remote vs non-remote, location, and companies.

Tools Used:
+ sqlalchemy
+ pandas
+ matplotlib
+ seaborn

## Methodology

Connnect to AWS,query,save as pandas data frames

![extract](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/extract.png)

Join all 3 tables and save new data as csv

![join](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/join.png)

After some data cleaning, categorical data from the description_tokens columns was transformed into numerical data. Each of the skills listed were turned into columns with sklearn one-hot encoding.

![join](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/transform.png)

Data is now ready for visualizations and statistical testing

## Visuals

KstestResult(statistic=0.08846265470616899, pvalue=1.2767836585040726e-15)

![salary](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/salary.png)

![remotevnon](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/remote%20vs%20nonremote.png)

![skills](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/topskills.png)

![sql](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/sql.png)

![python](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/python.png)

![tableau](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/tableau.png)

![topco](https://github.com/JacquelineGomez06/Big-Data-AWS-ETL/blob/b93f200e2dbec883bc7c795da3de9f6f079b688c/images/topco.png)

## Results

## Next Actions