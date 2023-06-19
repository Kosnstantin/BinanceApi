
How to use task1\task2

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Install the libraries that are listed in the file requirements.txt
First of all you need click the link (Ctrl+click) https://www.binance.com/ru-UA/my/settings/api-management and create API (you will got API Key and Secret Key);
Paste them in 11-12 strings (task1), then you can debug script;
If you want get only db and file.csv, you can debug task1, but if you want get Flask UI with candlestick and piechart on the website - you need debug task2.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We can deploy our code using the AWS service, use the Elastic Beanstalk service. Click on the environment tab on the left, then click on "Create environment", name it, and select the platform (in our case it is Python). Create the environment, and then deploy our archive with the code files. We will get a link to go to and this web page will contain our Flask UI.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can look at the code, I saved the data in a csv file, as well as in a relational database (SQLite)