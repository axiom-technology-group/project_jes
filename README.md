# project_jes

### the proejct1(6.17) folder ---  is documented the project I did on data science form 6.17 to 8.19, it contains the News atricle data I scraped from ChinaDaily website, and doing NLP and model building on the exsiting data.

______________________________________________________________________________________________________________________________

### the project2(8.19) folder ---  is documented the project I did since 8.19,

#### 1.0 scraping the data and simple data cleaning:
##### scrapy: it contains scrapy(the tool I mainly used for scrapying the data -- with 37 spiders that scraped the office,shop,residential data from multiple resources,using rotating IP and fake user agent dealing with the anti-crawling detection and blocking. all the scraped data can be further connected to Database.
##### simple scraper: simple scraper using bs4.

#### 2.0 more on data cleaning and location adding:
##### BUY: all the real estate that are on sell, including 5 cities (Beijing, Shanghai, chengdu, shenzhen, guangzhou) and 3 types of bulding. also connected with gaode API to attain the location coordinates.
##### RENT: all the real estate that are for rent, including 5 cities (Beijing, Shanghai, chengdu, shenzhen, guangzhou) and 3 types of bulding. also connected with gaode API to attain the location coordinates.


#### 3.0 data combination:
##### BUY: combining and cleaning the previous data for sell.
##### RENT: combining and cleaning the previous data for rent.

#### the next step will be getting the vectors and model building.

#### For all the files(including data) with reference on model building check the link: https://pan.baidu.com/s/1rraiuGeCXP5Oe5Xo5QK9VA

#### 4.0 model exploration.
___________________________________________
#### exploration 1. house price prediction:
  ##### using conventional nural networks models based on the reference to predict the house price in shanghai area.
  ##### the result shows significant improment on the prediction result comparing with other tradition machine learning models.
  ##### 1. tocsv.py Select useful attributes, extract data into data_c.csv file, and filter out unreasonable points and outliers. Some of the attributes attrs = ['decoration_condition', 'elevator', 'ownership', 'framework'] have unknown values, initially used -1 instead, as a new type, the model prediction effect is not ideal; after using the random forest RandomForestClassifier The unknown value is predicted, and the processed data is written to the data_r.csv file.
  ##### (27 input attributes + 2 output attributes Average room rate and total room rate, predicted total room rate when forecasting)
  (61,609 data)
  ##### 2. split.py splits the data set into training dataset train_data.csv and test dataset test_data.csv, each accounting for 80% and 20%
  ##### 3. Train the model and debug it, mainly using some logistic regression models in the sklearn library (train_data_sklearn.py) and using keras to build a neural network (train_data_nn.py).

  ##### 4.The ordinary linear model, the ridge regression model, and the lasso model are used in the sklearn library for prediction. R^2 is 0.696975214012, 0.696961885394, and 0.696974904752, respectively.
  
  ##### 5.A two-layer neural network was built with keras. The activation function uses relu, and R^2 is 0.728964325027.It can be seen that the effect of the neural network is better.

  ##### Further improvement:Since different variables often use different units of measure, they differ greatly in numerical value, making it easy for models based on distance metrics to be susceptible to variables with large values. So normalize the data and compress the data into a range so that the unit impact of all variables is consistent. Normal.py normalizes the data in data_r.csv, saves it to data_n.csv, and repartitions the training set and test set.The model was trained again and predicted that the ordinary linear model, the ridge regression model, and the lasso model did not change much, and the R^2 value of the neural network model was significantly improved 0.748450522912.
  
  ##### It is also found that the mean square error of the neural network model during training is better than the mean square error of the prediction, so there may be an over-fitting phenomenon, so the dropout layer added in the neural network is updated every time during the training process. The parameters are randomly disconnected from the input neurons by a probability of 0.05 to prevent overfitting. After further adjustment, the R^2 value of the predicted result can be maintained above 0.747. The current module.h5 is a better model, and R^2 is 0.75180572067.

### project_cpfreshmartshop
#### is the recent project made in 2021, september 14th, aim at crawling the website from https://cpfreshmartshop.com/en/


