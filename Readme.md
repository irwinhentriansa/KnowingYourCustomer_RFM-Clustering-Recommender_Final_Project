# JCDSJKT09 -Final Project-
<hr>

Final Project as a requirement for completing the Job Connector Data Science in Purwadhika Startup & Coding School Jakarta Batch 09.

> *RFM is a method used for analyzing customer value*

Original `Data Set` taken from : https://www.kaggle.com/mashlyn/online-retail-ii-uci

This `dataset` have 8 columns and 1067371 rows
<hr>

# The Brief Background

>*You've got to start with the customer experience and work back toward the technology - not the other way around.*
<br>-Steve Jobs.

# Business Insights.

- Does it matter knowing what kind of products that they love ?

- When the best time to give an emphaty tou your customer ?

- How do you get in touch with your Customer?


## Workflow

<img src="https://i.imgur.com/1jrJj0xh.png" title="source: imgur.com"/>


## Let's Take a Look The Features:

> - InvoiceNo: Invoice number. Nominal. A 6-digit integral number uniquely assigned to each transaction. If this code starts with the letter 'c', it indicates a cancellation.
> - StockCode: Product (item) code. Nominal. A 5-digit integral number uniquely assigned to each distinct product.
> - Description: Product (item) name. Nominal.
> - Quantity: The quantities of each product (item) per transaction. Numeric.
> - InvoiceDate: Invice date and time. Numeric. The day and time when a transaction was generated.
> - UnitPrice: Unit price. Numeric. Product price per unit in poundsterling.
> - CustomerID: Customer number. Nominal. A 5-digit integral number uniquely assigned to each customer.
> - Country: Country name. Nominal. The name of the country where a customer resides.
<hr>



### 1. Data Cleaning and Preprocessing

**A. Cleaning** 

- Checking The Null Values and checking the relatable data through each rows using **`msno`**

- Drop The Duplicated Values, and keep the first rows where data has represented by duplicates.

- Remove the minus values on Price and Quantity

- Imputing missing values on `CustomerID` which have been *overlap* checking in Invoice

- Imputing missing values on `Description` which have been overlaping with `StockCode`

**B. Enhancing Features to Get Time Series Features/Columns**

- We have an `InvoiceDate` disparting its features to get a month, year, hour, days, and week.

### 2. Exploratory Data Analysis (EDA)

Get an insights from the data where have a story behind.

### 3. RFM Analysis and Clustering

![RFM and Clustering](https://user-images.githubusercontent.com/61248667/92995376-40570680-f52d-11ea-8926-f479f36a527d.png)

> Those clustering based on goal oriented by Elbow-Methods, Silhoutte Score, DaviesBouldin Score then we have 5 clustering are representing by distribution of labelling to each customer.

### 4. Product Recommender and Bundling through time based on clustering and RFM

**Recommender System**

![Recommender System](https://user-images.githubusercontent.com/61248667/92995446-ff132680-f52d-11ea-81f4-d8149db0b1f4.png)

**Product Bundling**

![Product Bundling](https://user-images.githubusercontent.com/61248667/92995477-3e417780-f52e-11ea-959e-9d334af4e2e7.png)


### Conclusion

> *The best marketing doesn't feel like marketing* - Tom Fishburne
