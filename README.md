# Solar Power Forecasting
## Datasets

### Historical Weather Data
I used [Darksky API](https://darksky.net/dev) for historical weather dataset. I wrote [Jupyter Notebook](https://github.com/nailtosun/Ayasli-Ges-Solar-Prediction/blob/master/Neural%20Network/Darksky-api/Datapulling.ipynb) which automate pulling data (basically automate http request then format the JSON file). You can use for your purposes it's open source. However ofter 1000 data point you should use API key which cost 1$ per 10000 data points.(I think it is really inexpensive). 

### Solar Generation Data
We used [Solar-Log](https://www.solar-log.com/en/) for logging the solar generation. Our system is 50kW rated PV system which located Ayaslı Research Center in METU. 

## Algoritms 
The algoritm we used are;
* Neural Networks (classical way 2 hidden layer)
* Recurrent Neural Network (RNN)
* Long Short Term Memory (LSTM)
* LSTM with Encoder Network

## Hardware in the loop
Our cloud cover data mostly depend on Darksky which has 25km^2 resolution. Therefore, we built fish-eye camera for sky-imaging.

## Future ideas
* Using deep learning to forecasting next frame of sky image which will be feeded NN.
* Using Kalman filters to optimize system states continuously.
