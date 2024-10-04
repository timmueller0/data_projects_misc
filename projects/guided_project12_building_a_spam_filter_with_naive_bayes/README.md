# Building a Spam Filter with Naive Bayes

In this project, we're going to study the practical side of the algorithm by building a spam filter for SMS messages.

To classify messages as spam or non-spam, we saw that the computer:

- Learns how humans classify messages.
- Uses that human knowledge to estimate probabilities for new messages — probabilities for spam and non-spam.
- Classifies a new message based on these probability values — if the probability for spam is greater, then it classifies the message as spam. Otherwise, it classifies it as non-spam (if the two probability values are equal, then we may need a human to classify the message).

So our first task is to "teach" the computer how to classify messages. To do that, we'll use the multinomial Naive Bayes algorithm along with a dataset of 5,572 SMS messages that are already classified by humans.

The dataset was put together by Tiago A. Almeida and José María Gómez Hidalgo, and it can be downloaded from the The [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection). You can also download the dataset directly [from this link](https://dq-content.s3.amazonaws.com/433/SMSSpamCollection). The data collection process is described in more details on [this page](http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/#composition), where you can also find some of the authors' papers.

## Data Files

This project includes the following data files:

- `SMSSpamCollection`: SMS Message Spam Dataset

### Instructions

1. Download or clone this repository.
2. Ensure that the data files are located in the `Data/` directory.
3. Open the Jupyter Notebook `Guided_project_13 - Building a Spam Filter with Naive Bayes.ipynb` and run the cells to reproduce the analysis.

### Project Notebook

You can also directly view or run the analysis in the [Jupyter Notebook](https://github.com/timmueller0/data_projects_misc/blob/main/projects/guided_project12_mobile_app_for_lottery_addiction/Guided_project_12%20-%20Mobile%20App%20for%20Lottery%20Addiction.ipynb))


