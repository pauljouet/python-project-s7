# S7 Python Project

The goal of the project is to study a dataset and apply learning methods on it, using Python and packages such as sklearn, pandas and numpy.
In our case, we will study the [YearPredictionMSD Data Set](https://archive.ics.uci.edu/ml/datasets/YearPredictionMSD). The elements of the dataset are 515345 songs, with 90 attributes representing timbres, and the target is the release year of the song.

The dataset contains mostly western and pop music, and the audio features are described as real numbers.
We will try modelling a regression for estimating the release year of a song. We might also try another approach using ranges of years (70s, 80s... for example) if the results are not satisfying.

## Information

We developped an API using Flask, when launching the server using 'app.py', use type 'localhost:5000' as a URL in your web browser to access the main page of the form. Also the working directory should be the one containing 'python-project-s7'.

The Jupyter Notebook is quite readable (not a lot of lines printed by different models) and provides more information than the presentation and the README.md, to use it the working directory should be 'python-project-s7'.

The dataset 'YearPredictionMSD.txt' is too heavy to share on github, you should download it through [this link](https://archive.ics.uci.edu/ml/machine-learning-databases/00203/YearPredictionMSD.txt.zip) and unzip it into the 'data' folder of our repositery.

## Conclusions

Using deep learning we managed to fit interesting models, given the difficulty of the task and spreadness of the data, our models are only able to predict years close to 2000, but will give more accurate answers in a wider range than any other machine learning model. Tuning the model even further will not help much more.

Our leads to further improve the models are :

- **Splitting the features**, and treat individually the _mean_, _variance_ and _covariance_ of the timbres
- **Oversample/Undersample** : to artificially change the distribution of the features using a clever pre-processing protocol
- Change the **loss function**, we have used MSE but we could try using our custom metric (defined in the notebook)
