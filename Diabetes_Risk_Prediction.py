{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "import seaborn as sns\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "np.random.seed(42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('Diabetes_Data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Polyuria</th>\n",
       "      <th>Polydipsia</th>\n",
       "      <th>sudden weight loss</th>\n",
       "      <th>weakness</th>\n",
       "      <th>Polyphagia</th>\n",
       "      <th>Genital thrush</th>\n",
       "      <th>visual blurring</th>\n",
       "      <th>Itching</th>\n",
       "      <th>Irritability</th>\n",
       "      <th>delayed healing</th>\n",
       "      <th>partial paresis</th>\n",
       "      <th>muscle stiffness</th>\n",
       "      <th>Alopecia</th>\n",
       "      <th>Obesity</th>\n",
       "      <th>class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>40</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>58</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>41</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>45</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>60</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Age Gender Polyuria Polydipsia sudden weight loss weakness Polyphagia  \\\n",
       "0   40   Male       No        Yes                 No      Yes         No   \n",
       "1   58   Male       No         No                 No      Yes         No   \n",
       "2   41   Male      Yes         No                 No      Yes        Yes   \n",
       "3   45   Male       No         No                Yes      Yes        Yes   \n",
       "4   60   Male      Yes        Yes                Yes      Yes        Yes   \n",
       "\n",
       "  Genital thrush visual blurring Itching Irritability delayed healing  \\\n",
       "0             No              No     Yes           No             Yes   \n",
       "1             No             Yes      No           No              No   \n",
       "2             No              No     Yes           No             Yes   \n",
       "3            Yes              No     Yes           No             Yes   \n",
       "4             No             Yes     Yes          Yes             Yes   \n",
       "\n",
       "  partial paresis muscle stiffness Alopecia Obesity     class  \n",
       "0              No              Yes      Yes     Yes  Positive  \n",
       "1             Yes               No      Yes      No  Positive  \n",
       "2              No              Yes      Yes      No  Positive  \n",
       "3              No               No       No      No  Positive  \n",
       "4             Yes              Yes      Yes     Yes  Positive  "
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss',\n",
       "       'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',\n",
       "       'Itching', 'Irritability', 'delayed healing', 'partial paresis',\n",
       "       'muscle stiffness', 'Alopecia', 'Obesity', 'class'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.rename(columns={'sudden weight loss': 'Sudden_Weight_Loss', 'weakness':'Weakness', 'Genital thrush' : 'Genital_Thrush', 'visual blurring': 'Visual_Blurring', 'delayed healing':'Delayed_Healing',\n",
    "                  'partial paresis': 'Partial_Paresis', 'muscle stiffness':'Muscle_Stiffness'}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 520 entries, 0 to 519\n",
      "Data columns (total 17 columns):\n",
      " #   Column              Non-Null Count  Dtype \n",
      "---  ------              --------------  ----- \n",
      " 0   Age                 520 non-null    int64 \n",
      " 1   Gender              520 non-null    object\n",
      " 2   Polyuria            520 non-null    object\n",
      " 3   Polydipsia          520 non-null    object\n",
      " 4   Sudden_Weight_Loss  520 non-null    object\n",
      " 5   Weakness            520 non-null    object\n",
      " 6   Polyphagia          520 non-null    object\n",
      " 7   Genital_Thrush      520 non-null    object\n",
      " 8   Visual_Blurring     520 non-null    object\n",
      " 9   Itching             520 non-null    object\n",
      " 10  Irritability        520 non-null    object\n",
      " 11  Delayed_Healing     520 non-null    object\n",
      " 12  Partial_Paresis     520 non-null    object\n",
      " 13  Muscle_Stiffness    520 non-null    object\n",
      " 14  Alopecia            520 non-null    object\n",
      " 15  Obesity             520 non-null    object\n",
      " 16  class               520 non-null    object\n",
      "dtypes: int64(1), object(16)\n",
      "memory usage: 69.2+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Age                   0\n",
       "Gender                0\n",
       "Polyuria              0\n",
       "Polydipsia            0\n",
       "Sudden_Weight_Loss    0\n",
       "Weakness              0\n",
       "Polyphagia            0\n",
       "Genital_Thrush        0\n",
       "Visual_Blurring       0\n",
       "Itching               0\n",
       "Irritability          0\n",
       "Delayed_Healing       0\n",
       "Partial_Paresis       0\n",
       "Muscle_Stiffness      0\n",
       "Alopecia              0\n",
       "Obesity               0\n",
       "class                 0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Feature Engineering"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Gender"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Male      328\n",
       "Female    192\n",
       "Name: Gender, dtype: int64"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Gender'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Gender  class   \n",
       "Female  Positive    0.901042\n",
       "        Negative    0.098958\n",
       "Male    Negative    0.551829\n",
       "        Positive    0.448171\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Gender')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Females have higher tendency to be diabetic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAgcAAAGoCAYAAADSA0adAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAc2ElEQVR4nO3de5RdZZnn8W/lRmiSKF1mQLkYFfI4XtNyVVHSmvHWtspSuYpNYwKOoN0jY1oFFbBbRhTBG2ITAzRXUSaOgCDKpZWLCAgCAzziSFhi0q5Y0pCgIYlV88feJectkkpVpc7ZlarvZ61aqf3ufd79nHV2Vf3y7svb1dfXhyRJUr9JTRcgSZLGFsOBJEkqGA4kSVLBcCBJkgrjIRxMAebU/0qSpC00Hv6g7gw81NOzht5e77yQpPFu9uyZXU3XMN6Nh5EDSZI0igwHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqSC4UCSJBUMB5IkqWA4kCRJBcOBJEkqGA4kSVLBcCBJkgqGA0mSVDAcSJKkguFAkiQVpjRdgLZu2z9jGlOmbdN0GVuNDeue5NHH1jVdhiQNynCgLTJl2jbccerCpsvYauyxeAlgOJA0tnlaQZIkFQwHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUaOtzDiJiFnAz8FbgRcBnWlbvBNyamW+NiE8BRwKP1uvOzsyvtrM2SZK0cW0LBxGxD3A2MBcgM78HfK9etyNwE/A/6s33BA7OzFvaVY8kSRqadp5WWAQcA6zYyLrPAWdl5oP18p7AxyPi7oj4SkRMb2NdkiRpEG0bOcjMhQARUbRHxO7AfKB//QzgTuAjwC+Bc4FPAMcPZ3/d3TO2sGKpM2bPntl0CZI0qCbmVjgKODMznwTIzDXAW/pXRsRpwFKGGQ56etbQ29s3mnVqCPxDN3yrVq1uugRpq+bvnfZr4m6FdwCX9C9ExK4RcWTL+i5gfcerkiRJQIdHDiLiWcC2mflQS/MfgVMj4npgOdV1Css6WZckSXpKp08rPB94pLUhM1dFxNHA5cA04EbgtA7XJU1oM2dNZ/o2U5suY6uy9sn1rH58bdNlSG3R9nCQmXNavv8psO9GtrkMuKzdtUjauOnbTOXQxRc2XcZW5aJTD2M1hgONTz4hUZIkFQwHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqSC4UCSJBUMB5IkqWA4kCRJBcOBJEkqGA4kSVLBcCBJkgqGA0mSVDAcSJKkguFAkiQVDAeSJKlgOJAkSQXDgSRJKhgOJElSwXAgSZIKhgNJklQwHEiSpILhQJIkFQwHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqSC4UCSJBUMB5IkqWA4kCRJBcOBJEkqGA4kSVLBcCBJkgqGA0mSVDAcSJKkguFAkiQVprSz84iYBdwMvDUzl0fEOcB+wBP1Jidl5rKImAcsAWYBPwLen5kb2lmbJEnauLaFg4jYBzgbmNvSvCfw2sxcOWDzC4CFmfmTiPgGsAj4WrtqkyRJm9bOkYNFwDHA+QAR8RfArsDSiNgJWAacBOwCbJuZP6lfd27dbjiQJKkBbQsHmbkQICL6m3YErgM+ADwGXAG8D7gXaB1JWAnsPNz9dXfP2IJqpc6ZPXtm0yVolPhZarxq6zUHrTLzV8AB/csR8WXgvcB9QF/Lpl1A73D77+lZQ29v3+Y31Kjyl+PwrVq1uukSnsbPcWTG4mc5EXi8tl/H7laIiJdGxDtbmrqA9cAjwLNb2ncEVnSqLkmSVOrkrYxdwBkRsX1ETAWOApZl5sPA2oh4db3d4cBVHaxLkiS16Fg4yMy7gVOAm6hOJdyVmRfXqw8DTo+IB4AZwJc6VZckSSq1/ZqDzJzT8v2ZwJkb2ebnwN7trkWSJG1exy5I3FrMnDWd6dtMbboMSZIaYzgYYPo2Uzl08YVNl7HVuOjUw5ouQZI0ypxbQZIkFQwHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqSC4UCSJBUMB5IkqWA4kCRJBcOBJEkqGA4kSVLBcCBJkgqGA0mSVDAcSJKkguFAkiQVDAeSJKlgOJAkSQXDgSRJKhgOJElSwXAgSZIKhgNJklQwHEiSpILhQJIkFQwHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqSC4UCSJBUMB5IkqWA4kCRJBcOBJEkqGA4kSVLBcCBJkgpT2tl5RMwCbgbempnLI+Io4ENAH3A7cHRmrouITwFHAo/WLz07M7/aztokSdLGtS0cRMQ+wNnA3Hp5LvARYA9gNXAucAxwOrAncHBm3tKueiRJ0tC087TCIqo//ivq5SeBD2Tm45nZB9wD7Fqv2xP4eETcHRFfiYjpbaxLkiQNom0jB5m5ECAi+pcfBh6u22YDxwJHRMQM4E6qUYVfUo0ofAI4fjj76+6eMUqVS+01e/bMpkvQKPGz1HjV1msONiYidgKuAr6RmTfUzW9pWX8asJRhhoOenjX09vZtcX3+sKvdVq1a3XQJT+NxPzJj8bOcCDxe26+jdytExAupLlA8LzM/XbftGhFHtmzWBazvZF2SJOkpHRs5iIiZwDXA8Zl5fsuqPwKnRsT1wHKq6xSWdaouSZJU6uRphYXADsBxEXFc3fbdzPxkRBwNXA5MA24ETutgXZIkqUXbw0Fmzqm/Pb3+2tg2lwGXtbsWSZK0eT4hUZIkFQwHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqSC4UCSJBUMB5IkqWA4kCRJBcOBJEkqGA4kSVLBcCBJkgqGA0mSVDAcSJKkguFAkiQVDAeSJKlgOJAkSQXDgSRJKhgOJElSwXAgSZIKhgNJklQwHEiSpILhQJIkFQwHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqSC4UCSJBUMB5IkqWA4kCRJBcOBJEkqGA4kSVLBcCBJkgqGA0mSVDAcSJKkguFAkiQVprSz84iYBdwMvDUzl0fEAuALwLbANzPzhHq7ecASYBbwI+D9mbmhnbVJkqSNa9vIQUTsA9wIzK2XtwWWAm8H/iuwV0S8ud78AuDYzJwLdAGL2lWXJEkaXDtPKywCjgFW1Mt7Aw9m5kP1qMAFwLsj4rnAtpn5k3q7c4F3t7EuSZI0iLadVsjMhQAR0d/0HGBlyyYrgZ0HaR+W7u4ZI6pT6rTZs2c2XYJGiZ+lxqu2XnMwwCSgr2W5C+gdpH1YenrW0Nvbt/kNN8MfdrXbqlWrmy7haTzuR2YsfpYTgcdr+3XyboVHgGe3LO9IdcphU+2SJKkBnQwHtwIREbtFxGTgUOCqzHwYWBsRr663Oxy4qoN1SZKkFh0LB5m5FjgCuAy4D3gA+Ha9+jDg9Ih4AJgBfKlTdUmSpFLbrznIzDkt318LvHwj2/yc6m4GSZLUMJ+QKEmSCoYDSZJGKCLmR8S9Tdcx2gwHkiSp0MnnHEiStFWLiCOB44A/Ab8DzmlZNxf4KjCT6hb9u4CDMnNtRJwEHACsA3qAIzJz5abaO/iWNsqRA0mShiAiXg58FnhTZr4M+C5wfMsmi4DzMnNfYDfgecDfRMQuwD8Ce2XmnsA1wD6bau/YGxqE4UCSpKF5PfD9zPw1QGaeAby/Zf0/AasiYjHwNarpAWYAvwF+DvwsIj4P3JWZ3xmkvXGGA0mShmYDLY/7r2cbfmHL+ouBo4CHgdOBnwFdmdkL7E/1rJ8equf6nLqp9va/jc0zHEiSNDTXAwsiov+R/0cDrX/M3wicnJnfrJf3ASbXpyPuBe7PzFOogsNem2rvwPvYLMOBJElDkJn3AB8Bro6InwNvojyt8HFgWUTcA3wd+Hdgt/pBf5cCt0fE7cCRwIc31d6xNzQI71aQJGmIMvMC4IIBzRfV684EztzE604CThpqe9McOZAkSQXDgSRJKhgOJElSwXAgSZIKhgNJklQwHEiSpIK3MkqSxoV16zf8x7SpU3ZoQ7+/nTZ1yo6DbRMRc4BfAPdRPUVxGrAC+PvMfGSo+4qItwF7ZuYn60mZfpiZP46IJcBZmXn7SN/HcBgOJEnjwrSpU3Y4dPGFo97vRaceNtTAsSIz5/UvRMRpwOeAQ4a6r8z8LtWETlA9Wvn6un3hUPsYDYYDSZLa43rglIjYF/giMJ1qmuejM/OXEfFh4O+AXuCnmXl0RBwBzAeuA/YElkTEAcCXgROBDwEXZuZlABFxB7AQWE012VM38Afgg5l550gL95oDSZJGWURMBd4F3AZcAhybmS8HzgIujojJwMeoAsAewLSI2Kn/9Zn5b8DtwML6sc39zqceiYiI3YHpdQg4D1icma+gmvzpki2p33AgSdLoeE5E3BURdwF3A13AucCjmXkbQGZ+C9iNairnm6nCw6eA0zLzN0PYx5XAKyNiJlVIuCAiZlBN2HROve+LgBkR0T3SN+JpBUmSRkdxzQFARLxsI9t1AZOBdwD7Am+mmszpsM3tIDPXRcTlwNuAA4G/qftaO+B6h52B34/0jThyIElS+yTQHRF7AUTEgcDDVH/Q7wPuycxPAtcAA4PEBjb+n/jzgeOAnsx8ODMfAx6MiPfU+/hvwI+2pGjDgSRJbZKZTwIHAV+JiHuBY4GDMnMV8K/AbfVFhdOBpQNefjVwVkS8akCfNwHPoJwd8jBgYUTcDZxS76NvpHV7WkGSNC6sW7/ht8O47XBY/U6bOvify8xcDszZxLpbgH020n46cPqA5nPrLzLz88Dn6/b5A177ggHLDwzcZksYDiRJ48LmHlS0Bf22o9sxzdMKkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSdK40Lt+3X9QTZc8ql91vxPKxLs/Q5I0Lk2aOm2HO04d/ZmN91i8ZLPPToiIOcBDwBsy8wct7cuB+fVzELZYRJwE/DAzfxwRS4CzMvP20ei7lSMHkiSNjvXA2fWkSO2yP9Wjl8nMhe0IBuDIgSRJo2UF8APgNKppk/8sIj5KNVHSZOD7wD9lZl9EfAj4IPCfwAPA/8vMEyPiWOBwYDtgHdUMjPtQTfG8JCIOAL4MnAh8CLgwMy+r93UHsBBYDXwN6Ab+AHywnt55sxw5kCRp9BwHvLGe/Kjfm4A9qKZV/itgJ+CwesbGY+p1rwF2B4iIWVQzNs7PzJcAVwDHZua/AbcDCzPznpb+z6cKD0TE7sD0OgScByzOzFdQhZVLhvomDAeSJI2SzHwcWER5emEB1f/67wB+RvW//xfX7Vdk5uOZuRa4uKWPQ4GDI+IU4G+BGYPs9krglfX+DgEuiIgZVGHknIi4C7gImBER3UN5H4YDSZJGUWZew1OnF6A6lXBGZs7LzHlUQeFfgD+xkb/DEbELcAvwTOAqqomYugbZ3zrgcuBtVKcuLqr3ubZ/ny37/f1Q3oPhQJKk0Xcc8Ebg2cB1wOERMSMipgDfAd4FXAu8JSJmRcQ04J1Ut0/uBfyynrXxNuAA6osQgQ1s/HrB8+t99mTmw5n5GPBgRLwHoD7N8aOhFu8FiZKkcaF3/brfDuW2w5H0O2nqtGG9JjMfj4hFVBcfXg48A7iV6o/81cB59QWJX6IaJVgD/A74I3AN8N8j4j6qEYN/B15Sd301cFZEvHfA/m6KiGdQXYDY77B628VUFzUelJl9Q6m/4+EgIhYCx7Y0PY8q8WwH7Ac8UbeflJnLOlyeJGkrNWnqtLZM2TyUYFA/x2DOgLZreOp0wD/XX38WEXOBaZn54nr5/wD3Z+YaoPWCxtY+Pw98vl6cP2DdCwYsPzBwm6HqeDjIzCXAEoCIeDHV8MqJwPXAazNzZadrkiSpAQ8De0XEvVSnE75PdWdC45o+rfA14ONU91/uCiyNiJ2AZVQjB71NFidJUrtk5pNUdyWMOY1dkBgRC4BtM/NbwI5UF2wcCexLdb/n+5qqTZKkiazJkYOjgS8AZOavqK7GBCAivgy8Fzh7qJ11dw92C6g0dsye3c4nq6qT/Cw1XjUSDupbNvYHjqiXXwrM7X/0I9UFHOuH02dPzxp6e4d0Eeag/GFXu61atbrpEp7G435kxuJnORF4vLZfUyMHLwN+kZn9dyZ0AWdExHVUt3McRfXYR0mS1GFNXXPwfOCR/oXMvBs4BbgJuA+4KzMvbqg2SZImtEZGDjLzUuDSAW1nAmc2UY8kSXqKj0+WJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqSC4UCSJBUMB5IkqWA4kCRJBcOBJEkqGA4kSVLBcCBJkgqGA0mSVDAcSJKkguFAkiQVDAeSJKlgOJAkSQXDgSRJKhgOJElSwXAgSZIKhgNJklQwHEiSpILhQJIkFQwHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqSC4UCSJBUMB5IkqWA4kCRJBcOBJEkqGA4kSVLBcCBJkgqGA0mSVDAcSJKkguFAkiQVDAeSJKlgOJAkSYUpTew0Iq4H/guwvm46GpgJfAHYFvhmZp7QRG2SJE10HQ8HEdEFzAWem5kb6rZtgQT2B34NXBkRb87MqzpdnyRJE10TIwdR/3tNRHQDZwP3AA9m5kMAEXEB8G7AcCBJUoc1EQ62B64FPghMBW4APgusbNlmJbDzcDrt7p4xSuVJ7TV79symS9Ao8bPUeNXxcJCZtwC39C9HxDeAk4EbWzbrAnqH029Pzxp6e/u2uD5/2NVuq1atbrqEp/G4H5mx+FlOBB6v7dfxuxUiYr+IeH1LUxewHHh2S9uOwIpO1iVJkipNnFZ4JnByRLyK6rTC3wHvBy6NiN2Ah4BDgaUN1CZJ0oTX8ZGDzLwCuBK4E7gDWFqfajgCuAy4D3gA+Hana5MkSQ095yAzPwF8YkDbtcDLm6hHkiQ9xSckSpKkguFAkiQVDAeSJKlgOJAkSQXDgSRJKhgOJElSwXAgSZIKhgNJklQwHEiSpILhQJIkFQwHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqSC4UCSJBUMB5IkqWA4kCRJBcOBJEkqGA4kSVLBcCBJkgqGA0mSVDAcSJKkguFAkiQVDAeSJKlgOJAkSQXDgSRJKhgOJElSwXAgSZIKhgNJklQwHEiSpILhQJIkFQwHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqTClCZ2GhGfAg6sF6/MzMURcQ6wH/BE3X5SZi5roj5JkiayjoeDiFgAvAH4K6APuDoiDgD2BF6bmSs7XZMkSXpKEyMHK4HjMnMdQETcD+xafy2NiJ2AZVQjB70N1CdJ0oTW8XCQmf+3//uI2J3q9MJrgPnAB4DHgCuA9wFnD7Xf7u4Zo1qn1C6zZ89sugSNEj9LjVeNXHMAEBEvBq4EPpKZCRzQsu7LwHsZRjjo6VlDb2/fFtflD7vabdWq1U2X8DQe9yMzFj/LicDjtf0auVshIl4NXAt8NDPPi4iXRsQ7WzbpAtY3UZskSRNdExck7gJ8BzgoM6+rm7uAMyLiOmANcBRwXqdrkyRJzZxW+J/AdOALEdHfdhZwCnATMBW4LDMvbqA2SZImvCYuSPwH4B82sfrMTtYiSZKezickSpKkguFAkiQVDAeSJKlgOJAkSQXDgSRJKhgOJElSobHHJ0vS1qx3w3of4zsMG9Y9yaOPrWu6DA2R4UCSRmDSlKnccerCpsvYauyxeAlgONhaeFpBkiQVDAeSJKlgOJAkSQXDgSRJKhgOJElSwXAgSZIKhgNJklQwHEiSpILhQJIkFQwHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqSC4UCSJBUMB5IkqWA4kCRJBcOBJEkqGA4kSVLBcCBJkgqGA0mSVDAcSJKkguFAkiQVDAeSJKlgOJAkSQXDgSRJKhgOJElSwXAgSZIKhgNJklQwHEiSpMKUpgtoFRGHAicAU4EzMvOrDZckSdKEM2ZGDiJiJ+BfgP2AecBREfGiZquSJGniGUsjBwuA6zLz9wAR8W3gXcDJm3ndZIBJk7pGrZBnbb/dqPU1EUyb1d10CVuV0TxWR5PH/fB57A/PKB77c4BHgA2j1aFKXX19fU3XAEBEfAzYLjNPqJcXAntn5lGbeel+wI/bXZ8kaUx5HrC86SLGq7E0cjAJaE0qXUDvEF53G/AaYCXwpzbUJUkaex5puoDxbCyFg0eo/sj32xFYMYTXPQnc2JaKJEmagMZSOPghcGJEzAaeAN4JbO6UgiRJGmVj5m6FzPwNcDxwPXAXcFFm/rTZqiRJmnjGzAWJkiRpbBgzIweSJGlsMBxIkqSC4UCSJBUMB5IkqWA4kCRJhbH0nAONERExB3gI+NfMPLqlfR5wJ/D3mXnuJl67HJifmcvbXac0EvXx/QvgvgGr/jYzf92Gfd2QmXNGs1+p3QwH2pQe4E0RMTkz+x9LfRCwqsGapNGyIjPnNV2ENFYZDrQpa6geRvVaqgdTAbyB6kmWRMSxwOHAdsA64JDMzP4XR8Rk4HPAfKqZM8/NzNM7Vbw0XBGxA/B1YBeqeV0+lpk/jIgTgV2BucBsqqnlXw/sA/wcOJjqGP8a8BJgB+Bu4JCh9N/2NyaNgNccaDCXUk2bTUTsRfULbx0wC3gH1emDlwBXAMcOeO0igMx8BbA38PaIeA3S2PCciLir5esjwBeBpZm5B/A24OsRMbPe/qVUQfco4Bzgs1RB4BXAy4BXAesy85XAbsAzgbcM2Odg/UtjiiMHGsx3gX+OiElUpxS+SfW/pMeBQ4GDI2Iu8CaqUYZWC4B5EfG6enkG1S9Yp9fWWPC00woR8TvghRFxct00FXhB/f0PMnNDRDwMrMzM++rX/AbYPjNviIieiDgGeCGwO9Ux32rBJvof+LMjNc6RA21SZq6hGjbdD3gd9SkFqmHRW6j+d3QVcC7VFNutJgOLM3Ne/Ut4X2BpB8qWRmoy8LqWY3Yf4J563bqW7TYMfGFEvA24EPgD1cjCj9j4z8Sm+pfGFMOBNudS4H8Bt2dm/y/FJ4Bf1tcQ3AYcQPWLr9V1wKKImBoRM6im1d63QzVLI3Ed8AGAiHgRcC/wF0N87QLg0sw8B/hP4K/Z+M/ESPuXOspwoM25HJhHdUqh3zpgUkTcB/wMeAB43oDXnQU8SHXr4+3AOZl5Q9urlUbug8C+EXE31fH+nsxcPcTXng0cEhH3AN8CbuLpPxNb0r/UUc7KKEmSCo4cSJKkguFAkiQVDAeSJKlgOJAkSQXDgSRJKviERKkBEXEkcDQwE9gG+BVwQmbeOkr9fwX4XWaeOBr9SZpYHDmQOiwiPgMcCRyYmS/KzBcApwBXRMSuzVYnST7nQOqoema+h4AXZObKAesOp3pg1OPAV6hmApwKXJKZn4mIOcC1wPeoHr27PdUjqpdFxCxgCfByYCXVI35vzMwTI2KnQfr7MXA/MAfYf2BNkiYmRw6kznolcP/G/ghn5vmZeT9wPk/N3rc3sCAiDqw3ez7w/czcG/gocEbdfhLwR6pJf94NREvXg/W3M/DpzJxrMJDUz2sOpM7qAv48XFdP2ds/U+UMqsdV7w/8ZUR8uqV9HvBTYD3VyAFUj67+y/r7BcA/ZmYfsCoiltX9b7eZ/jZQTaIlSX9mOJA661aqaXu7M7Onfrb+PICIOJFq6L8LeFVm/qFufxawFngWsC4ze+u++ihn/mv9vn+SrMmb6e/Jlgm1JAnwtILUUZm5Avgi8K3Wiw8j4rnAq4HVwE+AD9ftz6SaxOftm+n6KuB9ETEpIrbv3z4zHx9hf5ImMMOB1GGZeTzwDeCiiLgzIn4F/G/gGuBjwKFUs/fdQzXScHFmXriZbk+kOuXwANWpiXta1o2kP0kTmHcrSJKkgiMHkiSpYDiQJEkFw4EkSSoYDiRJUsFwIEmSCoYDSZJUMBxIkqTC/wdOsyczFu6q1wAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 515.225x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Gender', kind='count', hue='class', data = df, height=6)\n",
    "plt.ylabel(' ')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Polyuria"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     262\n",
       "Yes    258\n",
       "Name: Polyuria, dtype: int64"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Polyuria'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Polyuria  class   \n",
       "No        Negative    0.706107\n",
       "          Positive    0.293893\n",
       "Yes       Positive    0.941860\n",
       "          Negative    0.058140\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Polyuria')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Positive Polyuria detection correlates highly with diabetes detection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 515.225x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Polyuria', kind='count', hue='class', data = df, height=6)\n",
    "plt.ylabel(' ')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Polydipsia"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     287\n",
       "Yes    233\n",
       "Name: Polydipsia, dtype: int64"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Polydipsia'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Polydipsia  class   \n",
       "No          Negative    0.668990\n",
       "            Positive    0.331010\n",
       "Yes         Positive    0.965665\n",
       "            Negative    0.034335\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Polydipsia')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Positive Polydipsia detection correlates highly with diabetes detection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 443.225x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Polydipsia', kind='count', hue='class', data = df, height=5)\n",
    "plt.ylabel(' ')\n",
    "plt.xlabel('Polyuria', size = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Sudden Weight Loss"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     303\n",
       "Yes    217\n",
       "Name: Sudden_Weight_Loss, dtype: int64"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Sudden_Weight_Loss'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sudden_Weight_Loss  class   \n",
       "No                  Negative    0.564356\n",
       "                    Positive    0.435644\n",
       "Yes                 Positive    0.866359\n",
       "                    Negative    0.133641\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Sudden_Weight_Loss')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Sudden weight loss could be a major symptom of diabetes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAb4AAAFkCAYAAABfKF6gAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAfFUlEQVR4nO3deZxcVZ338U9CEhJJYDBmRFlExfwEN5BVQWUUFJfH0XEUBRfEsAiCC4oKso7KCLKMIC5BhGEVzRMfBVGQgMoiyL7/hJEgCGqMiIkDJLH7+ePc1qLtTrqTrqpOn8/79epXd517695fVSr97XPq1D3jent7kSSpFuO7XYAkSZ1k8EmSqmLwSZKqYvBJkqoyFoJvArBx812SpOUaC2GxAXDfwoWL6elxhqqk1duMGdPGdbuGsW4s9PgkSRoyg0+SVBWDT5JUFYNPklQVg0+SVBWDT5JUFYNPklQVg0+SVBWDT5JUFYNPklQVg0+SVBWDT5JUFYNPklQVg0+SVJWxsCyRNOpNW3syk9ec2O0yOu7xJ5ay6M+Pd7sM6UkMPqkDJq85kd0OPqfbZXTcucfuziIMPo0uDnVKkqpi8EmSqmLwSZKqYvBJkqpi8EmSqmLwSZKqYvBJkqpi8EmSqmLwSZKqYvBJkqpi8EmSqmLwSZKqYvBJkqpi8EmSqmLwSZKq0tb1+CJibeBq4E3AZsDnWzavD1ybmW+KiCOAPYFHmm2zM/PL7axNklSntgVfRGwLzAZmAmTmD4AfNNvWA64CPtrsvhXwzsy8pl31SJIE7R3q3AvYH3hogG3HAV/NzHua21sBh0TErRFxSkRMbmNdkqSKta3Hl5mzACLiSe0R8TxgR6Bv+1TgJuATwL3AGcBhwKHDOd/06VNXsWJJ7TBjxrRulyA9SVvf4xvE3sCpmfkEQGYuBt7QtzEijgdOZ5jBt3DhYnp6ekeyTmnE1PzLf8GCRd0uYbVS82ulU7oxq/MtwPl9NyJio4jYs2X7OGBpx6uSJFWhoz2+iHgaMCUz72tpfgw4NiIuB+ZT3hec28m6JEn16HSP7znAg60NmbkA2Af4PpCUHt/xHa5LklSJtvf4MnPjlp+vA7YbYJ85wJx21yJJUjcmt2gUWHedSUyYtGa3y+i4ZUue4JFHl3S7DEldZPBVasKkNbnh2FndLqPjtjz4NMDgk2rmtTolSVUx+CRJVTH4JElVMfgkSVUx+CRJVTH4JElVMfgkSVUx+CRJVTH4JElVMfgkSVUx+CRJVTH4JElVMfgkSVUx+CRJVTH4JElVMfgkSVUx+CRJVTH4JElVMfgkSVUx+CRJVTH4JElVMfgkSVUx+CRJVTH4JElVMfgkSVUx+CRJVTH4JElVmdDOg0fE2sDVwJsyc35EfBPYAfhLs8tRmTk3IjYHTgPWBn4K7JuZy9pZmySpTm0LvojYFpgNzGxp3gp4ZWY+3G/3s4FZmfnziPgGsBfwlXbVJkmqVzt7fHsB+wNnAUTEU4CNgNMjYn1gLnAUsCEwJTN/3tzvjKbd4JMkjbi2BV9mzgKIiL6m9YB5wH7Ao8CFwAeA24HWHuDDwAbtqkuSVLe2vsfXKjN/Bby173ZEnAy8F7gT6G3ZdRzQM9zjT58+dVVLVCVmzJjW7RKq4vOt0aZjwRcRLwJmZuacpmkcsBR4EHhGy67rAQ8N9/gLFy6mp6d3xTsKqPuX0YIFizp+Tp9vDVXNr5VO6eTHGcYBJ0XEuhExEdgbmJuZ9wOPR8T2zX7vAS7uYF2SpIp0LPgy81bgGOAqyvDmzZl5XrN5d+DEiLgbmAp8qVN1SZLq0vahzszcuOXnU4FTB9jnFmCbdtciSZJXbpEkVcXgkyRVxeCTJFXF4JMkVcXgkyRVxeCTJFXF4JMkVcXgkyRVxeCTJFXF4JMkVcXgkyRVxeCTJFXF4JMkVcXgkyRVxeCTJFXF4JMkVcXgkyRVxeCTJFXF4JMkVcXgkyRVxeCTJFXF4JMkVWVCtwvotmlrT2bymhO7XYYkqUOqD77Ja05kt4PP6XYZHXfusbt3uwRJ6gqHOiVJVTH4JElVMfgkSVUx+CRJVTH4JElVMfgkSVVp68cZImJt4GrgTZk5PyL2Bg4EeoHrgX0yc0lEHAHsCTzS3HV2Zn65nbVJkurUtuCLiG2B2cDM5vZM4BPAlsAi4Axgf+BEYCvgnZl5TbvqkSQJ2jvUuRcl2B5qbj8B7JeZf87MXuA2YKNm21bAIRFxa0ScEhGT21iXJKlibevxZeYsgIjou30/cH/TNgP4ELBHREwFbqL0Bu+l9AQPAw4dzvmmT586QpVrrJsxY1q3S6iKz7dGm45fsiwi1gcuBr6RmVc0zW9o2X48cDrDDL6FCxfT09M77Hr8T1mfBQsWdfycNb/OuvF8r85qfq10SkdndUbE8ymTXc7MzP9o2jaKiD1bdhsHLO1kXZKkenSsxxcR04BLgEMz86yWTY8Bx0bE5cB8yvuCcztVlySpLp0c6pwFPB04KCIOatq+l5mHR8Q+wPeBScCVwPEdrEuSVJG2B19mbtz8eGLzNdA+c4A57a5FkiSv3CJJqorBJ0mqisEnSaqKwSdJqorBJ0mqisEnSaqKwSdJqorBJ0mqisEnSaqKwSdJqorBJ0mqisEnSaqKwSdJqorBJ0mqisEnSaqKwSdJqorBJ0mqisEnSaqKwSdJqorBJ0mqisEnSaqKwSdJqorBJ0mqisEnSaqKwSdJqorBJ0mqisEnSaqKwSdJqorBJ0mqisEnSarKhHYePCLWBq4G3pSZ8yNiJ+AEYArwrcz8TLPf5sBpwNrAT4F9M3NZO2uTJNWpbT2+iNgWuBKY2dyeApwO/CuwKbB1RLy+2f1s4EOZORMYB+zVrrokSXVr51DnXsD+wEPN7W2AezLzvqY3dzbw9oh4FjAlM3/e7HcG8PY21iVJqljbhjozcxZARPQ1PRN4uGWXh4ENltM+LNOnT12pOlWfGTOmdbuEqvh8a7Rp63t8/YwHeltujwN6ltM+LAsXLqanp3fFO/bjf8r6LFiwqOPnrPl11o3ne3U2Wl4rEbEjcEpmvrDbtYy0Ts7qfBB4Rsvt9SjDoIO1S5I04jrZ47sWiIjYBLgP2A04PTPvj4jHI2L7zLwKeA9wcQfrkqTqRcSewEHAX4E/AN9s2TYT+DIwjdJRuRnYNTMfj4ijgLcCS4CFwB6Z+fBg7R18SIPqWI8vMx8H9gDmAHcCdwPfaTbvDpwYEXcDU4EvdaouSapdRLwE+AKwS2a+GPgecGjLLnsBZ2bmdsAmwLOBN0bEhsBHgK0zcyvgEmDbwdo79oBWoO09vszcuOXny4CXDLDPLZRZn5KkznsN8KPMfAAgM0+KiJuBU5rtnwR2joiDKR9Reyalk/Ib4Bbgxoi4GLg4My+LiPEDtXf2IQ3OK7dIkpbRMsmw+dz181u2nwfsDdwPnAjcCIzLzB7gVZTRvIWUkbtjB2tv/8MYGoNPknQ5sFNE9E003AdoDarXAUdn5rea29sCazRDpLcDd2XmMZRQ3Hqw9g48jiEx+CSpcpl5G/AJ4IcRcQuwC7Bvyy6HAHMj4jbga8BPgE2at6kuAK6PiOuBPYGPDdbesQe0Ap2c1SlJGqUy82zKFbVandtsOxU4dZD7HQUcNdT20cAenySpKgafJKkqBp8kqSoGnySpKgafJKkqBp8kqSp+nEGSRrklS5f9dtLECU9vw3F/N2nihPVWtF9EbAz8knKd5V5gEmUVnfdn5oNDPV9EvBnYKjMPby5i/ePM/FlEnAZ8NTOvX5nHMVwGnySNcpMmTnj6bgefM+LHPffY3YcTpg9l5uZ9NyLieOA44F1DPUBmfo9yAWwolzS7vGmfNYw6VpnBJ0laGZcDx0TEdsB/AZMpyxntk5n3RsTHgPdRFha/LjP3iYg9gB2BecBWwGkR8VbgZOBI4EDgnMycAxARNwCzgEXAV4DpwP8CB2TmTStbuO/xSZKGJSImAv8O/AI4H/hQZr4E+CpwXkSsAXyaEm5bApMiYv2++2fmfwPXA7Oay6X1OYumBxkRzwMmNwF3JnBwZr6UcrHs81elfoNPkjQUz4yIm5vlim4FxgFnAI9k5i8AMvPblPX6pgJXU4LxCOD4zPzNEM5xEfCyiJhGCcCzI2Iq5QLX32zOfS4wNSKmr+wDcahTkjQUT3qPDyAiXjzAfuOANYC3ANsBr6dc/Hr3FZ0gM5dExPeBNwPvAN7YHOvxfu8vbgD8cWUfiD0+SdLKSmB6RGwNEBHvoKzZtwZlBuhtmXk4ZQX2/iG5jIE7X2cBBwELM/P+zHwUuCci3t2cY2fgp6tStMEnSVopmfkEsCtwSkTcDnwI2DUzFwBfB37RTFCZDJze7+4/BL4aES/vd8yrgHV48koRuwOzIuJW4JjmHL2sJIc6JWmUW7J02e+G+dGDIR930sQVx0Bmzgc2HmTbNZSFafu3n0hZgLbVGc0XmflF4ItN+4797vvcfrfv7r/PqjD4JGmUG8qHzFfyuO047KjnUKckqSoGnySpKgafJKkqBp8kqSoGnySpKgafJI1yPUuX/JayHNCIfjXHrU6dc1klaTUyfuKkp99w7Miv3LPlwacN6bOBzXp89wGvzcxLW9rnAzs2n/NbZZ1ao88enyRpKJYCs5sLSLfLqyiXOyMzZ7VrYVp7fJKkoXgIuBQ4nrI00N9ExKcoF5VeA/gR8MnM7I2IA4EDgD8BdwP/k5lHRsSHgPcAawFLKCsxbEuH1ujrePBFxCzK9dz6PJtyUdK1gB2AvzTtR2Xm3A6XJ0ka3EHAbRGxc8uQ5y6UNfe2prx3eBawe3Ndzf2bbUuAK4D/iYi1KSs37JiZj0XE0ZT1/A6IiD2BIzPztojoO+dZlGt1zmldoy8irmrud1NEbAbMBf52p+XpePBl5mnAaQAR8QLgu5RUvxx4ZWY+3OmaJEkrlpl/joi9KEOeL2qadwK2AW5obk8Bfg38M3BhZv4ZICLOA9ZtjrEb8M6ImEkJzpuXc9qLKBfBHmyNvr79pkbE9MxcuKLH0e2hzq8Ah1C6qRsBpzer9M6l9Ph6ulmcJOnJMvOSiOgb8oQyvHlSZp4AEBH/RFly6AMMMI8kIjak9P5OAS4GfgtssZzzjfgafV0LvojYCZiSmd+OiOcA84D9gEeBCylP2uyhHm/69KltqVNjz4wZ7XxvXv35fI9JBwG3AetRAnDPiPg68DhlFO8M4DLK8OQRTfvbmratgXsz88SImAIcDTzQHHd5a/SdTLNGH0BE3BMR787Ms5s1+r4GPHeA+/6Dbvb49gFOAMjMXwFv7dsQEScD72UYwbdw4WJ6eoa/PJP/KeuzYMGijp+z5tdZN57v1dlAr5WepUt+N9SPHgxHz9Ilvxs/cdKw79cy5Pkj4PuU9fOupfTEfgic2Uxu+RJwDbAY+APwGGVR2g9GxJ2U1dp/ArywOXTfGn3v7Xe+qyJiHcooYZ/dm30PpryHOOQ1+roSfBExiTJtdY/m9ouAmX2zdihPxtJu1CZJo834iZPasizRUENvoPX4MvMSyu9qgM82X3/TvH83KTNf0Nz+f8BdmbkY2HmQ83Rkjb5u9fheDPwyM/tmcI4DToqIeZS/DPYGzuxSbZKkVXc/sHWzMnsvpXd4YXdLKroVfM8BHuy7kZm3RsQxwFXARGBOZp7XpdokSasoM58Adut2HQPpSvBl5gXABf3aTgVO7UY9kqR6eMkySVJVDD5JUlUMPklSVQw+SVJVDD5JUlUMPklSVQw+SVJVDD5JUlUMPklSVQw+SVJVDD5JUlUMPklSVQw+SVJVDD5JUlUMPklSVQw+SVJVDD5JUlUMPklSVQw+SVJVDD5JUlUMPklSVQw+SVJVDD5JUlUMPklSVQw+SVJVDD5JUlUMPklSVQw+SVJVDD5JUlUMPklSVSZ046QRcTnwz8DSpmkfYBpwAjAF+FZmfqYbtUmSxraOB19EjANmAs/KzGVN2xQggVcBDwAXRcTrM/PiTtcnSRrbutHji+b7JRExHZgN3Abck5n3AUTE2cDbAYNPkjSiuhF86wKXAQcAE4ErgC8AD7fs8zCwwXAOOn361BEqT2PdjBnTul1CVXy+Ndp0PPgy8xrgmr7bEfEN4GjgypbdxgE9wznuwoWL6enpHXY9/qesz4IFizp+zppfZ914vldnNb9WOqXjszojYoeIeE1L0zhgPvCMlrb1gIc6WZckqQ7dGOr8J+DoiHg5ZajzfcC+wAURsQlwH7AbcHoXapMkjXEd7/Fl5oXARcBNwA3A6c3w5x7AHOBO4G7gO52uTZI09nXlc3yZeRhwWL+2y4CXdKMeSVI9vHKLJKkqBp8kqSoGnySpKgafJKkqBp8kqSoGnySpKgafJKkqBp8kqSoGnySpKgafJKkqBp8kqSoGnySpKgafJKkqBp8kqSoGnySpKgafJKkqBp8kqSoGnySpKgafJKkqBp8kqSoGnySpKgafJKkqBp8kqSoGnySpKgafJKkqBp8kqSoGnySpKhO6XYCksatn2VJmzJjW7TI6btmSJ3jk0SXdLkODMPgktc34CRO54dhZ3S6j47Y8+DTA4ButuhJ8EXEE8I7m5kWZeXBEfBPYAfhL035UZs7tRn2SpLGr48EXETsBrwW2AHqBH0bEW4GtgFdm5sOdrkmSVI9u9PgeBg7KzCUAEXEXsFHzdXpErA/MpfT4erpQnyRpDOt48GXmHX0/R8TzKEOerwB2BPYDHgUuBD4AzO50fZKksa1rk1si4gXARcAnMjOBt7ZsOxl4L8MIvunTp454jRqbapxlqM7zdTZ6dWtyy/bAHOAjmXl+RLwImJmZc5pdxgFLh3PMhQsX09PTO+xafHHWZ8GCRR0/p6+z+qzs68zXSvt1Y3LLhsB3gV0zc17TPA44KSLmAYuBvYEzO12bJGns60aP7+PAZOCEiOhr+ypwDHAVMBGYk5nndaE2SdIY143JLR8GPjzI5lM7WYskqT5eq1OSVBWDT5JUFYNPklQVg0+SVBWDT5JUFYNPklQVg0+SVBWDT5JUFYNPklQVg0+SVBWDT5JUFYNPklQVg0+SVBWDT5JUFYNPklQVg0+SVBWDT5JUFYNPklQVg0+SVBWDT5JUFYNPklQVg0+SVBWDT5JUFYNPklQVg0+SVBWDT5JUFYNPklQVg0+SVBWDT5JUFYNPklSVCd0uoFVE7AZ8BpgInJSZX+5ySZKkMWbU9PgiYn3gc8AOwObA3hGxWXerkiSNNaOpx7cTMC8z/wgQEd8B/h04egX3WwNg/PhxK33ip6271krfd3U2ae3p3S6hK1bltbIqfJ3VZRVeZxsDDwLLRqwYPcm43t7ebtcAQER8GlgrMz/T3J4FbJOZe6/grjsAP2t3fZLUQc8G5ne7iLFqNPX4xgOtKTwO6BnC/X4BvAJ4GPhrG+qSpE57sNsFjGWjKfgepARYn/WAh4ZwvyeAK9tSkSRpzBlNwfdj4MiImAH8BXgbsKJhTkmShmXUzOrMzN8AhwKXAzcD52bmdd2tSpI01oyayS2SJHXCqOnxSZLUCQafJKkqBp8kqSoGnySpKgafJKkqBt8YFxEbR0RvROzcr31+RGzcpbI0BkTEKc01dVvbXhsRv4qIad2qS1oRg68OS4HZ/jLSCPsUsGVEvBkgItYCvgLsmZmLulqZtBx+jm+Ma3p1VwCXAr19F/2OiPnAjsBuwLsp1zm9BDg4M73mqYYkInYCTgc2paykMh44FzgReArwB2CfzLwvIj4GvI9yDd7rMnOf7lSt2tnjq8dBwOv6DXm+HngzsBWwBbAJsG8XatNqKjN/DPwI+CbwWuBI4DRgt8x8KXA8ZbRhDeDTlNfalsCkZg1OqeMMvkpk5p+BvXjykOdrgPMy838zcxnlL/fXdKtGrbYOooTeAcCGwHOB70XEzcAXgOc0owhXU1ZTOQI4vrlModRxBl9FMvMSypDn8U1T/3//cYyuC5drNdD8UfUnyvpxawC/yszNM3NzSu9uh2bXtwAfpLzOfhgRr+pCuZLBV6GDgNcBzwDmAe+KiCkRMQF4P+Ui4dLKuht4akT0LTG2J3Bus+rKncBtmXk45f3kF3epRlXO4KtMy5DnJODC5ut64A7g18DJ3atOq7vMfAJ4O3B8RNxKmczygcxcAHwd+EVE3ABMpgytSx3nrE5JUlXs8UmSqmLwSZKqYvBJkqpi8EmSqmLwSZKqYvBpuSLivRFxXUT8JSIWRcRVEbHrCBz3xxFxxnK2vzsi2jblOCLmRsQVA7Q/0KxmsX6/9hMjIod47Csi4rRh1NIbEe9ezvanRMR+y9m+Y3OMDYZ6TqlmBp8GFRF7A6cApwIvAbYFLgLOi4j3dbO2ETAP2CYiJvY1RMSmlA/2/5ZyCa5WrwB+PMRj/xvwsZEosvFR4OARPJ5UNS9PpeXZB5idmWe0tN0ZEQF8GDizK1WNjHnAFGBzyvUjoYTdjZQP87+OcuFlImJqs99nh3LgzPzjCNc6boSPJ1XN4NPy/BXYPiLWycxHW9o/DqzVd6MZknxPZp49UFtEjKdcmHhvYCowm3JNR1r2fzVwHLAZcDPwg37b1wQ+T1lGaS3gJuCTmfnzZvuRwHbAVcB+lCuD/AzYNzMf6v/AMvOOiPgd8HKeHHyXUi6t9aWIGJ+ZPc0+0FzOLSI2pCy781rgsab9Y33naYZQ783MWc3tNwDHAAHcDpwNnJiZrYG2WXO/7Sg9zqMz8/SI2AP4j5bn9F8y84r+j2dFImIj4Fjg1ZTAv6yp+VfN9jdSgv35lOtufgf4RGY+3qyzdwrwBmAdyr/PIZk5b7h1SKOBQ51anuOAbYCHIuJ7EfHxiNg8Mxdk5vxhHOdQSg/xgOZ4T6WsBQhARGxCCborKT2rr1IWOW3138ArgXdQlraZB1weETNb9vkXypDsTsCuwPaUNeIGczlNqEXEJOBVlOC7FFi3OQ+UYc7rM/PRJgSuoATeyyk9w0nAvOYYTxIRWwDfa75e3Dy2zw9Qy/6UIeXNmn1nR8SzgW9RVjh4kDIMe/VyHs+AImJtyh8ETwV2oTz36wA/iYh1IuJpwP9tans+sDvl+esbXj26qet1zfebgO82z4W02jH4NKjM/DblyvoXUULnOOCmiLgxIl4wlGNExDjKL/XjM/M7mXkXpefXuiTNXsADwEezOBP4cssxNqEE3h6Z+bPM/GVmHkUJyoNajjMeeH9m3tGsRHEW8LLllHcZf+/Nbd98vzozfw/cSvlFDyX4Lm1+fhelx7lHZt6emTc3besDbxvgHB9pjnlYU/dplIDr75TMvKDpgR3RPJYtMvMxYDHw18z8bWYuWc7jGcy7KUH+zsy8MTNvoFxP86nNtg0p4f1gZt7f9OR2Ac5v7r8JsAi4r6nv45T3MV2wWKslg0/LlZlXZ+Y7gOmUyS2fBZ4DXDxQD2cATwOeDtzQcswllPfS+rwQuKkZVuzz85aft2i+XxsRi/u+KD2XTVv2+21mLmq5/SfKL/TBzAM2aIYBXwtc0RIslwI7No9xG/4+sWULYAbwaEsdCylhuCn/6KXANf3arhxgv1/2/ZCZjzQ/TllO7cPxQuCu1vceM/MPlCHdF1KGLi8ALmxmtX4DeGZm9tV0HOVxLGiGYw8A7szMx0eoPqmjDD4NKCI2jIhTI2I9gMz8a2Zel5mHUXpfGzLIsjLNEkd9+j6S0H+CxpJ++yxve9/PL6MMhfZ9bUoZluvzxADlDDoxpOm9zKe8r7YTf+/V0fz8smZbD38PryWUyS+b9/uaCXxpgNMsY2j/zwbqPY3UpJbBAmoNYGlm9mbmrsALgP8CNqIMZZ4KkJlXAhtQhj/vovTgb4mIzUaoPqmjDD4N5jFgFmUySX9/ooTV75vbS4G1W7Y/r++HpmfxG/4+pEgz2WWLlv1vBrbuF5hbtfx8R/P96Zl5b98XZZr/vw7nQQ3gcsp7g1tQ1ojr8zOaoVPgpy09wTuAZwMLW+r4PXAC8KIBjn8rpafcqv/tFVnVzzPeAWwaEU/ta2je1wvKLN2tIuKEzLwzM7+YmTsDhwB7NPseDmyfmXMz84OUf981gDetYl1SVzirUwPKzD9ExLHAMc3kiDmUMHwRZbjzzMz8dbP7NcDeEXEV5RfiiTy59/VF4LMRcTdwHXAg8CxKuAB8rWn7WkQcR+lJHthSy70R8S3g6xGxP2VYcE9gX/7x83bDNQ/4CvBw8/5j3zkfi4grKe+FHd6y/zmUyToXRMSnKb2p/6QMh97BPzoBuLGZdXoOpRd54AD7Lc8iYN3mYyT3L2eIcceI+EO/tttbaj4/Ij5J6UkeCzxCeR9vBrB/RDwOfAOYBvwf4NrmGBsD74mIvYD7gJ0pk2OuRVoN2ePToDLzM5TP8u1MeV/qDuBzlM/v7d2y6weBRym/CL9DWXD0wZbjnEQJj89RZgROA+a2bH8AeA1lRuFNlF/S/9mvnFmUmZ/fpPwyfz3wb5l52So+zHmUj1hcOsC2Synv3f3tg+vNZJOdgf9t7nsV5Q/IVzeTYp4kM2+hhOc7m7r3p8yeHM4klTmUIdlbgTcuZ7+zgIv7fe3SBOXrKH+M/Kyp+1HgFZn5p8y8B3hL87hupfSCH6RM2oES1POAcyl/dHyUMonoJ8N4DNKo4UK0UhtFxNbAE5l5a0vbp4C9MvO53atMqpdDnVJ7vRT4XHMtzjspQ8UfoQzvSuoCg09qr9nAMynDm88AHqJ8RvGYbhYl1cyhTklSVZzcIkmqisEnSaqKwSdJqorBJ0mqisEnSarK/wfJqN1zCq2YMQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 443.225x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Sudden_Weight_Loss', kind='count', hue='class', data = df, height=5)\n",
    "plt.ylabel(' ')\n",
    "plt.xlabel('Sudden Weight Loss', size = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Polyphagia"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     283\n",
       "Yes    237\n",
       "Name: Polyphagia, dtype: int64"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Polyphagia'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Polyphagia  class   \n",
       "No          Negative    0.537102\n",
       "            Positive    0.462898\n",
       "Yes         Positive    0.797468\n",
       "            Negative    0.202532\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Polyphagia')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Symptoms of Polyphagia could be a major symptom of diabetes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 443.225x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Polyphagia', kind='count', hue='class', data = df, height=5)\n",
    "plt.ylabel(' ')\n",
    "plt.xlabel('Polyphagia', size = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Genital Thrush"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     404\n",
       "Yes    116\n",
       "Name: Genital_Thrush, dtype: int64"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Genital_Thrush'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Genital_Thrush  class   \n",
       "No              Positive    0.586634\n",
       "                Negative    0.413366\n",
       "Yes             Positive    0.715517\n",
       "                Negative    0.284483\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Genital_Thrush')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Genital Thrush could be a major symptom as well"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 443.225x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Genital_Thrush', kind='count', hue='class', data = df, height=5)\n",
    "plt.ylabel(' ')\n",
    "plt.xlabel('Genital thrush', size = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Visual Blurring"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     287\n",
       "Yes    233\n",
       "Name: Visual_Blurring, dtype: int64"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Visual_Blurring'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Visual_Blurring  class   \n",
       "No               Positive    0.505226\n",
       "                 Negative    0.494774\n",
       "Yes              Positive    0.751073\n",
       "                 Negative    0.248927\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Visual_Blurring')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Blurred visuals may be a symptom of Diabetes too"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 443.225x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Visual_Blurring', kind='count', hue='class', data = df, height=5)\n",
    "plt.ylabel(' ')\n",
    "plt.xlabel('visual blurring', size = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Itching"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     267\n",
       "Yes    253\n",
       "Name: Itching, dtype: int64"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Itching'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Itching  class   \n",
       "No       Positive    0.621723\n",
       "         Negative    0.378277\n",
       "Yes      Positive    0.608696\n",
       "         Negative    0.391304\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Itching')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 443.225x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Itching', kind='count', hue='class', data = df, height=5)\n",
    "plt.ylabel(' ')\n",
    "plt.xlabel('Itching', size = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Irritability"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     394\n",
       "Yes    126\n",
       "Name: Irritability, dtype: int64"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Irritability'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Irritability  class   \n",
       "No            Positive    0.532995\n",
       "              Negative    0.467005\n",
       "Yes           Positive    0.873016\n",
       "              Negative    0.126984\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Irritability')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 443.225x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Irritability', kind='count', hue='class', data = df, height=5)\n",
    "plt.ylabel(' ')\n",
    "plt.xlabel('Irritability', size = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Delayed Healing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     281\n",
       "Yes    239\n",
       "Name: Delayed_Healing, dtype: int64"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Delayed_Healing'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Delayed_Healing  class   \n",
       "No               Positive    0.594306\n",
       "                 Negative    0.405694\n",
       "Yes              Positive    0.640167\n",
       "                 Negative    0.359833\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Delayed_Healing')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 443.225x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Delayed_Healing', kind='count', hue='class', data = df, height=5)\n",
    "plt.ylabel(' ')\n",
    "plt.xlabel('Delayed Healing', size = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Partial Paresis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     296\n",
       "Yes    224\n",
       "Name: Partial_Paresis, dtype: int64"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Partial_Paresis'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Partial_Paresis  class   \n",
       "No               Negative    0.567568\n",
       "                 Positive    0.432432\n",
       "Yes              Positive    0.857143\n",
       "                 Negative    0.142857\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Partial_Paresis')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 443.225x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Partial_Paresis', kind='count', hue='class', data = df, height=5)\n",
    "plt.ylabel(' ')\n",
    "plt.xlabel('Partial_Paresis', size = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Muscle Stiffness"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     325\n",
       "Yes    195\n",
       "Name: Muscle_Stiffness, dtype: int64"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Muscle_Stiffness'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Muscle_Stiffness  class   \n",
       "No                Positive    0.569231\n",
       "                  Negative    0.430769\n",
       "Yes               Positive    0.692308\n",
       "                  Negative    0.307692\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Muscle_Stiffness')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 443.225x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Muscle_Stiffness', kind='count', hue='class', data = df, height=5)\n",
    "plt.ylabel(' ')\n",
    "plt.xlabel('Muscle_Stiffness', size = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Alopecia"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     341\n",
       "Yes    179\n",
       "Name: Alopecia, dtype: int64"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Alopecia'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Alopecia  class   \n",
       "No        Positive    0.709677\n",
       "          Negative    0.290323\n",
       "Yes       Negative    0.564246\n",
       "          Positive    0.435754\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Alopecia')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Patients without Alopecia have high tendencies to be diabetic "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 443.225x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Alopecia', kind='count', hue='class', data = df, height=5)\n",
    "plt.ylabel(' ')\n",
    "plt.xlabel('Alopecia', size = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Obesity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     432\n",
       "Yes     88\n",
       "Name: Obesity, dtype: int64"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Obesity'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Obesity  class   \n",
       "No       Positive    0.599537\n",
       "         Negative    0.400463\n",
       "Yes      Positive    0.693182\n",
       "         Negative    0.306818\n",
       "Name: class, dtype: float64"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Obesity')['class'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 443.225x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Obesity', kind='count', hue='class', data = df, height=5)\n",
    "plt.ylabel(' ')\n",
    "plt.xlabel('Obesity', size = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Age"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>40</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>58</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>41</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>45</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>60</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Age     class\n",
       "0   40  Positive\n",
       "1   58  Positive\n",
       "2   41  Positive\n",
       "3   45  Positive\n",
       "4   60  Positive"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_age = df[['Age', 'class']]\n",
    "df_age.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Positive    320\n",
       "Negative    200\n",
       "Name: class, dtype: int64"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_age['class'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Maximum Age:  90\n",
      "Minimum Age:  16\n"
     ]
    }
   ],
   "source": [
    "print('Maximum Age: ', df_age[\"Age\"].max())\n",
    "print('Minimum Age: ', df_age[\"Age\"].min())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_age.replace({'Male': 1, 'Female': 0, 'Positive': 1, 'Negative':0, 'Yes':1, 'No':0}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>class</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Age</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>(80, 90]</th>\n",
       "      <td>87.500000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>(60, 70]</th>\n",
       "      <td>65.545455</td>\n",
       "      <td>0.742424</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>(30, 40]</th>\n",
       "      <td>36.829268</td>\n",
       "      <td>0.682927</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>(50, 60]</th>\n",
       "      <td>55.748031</td>\n",
       "      <td>0.614173</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>(40, 50]</th>\n",
       "      <td>46.048276</td>\n",
       "      <td>0.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>(20, 30]</th>\n",
       "      <td>28.840909</td>\n",
       "      <td>0.318182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>(70, 80]</th>\n",
       "      <td>72.700000</td>\n",
       "      <td>0.300000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                Age     class\n",
       "Age                          \n",
       "(80, 90]  87.500000  1.000000\n",
       "(60, 70]  65.545455  0.742424\n",
       "(30, 40]  36.829268  0.682927\n",
       "(50, 60]  55.748031  0.614173\n",
       "(40, 50]  46.048276  0.600000\n",
       "(20, 30]  28.840909  0.318182\n",
       "(70, 80]  72.700000  0.300000"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_age = df_age[['Age', 'class']]\n",
    "df_age\n",
    "\n",
    "bins = np.arange(20, 100, 10)\n",
    "age_grade = df_age.groupby(pd.cut(df_age['Age'], bins)).mean()\n",
    "\n",
    "age_grade = age_grade.sort_values(by='class', ascending=False)\n",
    "age_grade"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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t0ePbmlpqX/xm7nfjHSP4gcAKyunegIAABRO8QMAACic4gcAAFC4motfc3NzFi9enCR59tlnc9FFF+XBBx/ssmAAAAB0jpqK33333Zdtt902Dz30UObOnZt99903F154YQ444IBcf/31XZ0RAACADqip+J133nmZMGFCNt5441x77bXp06dP7rzzzpxyyimZNm1aV2cEAACgA2oqfrNmzcrkyZPTt2/f3Hnnndl+++3Tq1evbLPNNnnxxRe7OiMAAAAdUFPxGzBgQBYsWJD58+fnkUceyTbbbJMkmT17dgYOHNilAQEAAOiYmm7gPmbMmJx00klZZZVVssoqq2S77bbLPffck1NPPTU77LBDV2cEAACgA2o64nfSSSdlk002SZ8+ffKLX/wivXv3ziOPPJLNNtssxx13XFdnBAAAoANqOuLXt2/fZQre4Ycf3iWBAAAA6Fw138fvgQceyOTJk7PjjjvmlVdeyfnnn59rr722K7MBAADQCWoqfnfccUcmT56cNdZYI6+//nra2tpSqVQyderU/P73v+/qjAAAAHRATcXvggsuyDHHHJPTTjst3bt3T5IcccQROfbYY/PrX/+6SwMCAADQMTUVv2eeeSZjxoxZ5vkddtghL7/8cqeHAgAAoPPUVPxWW221Dyx4TzzxRAYPHtzpoQAAAOg8NRW/r3/96zn11FNzxx13JEleeumlXH311TnttNMyadKkLg0IAABAx9R0O4fvfve7mTdvXr7//e9n8eLFOfjgg9OjR48ceOCBOeyww7o6IwAAAB1QU/GrVCo5+uijc/jhh+fZZ59Nz549s84666RPnz5dnQ8AAIAOWm7xe/jhh/PlL3853bt3z8MPP7zUviVLluTJJ59s39500027LiEAAAAdstzi981vfjN33313Bg0alG9+85upVCqpVqvLvK5SqWTWrFldGhIAAIBPbrnF79Zbb83qq6/e/hgAAIBPp+Ve1XPEiBGpVCrtj1988cU8//zzGTFiREaMGJFLLrkkL7/8ckaMGFG3sAAAAHx8Nd3O4dprr813vvOdPPfcc+3PvfPOO5k8eXJmzJjRZeEAAADouJqu6nnhhRfm5JNPzte+9rX2584555xsvvnm+cUvfpHddtutywICAADQMTUd8XvllVey5ZZbLvP8VlttlZdeeqnTQwEAANB5aip+n/vc53LHHXcs8/zdd9+dNdZYo9NDAQAA0HlqOtXz4IMPzoknnpgnn3wyo0aNSpI88cQTuf7663PSSSd1aUAAAAA6pqbit+eee6ZXr1659NJLM2PGjPTs2TPrrbdezjvvvOy0005dnREAAIAOqKn4Jcn48eMzfvz4rswCAABAF6i5+P31r3/NY489liVLlqRarS61b+LEiZ0eDAA+sT6L05qWui/btKA5rX3a6rpm9/RImnvVdU0APn1qKn5XXnllTj311LS2ti6zr1KpKH4ArFBa05JdL6v/rYZ69OiWlpb6Fr+Z+81I9yh+AHy4morfxRdfnL322ivHHHNMBgwY0NWZAAAA6EQ13c7h1VdfzUEHHdTh0nfDDTdk/Pjx2WWXXTJ9+vRl9j/33HPZb7/9sscee+Tggw/OO++806H1AAAAqLH4jRo1Kk8//XSHFpozZ07OO++8XH755bn22mtzxRVX5JlnnmnfX61W873vfS+HHHJIrr/++my44Ya58MILO7QmAAAANZ7qOWnSpJx66qn5y1/+krXXXju9ei39WYJaPuN3zz33ZMstt8zAgQOTJOPGjcvMmTNzxBFHJEn+8pe/pF+/fhkzZkyS5NBDD8277777sb4ZAAAAllVT8Zs6dWqSfOARuFov7jJ37twMGTKkfXvo0KF57LHH2rdfeumlDB48OCeccEJmzZqV9dZbLz/60Y9qiddu0KD+H+v1naFpQXN69KjpwGmna8S63bt1y5AhK8/nPBs1X7Ptet67ZVuZ5ruyzfbt5rezpHVJ3ddtWtCc9Kv7sunZvWcG9hlY/4VXQivT+2hlY7bvq6n4PfXUUx1eqK2tLZVKpX27Wq0utd3S0pL7778/v/3tbzNq1Kj89Kc/zdlnn52zzz675jXeeGN+2tqqH/3CTtTap63uV3BLGnPluCRpbWtLU9O8uq/bKI2Yr9nWh/du2Vam+a58s1200lyxNXn/qq1N81ae+TbKkCEDVqr30cpkZZptt26VDz0Q9rH+WvL111/Pn//85zQ3N+eNN974WEGGDx+epqam9u2mpqYMHTq0fXvIkCFZe+21M2rUqCTJhAkTljoiCAAAwCdTU/FbvHhxjj/++Gy77bY58MAD09TUlJNOOikHHHBA5tX4t1Bbb7117r333rz55ptZuHBhbrnllvbP8yXJJptskjfffLP96OJtt92WL33pS5/gWwIAAOC/qqn4XXDBBXniiSdy+eWXp3fv3kmSyZMn57XXXsu5555b00LDhg3LkUcemf333z977rlnJkyYkNGjR+eQQw7J448/nj59+uTnP/95TjzxxOy+++7585//nOOOO+6Tf2cAAAAkqfEzfjNmzMjpp5+eTTfdtP25TTbZJKeddlqOOuqo/MM//ENNi02cOHGZC8FMmzat/fGXv/zlXH311TV9LQAAAGpT0xG/uXPnZs0111zm+cGDB9d8qicAAACNUVPx23DDDXPrrbcu8/yVV16ZkSNHdnooAAAAOk9Np3r+8Ic/zOTJk/Nv//ZvaWlpybRp0/Lss8/m0Ucf/cB7+wEAALDiqOmI3+abb57f/e536dmzZ9Zee+08/vjjWXPNNXPNNddk66237uqMAAAAdEBNR/yS90/3rPUKngAAAKw4llv8Lrjggpq/yBFHHNEpYQAAAOh8yy1+119//VLbL7/8cnr37p3Pfe5z6dmzZ1544YUsWrQoo0ePVvwAAABWYMstfrfcckv742nTpuX+++/Pueeem4EDByZJ5s+fnxNOOCEjRozo+pQAAAB8YjVd3OWf//mfc8wxx7SXviTp379/pkyZkquuuqrLwgEAANBxNRW/JHn99deXee7ll19Or169OjUQAAAAnaumq3ruvvvuOeGEE3LUUUdlo402SpI8/PDD+dnPfpavfe1rXRoQAACAjqmp+B133HFpbm7O8ccfn9bW1lSr1fTq1Svf+MY3MmXKlK7OCAAAQAfUVPx69eqVM888MyeccEKef/75VCqVrLfeeunXr19X5wMAAKCDar6Be3Nzc1544YW0tLSkWq3mqaeeat+36aabdkk4AAAAOq6m4venP/0pxx9/fObPn59qtbrUvkqlklmzZnVJOAAAADqupuJ3wQUXZPPNN8///J//MwMGDOjqTAAAAHSimorfCy+8kJ/85CdZf/31uzoPAAAAnaym+/itt956mTNnTldnAQAAoAvUdMTv0EMPzSmnnJLJkydn7bXXXuam7S7uAgAAsOKqqfj95736Tj755GX2ubgLAADAiq2m4nfrrbd2dQ4AAAC6SE3Fb8SIEe2PZ8+eneHDh6daraZnz55dFgwAAIDOUdPFXarVan7+859n4403zi677JK//vWvOeaYY3LCCSdkyZIlXZ0RAACADqip+F188cW5+uqrc9ppp7Vf2GX8+PG5/fbb89Of/rRLAwIAANAxNRW/q6++OieddFImTpyYSqWSJNl5551z5pln5sYbb+zSgAAAAHRMTcVv9uzZH3jz9nXXXTdvvvlmp4cCAACg89RU/NZdd908+OCDyzx/8803Z9111+30UAAAAHSemq7q+f3vfz9HH310nnnmmbS2tub666/Piy++mBtvvDHnnHNOV2cEAACgA5Z7xO9v//Zv89ZbbyVJdtppp/z0pz/NI488ku7du+c3v/lNZs+enf/9v/93dt9997qFBQAA4ONb7hG/V155JW1tbe3bY8eOzdixY+sSCgAAgM5T02f8AAAA+PT60M/4Pf744/nMZz7zkV9k00037bRAAAAAdK4PLX7f+973Uq1WP/QLVCqVzJo1q1NDAQAA0Hk+tPhdeeWVWX311euVBQAAgC6w3OJXqVSy5pprZtCgQfXMAwAAQCdb7sVdPuoUTwAAAD4dllv8Jk2alN69e9czCwAAAF1guad6nnXWWfXMAQAAQBdxHz8AAIDCKX4AAACFU/wAAAAKV3Pxa25uzuLFi5Mkzz77bC666KI8+OCDXRYMAACAzlFT8bvvvvuy7bbb5qGHHsrcuXOz77775sILL8wBBxyQ66+/vqszAgAA0AE1Fb/zzjsvEyZMyMYbb5xrr702ffr0yZ133plTTjkl06ZN6+qMAAAAdEBNxW/WrFmZPHly+vbtmzvvvDPbb799evXqlW222SYvvvhiV2cEAACgA2oqfgMGDMiCBQsyf/78PPLII9lmm22SJLNnz87AgQO7NCAAAAAds9wbuP9XY8aMyUknnZRVVlklq6yySrbbbrvcc889OfXUU7PDDjt0dUYAAAA6oKYjfieddFI22WST9OnTJ7/4xS/Su3fvPPLII9lss81y3HHHdXVGAAAAOqCmI359+/ZdpuAdfvjhXRIIAACAzlXzffweeOCBTJ48OTvuuGNeeeWVnH/++bn22mu7MhsAAACdoKbid8cdd2Ty5MlZY4018vrrr6etrS2VSiVTp07N73//+67OCAAAQAfUVPwuuOCCHHPMMTnttNPSvXv3JMkRRxyRY489Nr/+9a+7NCAAAAAdU1Pxe+aZZzJmzJhlnt9hhx3y8ssvd3ooAAAAOk9NxW+11Vb7wIL3xBNPZPDgwZ0eCgAAgM5TU/H7+te/nlNPPTV33HFHkuSll17K1VdfndNOOy2TJk3q0oAAAAB0TE23c/jud7+befPm5fvf/34WL16cgw8+OD169MiBBx6Yww47rKszAgAA0AE1Fb9KpZKjjz46hx9+eJ599tn07Nkz66yzTvr06ZM33ngjgwYN6uqcAAAAfEI1neq54YYb5s0330y/fv0yatSojBw5Mn369Mmrr76anXbaqaszAgAA0AHLPeJ300035c4770ySVKvVnH766endu/dSr5k9e3ZWWWWVrk0IAABAhyy3+G266aa5+uqrU61WkyRz585Nz5492/dXKpUMHDgw5557btenBAAA4BNbbvEbPnx4+83Zjz/++EydOjX9+/evWzAAAAA6R02f8TvrrLPSv3//PProo7nmmmsyf/78PPPMM2lpaenqfAAAAHRQTVf1/M9bOdx3332pVCr5yle+kp/85Cd58cUXc/HFF2f48OFdnRMAAIBPqKYjfueee25aWlpyxx13pE+fPkmSqVOnZsCAAfnxj3/cpQEBAADomJqK3x133JFjjjkmw4YNa3/us5/9bH70ox/l3nvv7bJwAAAAdFxNxe+dd97JqquuuszzvXv3zqJFizo9FAAAAJ2npuK32Wab5aqrrlrqudbW1lx44YXZeOONuyQYAAAAnaOmi7sce+yx2W+//fLnP/85ixcvzumnn55nn3027777bi6++OKuzggAAEAH1FT8vvjFL+b666/P5ZdfntVXXz09e/bMhAkTsu+++2bw4MFdnREAAIAOqKn4JcmwYcNy5JFHZv78+enZs2d69+7dlbkAAADoJDV9xi9JLr744my//fb5yle+ko033jg777xzrrnmmq7MBgAAQCeo6Yjfr371q0ybNi3f/va3M2rUqFSr1Tz00EM57bTT8u677+bb3/52F8cEAADgk6qp+F122WU544wzMm7cuPbntt9++3z+85/PT3/6U8UPAABgBVbTqZ7vvfdevvCFLyzz/KhRo/L22293eigAAAA6T03Fb+LEiZk2bVpaWlqWev7SSy/Nbrvt1iXBAAAA6BzLPdXzoIMOan+8ZMmSPPDAA7nvvvsyatSodOvWLbNmzcrs2bOz00471SUoAAAAn8xyi9+wYcOW2l5rrbWW2t50002z6aabdk0qAAAAOs1yi99ZZ51VzxwAAAB0kZpv4P7UU0/l6aefTltbW5KkWq1m8eLFefzxx3P66ad3WUAAAAA6pqbid9FFF+Xcc89Nt27dUq1WU6lU0tbWlkqlkq9+9atdnREAAIAOqOmqntOnT8/hhx+exx9/PKuvvnr+9V//NTfddFO++MUvZsyYMV2dEQAAgA6oqfjNnTs3e+65Z7p3756RI0fmsccey3rrrZfjjjsuV199dVdnBAAAoANqKn79+/fPokWLkiTrrLNOnn766STJ2muvnVdffbXr0gEAANBhNRW/LbbYIv/4j/+YuXPnZtSoUbn55pszb9683HbbbRk4cGBXZwQAAKADaip+xx57bGbPnp2bbrop48ePT7du3bLFFlvkjDPOyAEHHFDzYjfccEPGjx+fXXbZJdOnT1/u626//fbsuOOONX9dAAAAlq+mq3qOGDEiN9xwQxYtWpRevXrld7/7Xe6///6sttpqGT16dE0LzZkzJ+edd16uueaa9OrVK9/4xjfy1a9+Neuvv/5Sr3v99dfz4x//+ON/JwAAAHyg5R7xmzNnzlKP58yZk7fffjtz5szJu+++m5EjR2bYsGFLve7D3HPPPdlyyy0zcODA9OvXL+PGjcvMmTOXed2JJ56YI4444hN8KwAAAHyQ5R7x23777XPXXXdl0KBBGTt2bCqVyjKv+c97+s2aNesjF5o7d26GDBnSvj106NA89thjS73m0ksvzUYbbZQvf/nLH+d7AAAA4EMst/j95je/yaqrrtr++IOK38fxnzd8/0//WRr/09NPP51bbrkll1xySV577bVPtMagQf07lPGTaFrQnB49avqoZKdrxLrdu3XLkCED6r5uozRqvmbb9bx3y7Yyzdds68d7t2x+zuUy2/ctt/htscUW7Y+/+tWvdnih4cOH58EHH2zfbmpqytChQ9u3Z86cmaampuy9995ZsmRJ5s6dm29+85u5/PLLa17jjTfmp62t2uGsH0drn7a0tLTVdc3k/V8+jVi3ta0tTU3z6r5uozRivmZbH967ZVuZ5mu29eG9W7YhQwb4ORdqZZptt26VDz0Q9qEXd2lpacnvf//73HjjjXn66aczf/78fOYzn8lGG22UiRMnZo899qj5SODWW2+d888/P2+++Wb69u2bW265Jaeddlr7/ilTpmTKlClJktmzZ2f//ff/WKUPAACAD7bc4rdgwYIccsgheeSRR7LZZptl/Pjx+cxnPpP58+fnySefzHHHHZdrrrkmF154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jI4y27KZb9nMt1xmWzbzLZfZfjS3c1jB9e7dO6+99toyz7/66qvp1atXAxLRWcy2bOZbNvMtl9mWzXzLZbYfzcVdVnDHHXdcvvWtb2WdddbJkCFDUqlUMnfu3Lzwwgs566yzGh2PDjDbsplv2cy3XGZbNvMtl9l+NKd6fgosWrQojz32WObOnZu2trYMHz48X/7yl/3tRQHMtmzmWzbzLZfZls18y/XfZ7vGGmtk9OjRZvsfup9yyimnNDoEH+7222/PjTfemIceeijPPvts3njjjQwcODDDhw9vdDQ64PTTT89mm22W9dZbL1/84hezwQYbZMSIEenevXujo9FJevTokREjRrTP97LLLsvYsWMbHYtOcu+99+ZLX/pSRo0alSeffDJ333133n777Wy44YaNjkYHPPbYYxkxYkRGjBiRN954Iw888EBefvnlrLrqqhk2bFij49EJZs+encGDB2eTTTbJo48+mvvvvz/Nzc35whe+0OhodNADDzyQXr16ZcyYMbnrrrvyxz/+MbNnz87GG2/s/6/iiN8K71e/+lX+7d/+Ldttt11uu+22bL755unZs2euvvrqHHjggfn617/e6Ih8QptvvnkGDRqUH/zgB9lll10aHYdOdvzxxy/z3G233ZYdd9wxSZx28il3xhlnZNasWTnvvPNy+eWX59FHH81OO+2U//t//2/WWmutnHjiiY2OyCc0adKk/OEPf8j06dPzL//yL9l7772TJH/4wx/yta99Lfvuu2+DE9IRl1xySS677LK0tbVlyy23zF//+tfsvPPOue2227Lpppvm8MMPb3REPqFzzjknDz74YFpaWrLWWmulUqlkr732ym233ZbW1tacfvrpjY7YeFVWaHvssUe1ra2tWq1Wq83NzdX99tuvWq1Wq++++2511113bWQ0Oujv/u7vqv/v//2/6re+9a3qPvvsU73xxhurCxcubHQsOsnZZ59d3XLLLauXXHJJ9Zprrqlec8011e233779MZ9u48ePr7a0tFSr1Wp1zz33rC5atKharVarLS0t/tv8KbfnnntWq9X3f/+++eab7c/PmzevOm7cuEbFopNMmDCh2tzcXJ09e3Z14403rjY3N1er1Wp10aJF1YkTJzY4HR0xYcKEamtra3XhwoXVr371q9XFixdXq9Vqta2tzWz/g6t6ruAWLVqUhQsXJkmam5vz9ttvJ0n69eu3zOVq+XSpVCpZf/3189vf/jZHHnlkbr755vzt3/5tvvWtb+UHP/hBo+PRQccee2z+6Z/+KTfddFPWXHPNTJo0KauuumomTZqUSZMmNToeHdSnT5+88cYbSZLhw4fnvffeS5IsXLgwPXq4btqnWUtLS9ra2jJw4MClPhfUq1cvv3cL0NbWll69emXEiBE56KCD0rt37/Z9ra2tDUxGR1Wr1cybNy9vvfVWFi5cmPnz5yd5//+flyxZ0uB0Kwa/nVZwe+21V/7+7/8+2267be66667stddeefXVV3PYYYdlwoQJjY5HB1T/y1nWW2+9dbbeeussWbIk//7v/56XX365gcnoLFtttVU23HDDnHzyybn99tv9T0VBDj/88Oyzzz7Zfffds9Zaa2W//fbLVlttlbvuuiuTJ09udDw6YODAgdl+++2TJKeddlrOPvvs3HvvvTn33HOz6667NjYcHbbLLrtk3333zaWXXprvf//7SZKnnnoqJ554YnbbbbcGp6MjDjnkkOyyyy6pVqs5+uijc9BBB2WrrbbKvffe237K9srOZ/w+Be699948+eST2WijjbLVVltlwYIFmT17djbYYINGR6MDrrrqqnzta19rdAzq5KqrrsqMGTPy61//utFR6CQvv/xy/vSnP+XFF19Ma2trBg8enB122CGjR49udDQ6wXPPPZd33303G2+8cR566KHMmzevvRDy6fbAAw/kK1/5Svv2c889l5dfftnFtwrQ3Nyc1tbWrLLKKvn3f//33HXXXRk5cmS22WabRkdbISh+AAAAhXOyOgAAQOEUPwAAgMIpfgAAAIXrfsopp5zS6BB8MnvuuWeeeOKJtLW1Zb311mt0HDqR2ZbNfMtmvuUy27KZb7nM9n0u7vIpNnfu3AwdOjQLFy5M3759Gx2HTmS2ZTPfsplvucy2bOZbLrN9n+L3KdDW1paHH344c+bMSaVSydChQzN69OilbizLp5PZls18y2a+5TLbsplvucz2w7mB+wru4YcfzvHHH58111wzgwcPTrVazeuvv54XX3wxZ555ZrbaaqtGR+QTMtuymW/ZzLdcZls28y2X2dagygpt9913rz7//PPLPP/CCy9UJ0yYUP9AdBqzLZv5ls18y2W2ZTPfcpntR3NVzxVca2tr1llnnWWe/+xnP5uqs3Q/1cy2bOZbNvMtl9mWzXzLZbYfzameK7jtt98+hx56aMaPH58hQ4akUqmkqakpN9xwQ8aMGdPoeHSA2ZbNfMtmvuUy27J92Hy32267RsejA7x3P5qLu3wKzJw5M3fccUfmzp2barWa4cOHZ8yYMdl1110bHY0O+u+zHTZsWMaOHWu2hTDfst188825/fbbzbdA/322fu+WxX+by2W2H07x+5R59dVX8/jjj2fDDTfM5z73uUbHoRNUq9VUKpXMnz8/zz//fNZdd93079+/0bHoZO+8805mz56d9dZbb6W+lHSJlixZkmeffTY9e/bM5z//+UbHoQvcf//92WKLLRodg05SrVazYMGCZX7XNjU1ZciQIQ1KRUf95S9/yZe+9KVGx1ih+YzfCu7ee+/N2LFjM27cuPzpT3/KN7/5zdx000056KCDctNNNzU6Hh1w9913Z+zYsXnuuedy//33Z9ddd80//MM/ZNddd80dd9zR6Hh00FNPPZVvfOMbOfTQQ3P33Xdnt912y8knn5zx48fnkUceaXQ8Omjy5MlJkqeffjrjx4/PcccdlyOPPDITJ07M008/3eB0dMQDDzywzD8/+tGP8uCDD+aBBx5odDw66L777st2222XHXfcMd/+9rczZ86c9n3f+c53GpiMjtp7771z8skn57333mt0lBWWz/it4M4555xMmzYt7733Xvbff/9cf/31WWeddfLmm2/mwAMPzPjx4xsdkU/o7LPPzkUXXZTPf/7zmTp1ai666KJssMEGefnll3PYYYdl7NixjY5IB5x88sk54ogj2ud5xRVXZOTIkXnmmWcyderUXHHFFY2OSAe88cYbSZIzzzwzJ554Yvv79f7778/UqVNz1VVXNTIeHXDCCSfk3XffzQYbbNB+QYi5c+fmZz/7WSqVSi699NIGJ6QjzjnnnFx22WVZe+2188///M/Zd999M3369AwdOtQFQD7lvvCFL2TQoEGZMGFCJk+enH322cf9+/4bxW8F19LSki9+8Ytpa2vLgAED2q9WtPrqq6e1tbWx4eiQHj16ZP3110+SdO/ePRtssEESV58qRXNzc/uFAi677LKMHDkySbL++uunubm5kdHoRG+//fZSf0mzxRZbmO+n3B/+8IecdtppGTBgQI455pj06tUre+65Zy677LJGR6MTtLW1Zd11103y/hG+Xr165eCDD87vfve7VCqVBqejI3r06JEpU6ZkwoQJ+eUvf5mf//znGTNmTDbbbLMMHz482267baMjNpxTPVdwG2ywQX7wgx/k8MMPz2c/+9n8+Mc/zjPPPJNf/vKXPuP3KbfZZpvlhz/8YZ5++unstttu+cd//Mc89dRT+ad/+ifnqBdg9dVXz5VXXpkkmTFjRpLkvffeyyWXXJLBgwc3Mhqd4MUXX8zJJ5+cvn375l/+5V+SvP85zosuushnhD7l+vfvnx//+MfZdNNNs//+++fJJ59UCAoyePDgXH755Zk3b16S5Nvf/na22267HHjggXnnnXcanI7OsN566+Xcc8/NjBkzsvXWW2fWrFn+4uY/uLjLCm7JkiW57rrr0tbWlkmTJuWCCy7IrbfempEjR+b444/PoEGDGh2RT2jJkiWZNm1aZsyYkZdeeimtra0ZMmRIdthhhxx11FEu8PIpN3fu3Jx33nk566yz2p+744478oc//CFTp05VDj7lXn311TzxxBN5/PHH07t37xxxxBH57W9/236q57BhwxodkU7w6quv5sQTT8zzzz+ff/3Xf210HDpBU1NTzjnnnOyyyy7Zeeed25+/5JJL8otf/CL3339/A9PREd/73vfyy1/+stExVmiK3wpu0aJF6d27d4dfw4rHbMtmvmUz33L997lVq9U899xzS12x1Ww/vbx3y2W2H82pniu4H/7wh7nyyiszf/78ZfbNnz8/06dPz1FHHdWAZHSU2ZbNfMtmvuX677OtVCrtpc9sP/28d8tlth/NEb8VXFtbW373u9/lsssuy2c+85kMHz48PXr0yOzZs/P2229n//33zze+8Y306OE6PZ82Zls28y2b+ZbLbMtmvuUy24+m+H2KPPXUU3nhhRdSqVSy9tprt18lkE8/sy2b+ZbNfMtltmUz33KZ7QdT/AAAAArnM34AAACFU/wAAAAKp/gBUISmpqZstNFGGT9+fN3WXLRoUS688MJMmjQpm266aTbZZJPsvffemT59etra2jp9veuuuy4bbLBBp39dAMq38l7WBoCiXHfddfnsZz+bZ599Ng8++GD+v/buPSSqbYHj+Dc9HuqPpJdIlo4ViWFZTCISGhQ9JYvsJZG9EC1So3+MIoOE3sYYQUkP7IGhQj6y11BBQWWYYoyDYDKKZoaUZqWUo+b5Q9z3TI97zz33dO91zu8DG/bsvdde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\n",
      "text/plain": [
       "<Figure size 1080x648 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set(rc={'figure.figsize' :(15,9)})\n",
    "age_grade.drop(columns=['Age']).plot(kind='bar', color='green', alpha=0.80)\n",
    "plt.ylabel('Diabetes Tendencies', size=15)\n",
    "plt.xlabel('Age Grade', size=15)\n",
    "plt.legend(' ')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Patients with old age greater than 80 years have high tendency to be diabetic. 60<Age grade<70 also had a high tendency\n",
    "#### Followed by 30<Age grade<40 which may be as a result of lifestyle.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x432 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set(rc={'figure.figsize':(15,6)})\n",
    "ax=sns.boxplot(x='class', y='Age', data=df)\n",
    "ax.set_xticklabels(ax.get_xticklabels(),rotation=45)\n",
    "plt.ylabel('Age', size=15)\n",
    "plt.xlabel('Class', size=15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Apply label encoding to the dataset since its a binary classification"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use label encoding since its a binary classification\n",
    "df.replace({'Male': 1, 'Female': 0, 'Positive': 1, 'Negative':0, 'Yes':1, 'No':0}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Polyuria</th>\n",
       "      <th>Polydipsia</th>\n",
       "      <th>Sudden_Weight_Loss</th>\n",
       "      <th>Weakness</th>\n",
       "      <th>Polyphagia</th>\n",
       "      <th>Genital_Thrush</th>\n",
       "      <th>Visual_Blurring</th>\n",
       "      <th>Itching</th>\n",
       "      <th>Irritability</th>\n",
       "      <th>Delayed_Healing</th>\n",
       "      <th>Partial_Paresis</th>\n",
       "      <th>Muscle_Stiffness</th>\n",
       "      <th>Alopecia</th>\n",
       "      <th>Obesity</th>\n",
       "      <th>class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>40</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>58</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>45</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Age  Gender  Polyuria  Polydipsia  Sudden_Weight_Loss  Weakness  \\\n",
       "0   40       1         0           1                   0         1   \n",
       "1   58       1         0           0                   0         1   \n",
       "2   41       1         1           0                   0         1   \n",
       "3   45       1         0           0                   1         1   \n",
       "4   60       1         1           1                   1         1   \n",
       "\n",
       "   Polyphagia  Genital_Thrush  Visual_Blurring  Itching  Irritability  \\\n",
       "0           0               0                0        1             0   \n",
       "1           0               0                1        0             0   \n",
       "2           1               0                0        1             0   \n",
       "3           1               1                0        1             0   \n",
       "4           1               0                1        1             1   \n",
       "\n",
       "   Delayed_Healing  Partial_Paresis  Muscle_Stiffness  Alopecia  Obesity  \\\n",
       "0                1                0                 1         1        1   \n",
       "1                0                1                 0         1        0   \n",
       "2                1                0                 1         1        0   \n",
       "3                1                0                 0         0        0   \n",
       "4                1                1                 1         1        1   \n",
       "\n",
       "   class  \n",
       "0      1  \n",
       "1      1  \n",
       "2      1  \n",
       "3      1  \n",
       "4      1  "
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Polyuria</th>\n",
       "      <th>Polydipsia</th>\n",
       "      <th>Sudden_Weight_Loss</th>\n",
       "      <th>Weakness</th>\n",
       "      <th>Polyphagia</th>\n",
       "      <th>Genital_Thrush</th>\n",
       "      <th>Visual_Blurring</th>\n",
       "      <th>Itching</th>\n",
       "      <th>Irritability</th>\n",
       "      <th>Delayed_Healing</th>\n",
       "      <th>Partial_Paresis</th>\n",
       "      <th>Muscle_Stiffness</th>\n",
       "      <th>Alopecia</th>\n",
       "      <th>Obesity</th>\n",
       "      <th>class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Age</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.062872</td>\n",
       "      <td>0.199781</td>\n",
       "      <td>0.137382</td>\n",
       "      <td>0.064808</td>\n",
       "      <td>0.224596</td>\n",
       "      <td>0.315577</td>\n",
       "      <td>0.096519</td>\n",
       "      <td>0.402729</td>\n",
       "      <td>0.296559</td>\n",
       "      <td>0.201625</td>\n",
       "      <td>0.257501</td>\n",
       "      <td>0.232742</td>\n",
       "      <td>0.307703</td>\n",
       "      <td>0.321691</td>\n",
       "      <td>0.140458</td>\n",
       "      <td>0.108679</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <td>0.062872</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.268894</td>\n",
       "      <td>-0.312262</td>\n",
       "      <td>-0.281840</td>\n",
       "      <td>-0.124490</td>\n",
       "      <td>-0.219968</td>\n",
       "      <td>0.208961</td>\n",
       "      <td>-0.208092</td>\n",
       "      <td>-0.052496</td>\n",
       "      <td>-0.013735</td>\n",
       "      <td>-0.101978</td>\n",
       "      <td>-0.332288</td>\n",
       "      <td>-0.090542</td>\n",
       "      <td>0.327871</td>\n",
       "      <td>-0.005396</td>\n",
       "      <td>-0.449233</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polyuria</th>\n",
       "      <td>0.199781</td>\n",
       "      <td>-0.268894</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.598609</td>\n",
       "      <td>0.447207</td>\n",
       "      <td>0.263000</td>\n",
       "      <td>0.373873</td>\n",
       "      <td>0.087273</td>\n",
       "      <td>0.235095</td>\n",
       "      <td>0.088289</td>\n",
       "      <td>0.237740</td>\n",
       "      <td>0.149873</td>\n",
       "      <td>0.441664</td>\n",
       "      <td>0.152938</td>\n",
       "      <td>-0.144192</td>\n",
       "      <td>0.126567</td>\n",
       "      <td>0.665922</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polydipsia</th>\n",
       "      <td>0.137382</td>\n",
       "      <td>-0.312262</td>\n",
       "      <td>0.598609</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.405965</td>\n",
       "      <td>0.332453</td>\n",
       "      <td>0.316839</td>\n",
       "      <td>0.028081</td>\n",
       "      <td>0.331250</td>\n",
       "      <td>0.128716</td>\n",
       "      <td>0.203446</td>\n",
       "      <td>0.115691</td>\n",
       "      <td>0.442249</td>\n",
       "      <td>0.180723</td>\n",
       "      <td>-0.310964</td>\n",
       "      <td>0.098691</td>\n",
       "      <td>0.648734</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sudden_Weight_Loss</th>\n",
       "      <td>0.064808</td>\n",
       "      <td>-0.281840</td>\n",
       "      <td>0.447207</td>\n",
       "      <td>0.405965</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.282884</td>\n",
       "      <td>0.243511</td>\n",
       "      <td>0.089858</td>\n",
       "      <td>0.068754</td>\n",
       "      <td>-0.004516</td>\n",
       "      <td>0.140340</td>\n",
       "      <td>0.088140</td>\n",
       "      <td>0.264014</td>\n",
       "      <td>0.109756</td>\n",
       "      <td>-0.202727</td>\n",
       "      <td>0.169294</td>\n",
       "      <td>0.436568</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Weakness</th>\n",
       "      <td>0.224596</td>\n",
       "      <td>-0.124490</td>\n",
       "      <td>0.263000</td>\n",
       "      <td>0.332453</td>\n",
       "      <td>0.282884</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.180266</td>\n",
       "      <td>0.027780</td>\n",
       "      <td>0.301043</td>\n",
       "      <td>0.309440</td>\n",
       "      <td>0.146698</td>\n",
       "      <td>0.335507</td>\n",
       "      <td>0.272982</td>\n",
       "      <td>0.263164</td>\n",
       "      <td>0.090490</td>\n",
       "      <td>0.045665</td>\n",
       "      <td>0.243275</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polyphagia</th>\n",
       "      <td>0.315577</td>\n",
       "      <td>-0.219968</td>\n",
       "      <td>0.373873</td>\n",
       "      <td>0.316839</td>\n",
       "      <td>0.243511</td>\n",
       "      <td>0.180266</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.063712</td>\n",
       "      <td>0.293545</td>\n",
       "      <td>0.144390</td>\n",
       "      <td>0.239466</td>\n",
       "      <td>0.263980</td>\n",
       "      <td>0.373569</td>\n",
       "      <td>0.320031</td>\n",
       "      <td>-0.053498</td>\n",
       "      <td>0.029785</td>\n",
       "      <td>0.342504</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Genital_Thrush</th>\n",
       "      <td>0.096519</td>\n",
       "      <td>0.208961</td>\n",
       "      <td>0.087273</td>\n",
       "      <td>0.028081</td>\n",
       "      <td>0.089858</td>\n",
       "      <td>0.027780</td>\n",
       "      <td>-0.063712</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.148408</td>\n",
       "      <td>0.125336</td>\n",
       "      <td>0.160551</td>\n",
       "      <td>0.136111</td>\n",
       "      <td>-0.195612</td>\n",
       "      <td>-0.100188</td>\n",
       "      <td>0.204847</td>\n",
       "      <td>0.053828</td>\n",
       "      <td>0.110288</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Visual_Blurring</th>\n",
       "      <td>0.402729</td>\n",
       "      <td>-0.208092</td>\n",
       "      <td>0.235095</td>\n",
       "      <td>0.331250</td>\n",
       "      <td>0.068754</td>\n",
       "      <td>0.301043</td>\n",
       "      <td>0.293545</td>\n",
       "      <td>-0.148408</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.291191</td>\n",
       "      <td>0.077095</td>\n",
       "      <td>0.177767</td>\n",
       "      <td>0.364156</td>\n",
       "      <td>0.412369</td>\n",
       "      <td>0.014604</td>\n",
       "      <td>0.109005</td>\n",
       "      <td>0.251300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Itching</th>\n",
       "      <td>0.296559</td>\n",
       "      <td>-0.052496</td>\n",
       "      <td>0.088289</td>\n",
       "      <td>0.128716</td>\n",
       "      <td>-0.004516</td>\n",
       "      <td>0.309440</td>\n",
       "      <td>0.144390</td>\n",
       "      <td>0.125336</td>\n",
       "      <td>0.291191</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.114006</td>\n",
       "      <td>0.453316</td>\n",
       "      <td>0.116669</td>\n",
       "      <td>0.215575</td>\n",
       "      <td>0.266506</td>\n",
       "      <td>0.001894</td>\n",
       "      <td>-0.013384</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Irritability</th>\n",
       "      <td>0.201625</td>\n",
       "      <td>-0.013735</td>\n",
       "      <td>0.237740</td>\n",
       "      <td>0.203446</td>\n",
       "      <td>0.140340</td>\n",
       "      <td>0.146698</td>\n",
       "      <td>0.239466</td>\n",
       "      <td>0.160551</td>\n",
       "      <td>0.077095</td>\n",
       "      <td>0.114006</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.126877</td>\n",
       "      <td>0.151571</td>\n",
       "      <td>0.201637</td>\n",
       "      <td>0.043708</td>\n",
       "      <td>0.127801</td>\n",
       "      <td>0.299467</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Delayed_Healing</th>\n",
       "      <td>0.257501</td>\n",
       "      <td>-0.101978</td>\n",
       "      <td>0.149873</td>\n",
       "      <td>0.115691</td>\n",
       "      <td>0.088140</td>\n",
       "      <td>0.335507</td>\n",
       "      <td>0.263980</td>\n",
       "      <td>0.136111</td>\n",
       "      <td>0.177767</td>\n",
       "      <td>0.453316</td>\n",
       "      <td>0.126877</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.187382</td>\n",
       "      <td>0.250078</td>\n",
       "      <td>0.290179</td>\n",
       "      <td>-0.066339</td>\n",
       "      <td>0.046980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Partial_Paresis</th>\n",
       "      <td>0.232742</td>\n",
       "      <td>-0.332288</td>\n",
       "      <td>0.441664</td>\n",
       "      <td>0.442249</td>\n",
       "      <td>0.264014</td>\n",
       "      <td>0.272982</td>\n",
       "      <td>0.373569</td>\n",
       "      <td>-0.195612</td>\n",
       "      <td>0.364156</td>\n",
       "      <td>0.116669</td>\n",
       "      <td>0.151571</td>\n",
       "      <td>0.187382</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.232634</td>\n",
       "      <td>-0.221576</td>\n",
       "      <td>-0.009401</td>\n",
       "      <td>0.432288</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Muscle_Stiffness</th>\n",
       "      <td>0.307703</td>\n",
       "      <td>-0.090542</td>\n",
       "      <td>0.152938</td>\n",
       "      <td>0.180723</td>\n",
       "      <td>0.109756</td>\n",
       "      <td>0.263164</td>\n",
       "      <td>0.320031</td>\n",
       "      <td>-0.100188</td>\n",
       "      <td>0.412369</td>\n",
       "      <td>0.215575</td>\n",
       "      <td>0.201637</td>\n",
       "      <td>0.250078</td>\n",
       "      <td>0.232634</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.040758</td>\n",
       "      <td>0.158910</td>\n",
       "      <td>0.122474</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Alopecia</th>\n",
       "      <td>0.321691</td>\n",
       "      <td>0.327871</td>\n",
       "      <td>-0.144192</td>\n",
       "      <td>-0.310964</td>\n",
       "      <td>-0.202727</td>\n",
       "      <td>0.090490</td>\n",
       "      <td>-0.053498</td>\n",
       "      <td>0.204847</td>\n",
       "      <td>0.014604</td>\n",
       "      <td>0.266506</td>\n",
       "      <td>0.043708</td>\n",
       "      <td>0.290179</td>\n",
       "      <td>-0.221576</td>\n",
       "      <td>0.040758</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.029229</td>\n",
       "      <td>-0.267512</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Obesity</th>\n",
       "      <td>0.140458</td>\n",
       "      <td>-0.005396</td>\n",
       "      <td>0.126567</td>\n",
       "      <td>0.098691</td>\n",
       "      <td>0.169294</td>\n",
       "      <td>0.045665</td>\n",
       "      <td>0.029785</td>\n",
       "      <td>0.053828</td>\n",
       "      <td>0.109005</td>\n",
       "      <td>0.001894</td>\n",
       "      <td>0.127801</td>\n",
       "      <td>-0.066339</td>\n",
       "      <td>-0.009401</td>\n",
       "      <td>0.158910</td>\n",
       "      <td>0.029229</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.072173</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>class</th>\n",
       "      <td>0.108679</td>\n",
       "      <td>-0.449233</td>\n",
       "      <td>0.665922</td>\n",
       "      <td>0.648734</td>\n",
       "      <td>0.436568</td>\n",
       "      <td>0.243275</td>\n",
       "      <td>0.342504</td>\n",
       "      <td>0.110288</td>\n",
       "      <td>0.251300</td>\n",
       "      <td>-0.013384</td>\n",
       "      <td>0.299467</td>\n",
       "      <td>0.046980</td>\n",
       "      <td>0.432288</td>\n",
       "      <td>0.122474</td>\n",
       "      <td>-0.267512</td>\n",
       "      <td>0.072173</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         Age    Gender  Polyuria  Polydipsia  \\\n",
       "Age                 1.000000  0.062872  0.199781    0.137382   \n",
       "Gender              0.062872  1.000000 -0.268894   -0.312262   \n",
       "Polyuria            0.199781 -0.268894  1.000000    0.598609   \n",
       "Polydipsia          0.137382 -0.312262  0.598609    1.000000   \n",
       "Sudden_Weight_Loss  0.064808 -0.281840  0.447207    0.405965   \n",
       "Weakness            0.224596 -0.124490  0.263000    0.332453   \n",
       "Polyphagia          0.315577 -0.219968  0.373873    0.316839   \n",
       "Genital_Thrush      0.096519  0.208961  0.087273    0.028081   \n",
       "Visual_Blurring     0.402729 -0.208092  0.235095    0.331250   \n",
       "Itching             0.296559 -0.052496  0.088289    0.128716   \n",
       "Irritability        0.201625 -0.013735  0.237740    0.203446   \n",
       "Delayed_Healing     0.257501 -0.101978  0.149873    0.115691   \n",
       "Partial_Paresis     0.232742 -0.332288  0.441664    0.442249   \n",
       "Muscle_Stiffness    0.307703 -0.090542  0.152938    0.180723   \n",
       "Alopecia            0.321691  0.327871 -0.144192   -0.310964   \n",
       "Obesity             0.140458 -0.005396  0.126567    0.098691   \n",
       "class               0.108679 -0.449233  0.665922    0.648734   \n",
       "\n",
       "                    Sudden_Weight_Loss  Weakness  Polyphagia  Genital_Thrush  \\\n",
       "Age                           0.064808  0.224596    0.315577        0.096519   \n",
       "Gender                       -0.281840 -0.124490   -0.219968        0.208961   \n",
       "Polyuria                      0.447207  0.263000    0.373873        0.087273   \n",
       "Polydipsia                    0.405965  0.332453    0.316839        0.028081   \n",
       "Sudden_Weight_Loss            1.000000  0.282884    0.243511        0.089858   \n",
       "Weakness                      0.282884  1.000000    0.180266        0.027780   \n",
       "Polyphagia                    0.243511  0.180266    1.000000       -0.063712   \n",
       "Genital_Thrush                0.089858  0.027780   -0.063712        1.000000   \n",
       "Visual_Blurring               0.068754  0.301043    0.293545       -0.148408   \n",
       "Itching                      -0.004516  0.309440    0.144390        0.125336   \n",
       "Irritability                  0.140340  0.146698    0.239466        0.160551   \n",
       "Delayed_Healing               0.088140  0.335507    0.263980        0.136111   \n",
       "Partial_Paresis               0.264014  0.272982    0.373569       -0.195612   \n",
       "Muscle_Stiffness              0.109756  0.263164    0.320031       -0.100188   \n",
       "Alopecia                     -0.202727  0.090490   -0.053498        0.204847   \n",
       "Obesity                       0.169294  0.045665    0.029785        0.053828   \n",
       "class                         0.436568  0.243275    0.342504        0.110288   \n",
       "\n",
       "                    Visual_Blurring   Itching  Irritability  Delayed_Healing  \\\n",
       "Age                        0.402729  0.296559      0.201625         0.257501   \n",
       "Gender                    -0.208092 -0.052496     -0.013735        -0.101978   \n",
       "Polyuria                   0.235095  0.088289      0.237740         0.149873   \n",
       "Polydipsia                 0.331250  0.128716      0.203446         0.115691   \n",
       "Sudden_Weight_Loss         0.068754 -0.004516      0.140340         0.088140   \n",
       "Weakness                   0.301043  0.309440      0.146698         0.335507   \n",
       "Polyphagia                 0.293545  0.144390      0.239466         0.263980   \n",
       "Genital_Thrush            -0.148408  0.125336      0.160551         0.136111   \n",
       "Visual_Blurring            1.000000  0.291191      0.077095         0.177767   \n",
       "Itching                    0.291191  1.000000      0.114006         0.453316   \n",
       "Irritability               0.077095  0.114006      1.000000         0.126877   \n",
       "Delayed_Healing            0.177767  0.453316      0.126877         1.000000   \n",
       "Partial_Paresis            0.364156  0.116669      0.151571         0.187382   \n",
       "Muscle_Stiffness           0.412369  0.215575      0.201637         0.250078   \n",
       "Alopecia                   0.014604  0.266506      0.043708         0.290179   \n",
       "Obesity                    0.109005  0.001894      0.127801        -0.066339   \n",
       "class                      0.251300 -0.013384      0.299467         0.046980   \n",
       "\n",
       "                    Partial_Paresis  Muscle_Stiffness  Alopecia   Obesity  \\\n",
       "Age                        0.232742          0.307703  0.321691  0.140458   \n",
       "Gender                    -0.332288         -0.090542  0.327871 -0.005396   \n",
       "Polyuria                   0.441664          0.152938 -0.144192  0.126567   \n",
       "Polydipsia                 0.442249          0.180723 -0.310964  0.098691   \n",
       "Sudden_Weight_Loss         0.264014          0.109756 -0.202727  0.169294   \n",
       "Weakness                   0.272982          0.263164  0.090490  0.045665   \n",
       "Polyphagia                 0.373569          0.320031 -0.053498  0.029785   \n",
       "Genital_Thrush            -0.195612         -0.100188  0.204847  0.053828   \n",
       "Visual_Blurring            0.364156          0.412369  0.014604  0.109005   \n",
       "Itching                    0.116669          0.215575  0.266506  0.001894   \n",
       "Irritability               0.151571          0.201637  0.043708  0.127801   \n",
       "Delayed_Healing            0.187382          0.250078  0.290179 -0.066339   \n",
       "Partial_Paresis            1.000000          0.232634 -0.221576 -0.009401   \n",
       "Muscle_Stiffness           0.232634          1.000000  0.040758  0.158910   \n",
       "Alopecia                  -0.221576          0.040758  1.000000  0.029229   \n",
       "Obesity                   -0.009401          0.158910  0.029229  1.000000   \n",
       "class                      0.432288          0.122474 -0.267512  0.072173   \n",
       "\n",
       "                       class  \n",
       "Age                 0.108679  \n",
       "Gender             -0.449233  \n",
       "Polyuria            0.665922  \n",
       "Polydipsia          0.648734  \n",
       "Sudden_Weight_Loss  0.436568  \n",
       "Weakness            0.243275  \n",
       "Polyphagia          0.342504  \n",
       "Genital_Thrush      0.110288  \n",
       "Visual_Blurring     0.251300  \n",
       "Itching            -0.013384  \n",
       "Irritability        0.299467  \n",
       "Delayed_Healing     0.046980  \n",
       "Partial_Paresis     0.432288  \n",
       "Muscle_Stiffness    0.122474  \n",
       "Alopecia           -0.267512  \n",
       "Obesity             0.072173  \n",
       "class               1.000000  "
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1296x720 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(18, 10))\n",
    "sns.heatmap(df.corr(), annot=True, vmin=-1, vmax=1)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Validation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_features = df.iloc[:, :16].values\n",
    "\n",
    "df_target = df.iloc[:, -1].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.6613669 ,  0.76509206, -0.99233705, ...,  1.29099445,\n",
       "         1.38022749,  2.21564684],\n",
       "       [ 0.82136224,  0.76509206, -0.99233705, ..., -0.77459667,\n",
       "         1.38022749, -0.45133547],\n",
       "       [-0.57899306,  0.76509206,  1.00772212, ...,  1.29099445,\n",
       "         1.38022749, -0.45133547],\n",
       "       ...,\n",
       "       [ 0.82136224, -1.30703226,  1.00772212, ...,  1.29099445,\n",
       "        -0.72451824,  2.21564684],\n",
       "       [-1.32035762, -1.30703226, -0.99233705, ..., -0.77459667,\n",
       "         1.38022749, -0.45133547],\n",
       "       [-0.49661921,  0.76509206, -0.99233705, ..., -0.77459667,\n",
       "        -0.72451824, -0.45133547]])"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn import preprocessing\n",
    "\n",
    "scaler = preprocessing.StandardScaler()\n",
    "df_features_scaled = scaler.fit_transform(df_features)\n",
    "df_features_scaled"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "(training_inputs,\n",
    " testing_inputs,\n",
    " training_classes,\n",
    " testing_classes) = train_test_split(df_features_scaled, df_target, train_size=0.8, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.40949304,  0.76509206,  1.00772212, ..., -0.77459667,\n",
       "         1.38022749, -0.45133547],\n",
       "       [-0.57899306,  0.76509206,  1.00772212, ..., -0.77459667,\n",
       "        -0.72451824,  2.21564684],\n",
       "       [ 0.49186688,  0.76509206, -0.99233705, ..., -0.77459667,\n",
       "         1.38022749, -0.45133547],\n",
       "       ...,\n",
       "       [-0.6613669 , -1.30703226,  1.00772212, ...,  1.29099445,\n",
       "        -0.72451824, -0.45133547],\n",
       "       [ 0.7389884 ,  0.76509206,  1.00772212, ..., -0.77459667,\n",
       "        -0.72451824, -0.45133547],\n",
       "       [ 3.45732515, -1.30703226, -0.99233705, ...,  1.29099445,\n",
       "         1.38022749, -0.45133547]])"
      ]
     },
     "execution_count": 148,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "training_inputs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9519230769230769\n"
     ]
    }
   ],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "\n",
    "clf= DecisionTreeClassifier(random_state=42)\n",
    "\n",
    "# Train the classifier on the training set\n",
    "clf.fit(training_inputs, training_classes)\n",
    "# Measure the accuracy\n",
    "print(clf.score(testing_inputs, testing_classes))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9903846153846154\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "\n",
    "clf = RandomForestClassifier(n_estimators=10, random_state=1)\n",
    "\n",
    "# Train the classifier on the training set\n",
    "clf.fit(training_inputs, training_classes)\n",
    "# Measure the accuracy\n",
    "print(clf.score(testing_inputs, testing_classes))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9903846153846154"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn import svm\n",
    "\n",
    "C = 1.0\n",
    "svc = svm.SVC(kernel='rbf', C=C)\n",
    "\n",
    "# Train the classifier on the training set\n",
    "svc.fit(training_inputs, training_classes)\n",
    "# Measure the accuracy\n",
    "svc.score(testing_inputs, testing_classes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.875"
      ]
     },
     "execution_count": 152,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn import neighbors\n",
    "\n",
    "clf = neighbors.KNeighborsClassifier(n_neighbors=10)\n",
    "\n",
    "# Train the classifier on the training set\n",
    "clf.fit(training_inputs, training_classes)\n",
    "# Measure the accuracy\n",
    "clf.score(testing_inputs, testing_classes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9230769230769231"
      ]
     },
     "execution_count": 153,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "clf = LogisticRegression()\n",
    "\n",
    "# Train the classifier on the training set\n",
    "clf.fit(training_inputs, training_classes)\n",
    "# Measure the accuracy\n",
    "clf.score(testing_inputs, testing_classes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9903846153846154"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import ExtraTreesClassifier\n",
    "clf =ExtraTreesClassifier(n_estimators=100, random_state=42)\n",
    "\n",
    "# Train the classifier on the training set\n",
    "clf.fit(training_inputs, training_classes)\n",
    "# Measure the accuracy\n",
    "clf.score(testing_inputs, testing_classes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9903846153846154"
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "clf = RandomForestClassifier(n_estimators=100, random_state=42)\n",
    "\n",
    "# Train the classifier on the training set\n",
    "clf.fit(training_inputs, training_classes)\n",
    "# Measure the accuracy\n",
    "clf.score(testing_inputs, testing_classes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1,\n",
       "       1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1,\n",
       "       0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,\n",
       "       0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,\n",
       "       0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0], dtype=int64)"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred = clf.predict(testing_inputs)\n",
    "y_pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[33,  0],\n",
       "       [ 1, 70]], dtype=int64)"
      ]
     },
     "execution_count": 157,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(testing_classes, y_pred)\n",
    "cm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(104,)"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testing_inputs[:, 0].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1,\n",
       "       1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1,\n",
       "       0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,\n",
       "       0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,\n",
       "       0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0], dtype=int64)"
      ]
     },
     "execution_count": 159,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1,\n",
       "       1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1,\n",
       "       0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,\n",
       "       0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,\n",
       "       0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0], dtype=int64)"
      ]
     },
     "execution_count": 160,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testing_classes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Regression Models needed to predict Diabetic Tendencies (Probabilities)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import important metric libraries\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.metrics import mean_squared_error\n",
    "from sklearn.metrics import mean_absolute_error\n",
    "from sklearn.metrics import r2_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Extra Tree Regression. mean_squared_error:  0.14582325972533694\n",
      "Extra Tree Regression. mean_absolute_error:  0.03278846153846154\n",
      "Extra Tree Regression. r2_score:  0.9018369611609048\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import ExtraTreesRegressor\n",
    "et =ExtraTreesRegressor(random_state=1)\n",
    "\n",
    "# Train the classifier on the training set\n",
    "et.fit(training_inputs, training_classes)\n",
    "\n",
    "# Predict the model\n",
    "pred_et = et.predict(testing_inputs)\n",
    "\n",
    "#mean square error\n",
    "#pred_dt = regressor.predict(X_pre_test)\n",
    "et_mse = mean_squared_error(testing_classes, pred_et)\n",
    "et_rmse = np.sqrt(et_mse)\n",
    "\n",
    "#mean absolute error\n",
    "et_mae = mean_absolute_error(testing_classes, pred_et)\n",
    "\n",
    "\n",
    "# r2 score\n",
    "et_r2 = r2_score(testing_classes, pred_et)\n",
    "\n",
    "\n",
    "print('Extra Tree Regression. mean_squared_error: ', et_rmse)\n",
    "print('Extra Tree Regression. mean_absolute_error: ', et_mae)\n",
    "print('Extra Tree Regression. r2_score: ', et_r2)\n",
    "\n",
    "#pred_et"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random Forest Regression. mean_squared_error:  0.1384217357320624\n",
      "Random Forest Regression. mean_absolute_error:  0.051250000000000004\n",
      "Random Forest Regression. r2_score:  0.911548954332053\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestRegressor\n",
    "\n",
    "rand = RandomForestRegressor(random_state=1)\n",
    "\n",
    "# Train the classifier on the training set\n",
    "rand.fit(training_inputs, training_classes)\n",
    "\n",
    "# Predict the model\n",
    "pred_rf = rand.predict(testing_inputs)\n",
    "\n",
    "#mean square error\n",
    "#pred_dt = regressor.predict(X_pre_test)\n",
    "rd_mse = mean_squared_error(testing_classes, pred_rf)\n",
    "rd_rmse = np.sqrt(rd_mse)\n",
    "\n",
    "#mean absolute error\n",
    "rd_mae = mean_absolute_error(testing_classes, pred_rf)\n",
    "\n",
    "\n",
    "# r2 score\n",
    "rd_r2 = r2_score(testing_classes, pred_rf)\n",
    "\n",
    "\n",
    "print('Random Forest Regression. mean_squared_error: ', rd_rmse)\n",
    "print('Random Forest Regression. mean_absolute_error: ', rd_mae)\n",
    "print('Random Forest Regression. r2_score: ', rd_r2)\n",
    "\n",
    "#pred_rf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SVR. mean_squared_error:  0.1608643639317102\n",
      "SVR. mean_absolute_error:  0.1108467372710835\n",
      "SVR. r2_score:  0.8805423183118265\n"
     ]
    }
   ],
   "source": [
    "from sklearn import svm\n",
    "\n",
    "C = 1.0\n",
    "svr = svm.SVR(kernel='rbf', C=C)\n",
    "\n",
    "# Train the classifier on the training set\n",
    "svr.fit(training_inputs, training_classes)\n",
    "# Measure the accuracy\n",
    "svr.score(testing_inputs, testing_classes)\n",
    "\n",
    "# Predict the model\n",
    "pred_svr = svr.predict(testing_inputs)\n",
    "\n",
    "#mean square error\n",
    "#pred_dt = regressor.predict(X_pre_test)\n",
    "svr_mse = mean_squared_error(testing_classes, pred_svr)\n",
    "svr_rmse = np.sqrt(svr_mse)\n",
    "\n",
    "#mean absolute error\n",
    "svr_mae = mean_absolute_error(testing_classes, pred_svr)\n",
    "\n",
    "\n",
    "# r2 score\n",
    "svr_r2 = r2_score(testing_classes, pred_svr)\n",
    "\n",
    "\n",
    "print('SVR. mean_squared_error: ', svr_rmse)\n",
    "print('SVR. mean_absolute_error: ', svr_mae)\n",
    "print('SVR. r2_score: ', svr_r2)\n",
    "\n",
    "#pred_svr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gradient Boost Regression. mean_squared_error:  0.17670144957569445\n",
      "Gradient Boost Regression. mean_absolute_error:  0.10313917109890401\n",
      "Gradient Boost Regression. r2_score:  0.8558632867760338\n"
     ]
    }
   ],
   "source": [
    "# Fitting gradient boosting regression model to the dataset\n",
    "\n",
    "from sklearn.ensemble import GradientBoostingRegressor\n",
    "\n",
    "grad = GradientBoostingRegressor(random_state=1)\n",
    "\n",
    "# Train the classifier on the training set\n",
    "grad.fit(training_inputs, training_classes)\n",
    "\n",
    "# Predict the model\n",
    "pred_gd = grad.predict(testing_inputs)\n",
    "\n",
    "#mean square error\n",
    "#pred_dt = regressor.predict(X_pre_test)\n",
    "gd_mse = mean_squared_error(testing_classes, pred_gd)\n",
    "gd_rmse = np.sqrt(gd_mse)\n",
    "\n",
    "#mean absolute error\n",
    "gd_mae = mean_absolute_error(testing_classes, pred_gd)\n",
    "\n",
    "\n",
    "# r2 score\n",
    "gd_r2 = r2_score(testing_classes, pred_gd)\n",
    "\n",
    "\n",
    "print('Gradient Boost Regression. mean_squared_error: ', gd_rmse)\n",
    "print('Gradient Boost Regression. mean_absolute_error: ', gd_mae)\n",
    "print('Gradient Boost Regression. r2_score: ', gd_r2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Fine-tune your model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "metadata": {},
   "outputs": [],
   "source": [
    "def display_scores(scores):\n",
    "    print(\"Scores:\", scores)\n",
    "    print(\"Mean:\", scores.mean())\n",
    "    print(\"Standard deviation:\", scores.std())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Scores: [0.22496154 0.18299853 0.16643895 0.12611808 0.34526745 0.02201398\n",
      " 0.34200765 0.05408327 0.04881283 0.09159904]\n",
      "Mean: 0.16043013122893915\n",
      "Standard deviation: 0.10985768728406688\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import cross_val_score\n",
    "\n",
    "forest_reg = RandomForestRegressor(n_estimators=100, random_state=42)\n",
    "\n",
    "forest_scores = cross_val_score(forest_reg, df_features_scaled, df_target,\n",
    "                                scoring=\"neg_mean_squared_error\", cv=10)\n",
    "forest_rmse_scores = np.sqrt(-forest_scores)\n",
    "display_scores(forest_rmse_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomizedSearchCV(cv=5,\n",
       "                   estimator=RandomForestRegressor(max_features=2,\n",
       "                                                   random_state=1),\n",
       "                   param_distributions={'n_estimators': <scipy.stats._distn_infrastructure.rv_frozen object at 0x000000979985F550>},\n",
       "                   random_state=1, scoring='neg_mean_squared_error')"
      ]
     },
     "execution_count": 192,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.model_selection import RandomizedSearchCV\n",
    "from scipy.stats import randint\n",
    "\n",
    "param_distribs = {\n",
    "        'n_estimators': randint(low=1, high=600),\n",
    "    \n",
    "    }\n",
    "\n",
    "forest_reg = RandomForestRegressor(max_features=2, random_state=1)\n",
    "rnd_search = RandomizedSearchCV(forest_reg, param_distributions=param_distribs,\n",
    "                                n_iter=10, cv=5, scoring='neg_mean_squared_error', random_state=1)\n",
    "rnd_search.fit(training_inputs, training_classes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.1503013656164835 {'n_estimators': 38}\n",
      "0.1478892624944955 {'n_estimators': 236}\n",
      "0.1491239345333303 {'n_estimators': 73}\n",
      "0.14868859856464225 {'n_estimators': 145}\n",
      "0.1503515114638367 {'n_estimators': 130}\n",
      "0.14756057088335953 {'n_estimators': 584}\n",
      "0.14793369982108787 {'n_estimators': 509}\n",
      "0.14823473186031394 {'n_estimators': 391}\n",
      "0.1470473817548751 {'n_estimators': 282}\n",
      "0.14832255511871678 {'n_estimators': 179}\n"
     ]
    }
   ],
   "source": [
    "cvres = rnd_search.cv_results_\n",
    "for mean_score, params in zip(cvres[\"mean_test_score\"], cvres[\"params\"]):\n",
    "    print(np.sqrt(-mean_score), params)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestRegressor(max_features=2, n_estimators=282, random_state=1)"
      ]
     },
     "execution_count": 194,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "best_estimator = rnd_search.best_estimator_\n",
    "best_estimator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.1105972 , 0.09289278, 0.18085389, 0.14804938, 0.07128732,\n",
       "       0.02964048, 0.03635925, 0.02656926, 0.03713344, 0.03508044,\n",
       "       0.04289252, 0.03407672, 0.05868003, 0.03156112, 0.04626079,\n",
       "       0.01806538])"
      ]
     },
     "execution_count": 195,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "feature_importances = rnd_search.best_estimator_.feature_importances_\n",
    "feature_importances"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAyAAAAHUCAYAAADC7ExOAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAgAElEQVR4nOzdfXzP9f7H8cf3wjYinDU6iKSaq6hTmosSs9Ns2KXGZC5SUoZ+dRYOoUIukqIi1YnkkGLmalNELtJIhBPScXEMzZSL2QXb9/v9/eF2vqed6Gzs8/lu3z3vf9nn8/1+Pq/vM7ntuc/785nF5XK5EBERERERMYHV0wOIiIiIiEjFoQIiIiIiIiKmUQERERERERHTqICIiIiIiIhpVEBERERERMQ0KiAiIiIiImIau6cHEPOdOZOD06mnLxvB378qP/98wdNjeC3layzlazxlbCzlayzlayxvy9dqtVCz5g1X3KcCUgE5nS4VEAMpW2MpX2MpX+MpY2MpX2MpX2NVlHy1BEtEREREREyjAiIiIiIiIqZRAREREREREdOogIiIiIiIiGl0E3oF5PTNw+FyenoMj7Bhh3wfT48hIiIiUmGpgFRAfZP7cSL7pKfH8Ii0hFRsqICIiIiIeIqWYImIiIiIiGlUQERERERExDQqINchJyeHF198kT//+c9ERETQq1cvtm7dCkBCQgLp6enXfY7IyEgAdu/ezdSpU6/7eCIiIiIinqR7QK6Ry+Vi0KBBNGnShFWrVuHj48P333/PwIEDmTZtWqmdJyUlBYAff/yRn3/+udSOKyIiIiLiCboCco22bdvGiRMnGDlyJD4+l29qbtq0KU899RRvv/02AIsXLyYqKoqoqCj31ZCcnByGDx9OTEwMkZGRrFy5EoD9+/cTFxdHTEwM8fHxHDlyBIDAwEDOnz/PjBkz+OKLL5g1axa9evViy5YtwOUi9PDDD5OZmWlyAiIiIiIiJacrINdoz549NG/eHIvFUmR7q1atmDZtGs2aNaNKlSosW7aM/fv3M3DgQNauXcusWbNo1qwZkydP5sKFC/Ts2ZOWLVsyb948+vfvT1hYGMnJyezatYtbb70VgBtvvJGhQ4eybds2nnrqKWrVqkVKSgrt2rXjm2++oX79+tSuXbvYs9tsVuz2itk9bVYrAQHVDD2H0cev6JSvsZSv8ZSxsZSvsZSvsSpKviog18hiseBwOH6zvaCgwF1KunfvDkDjxo3x9/fn0KFDfPXVV+Tn57NkyRIAcnNzOXjwIA899BAvvfQSmzZtIjg4mI4dO1713GFhYUyfPp3c3FySk5OJiYkp0ewOh5PCwor5e0AcTidZWdmGHT8goJqhx6/olK+xlK/xlLGxlK+xlK+xvC1fq9WCv3/VK+5TAblGLVu2ZP78+RQUFFCpUiX39l27dtG8eXOcTic2m8293el0YrfbcTqdTJ06lWbNmgFw+vRpqlevTqVKlbjnnntYv349c+fOZcOGDYwfP/6K565SpQrt27dnzZo1fP3114wdO9bYDysiIiIiUkoq5jqcUnDfffdx++23M3HiRAoKCgDYu3cvs2bN4umnnwZgxYoVwOXlWjk5OTRo0IDWrVuzcOFCAE6dOkVERAQnT57kmWeeYc+ePfTs2ZNhw4bx/fffFzmfzWajsLDQ/XVsbCzTp0/nwQcfxNfX14yPLCIiIiJy3VRArsObb76Jj48PXbt2JTw8nAkTJjB16lSCgoKAy8uroqKiGDt2LNOmTaNSpUokJiaSn59P165d6du3L0lJSdSvX59BgwYxa9YsoqOjmTp1KuPGjStyrhYtWvDdd9/x6quvAnDvvfdisViIjY01+2OLiIiIiFwzi8vlcnl6CCkZl8vFDz/8wPDhw1m2bFmJ3x8+vwsnsk8aMFnZl5aQii2/imHH97b1m2WN8jWW8jWeMjaW8jWW8jWWt+Wre0C8zLx583jvvfd44403PD2KiIiIiEiJqICUQ/369aNfv37X/P550XNxuCrmU7Bs+isvIiIi4lH6bqwCsl6sDE6tvBMRERER8+kmdBERERERMY0KiIiIiIiImEYFRERERERETKMCIiIiIiIiplEBERERERER06iAiIiIiIiIaVRARERERETENCogIiIiIiJiGhUQERERERExjQqIiIiIiIiYRgVERERERERMY/f0AGI+p28eDpfT02N4paycfBx+v83Whh3yfTwwkYiIiEjZogJSAfVN7seJ7JOeHsMr2e1WCgt/W0DSElKxoQIiIiIioiVYIiIiIiJiGhUQERERERExjQqIiIiIiIiYplwUkMLCQmbNmkVYWBjh4eGEhoYye/ZsXC5XiY+1bt063njjDQBmzJjBN99887uvHzFiBEuXLr3q/iVLlhAZGUlkZCTNmzcnPDycyMhIXnzxRdLT00lISCjxjP9LcHAwGRkZpX5cERERERGjlYub0F988UVOnz7Nxx9/zI033siFCxcYPHgw1apV49FHHy3RsTp16kSnTp0A2L59O0FBQdc1W2xsLLGxscDlYjBnzhzq1asHQHp6+nUdW0RERETE25T5AvLTTz+xfPlyNm7cyI033ghA1apVGTNmDD/++COnT59mzJgx/PTTT1gsFp577jnatm3LzJkzyczM5OjRoxw/fpxHHnmEp556iqVLl7Jt2zZat27N3r17GT16NG+++Sbnzp1j+vTp5Ofnc/78eUaOHElISMh1z//LL7/wxBNP8K9//YuGDRsyY8YMTp06xeOPP07NmjXx8/OjW7dubNu2jUmTJgGQkJBAYmIiDRo04C9/+Qu5ublYrVZGjx7N3XffDcBbb73Fvn37yMvLY8qUKbRs2bLYM9lsVuz2cnHxq1y6UrY2q5WAgGoemMb7KEdjKV/jKWNjKV9jKV9jVZR8y3wB2b17N40aNaJ69epFtjdq1IhGjRrxf//3f8TGxtKpUydOnTpFr169WLZsGQAHDhxgwYIFZGdnExISUuRqSVRUFEuWLCExMZHAwECGDh3K+PHjadSoEVu3bmXixImlUkBOnDjB7NmzqVu3LnFxcXz11VfcfvvtHD58mPfee4969epddYnXp59+SocOHXj88cfZuHEjO3bscBeQ22+/nVdeeYWPPvqI999/nxkzZhR7JofDecVHxcr1u9pjeB1OJ1lZ2R6YyLsEBFRTjgZSvsZTxsZSvsZSvsbytnytVgv+/lWvuK/MFxAAi8Xi/nNaWhqzZs3C6XTi4+NDRkYGhw4dcn8DXlhYyLFjxwAICgrCx8cHf39/atSoQXb21f+jTp06lfXr15OWlsZ3331HTk5OqczeuHFjbrnlFuByaTpz5gwA/v7+7qVaV9OmTRuGDBnCvn37eOihh+jdu7d737/L0e23386aNWtKZVYREREREaOV+XU4zZs355///CcXLlwAoHPnzqSkpDBr1izOnDmD0+lk3rx5pKSkkJKSwuLFi7nzzjsB8PX1dR/HYrH87k3rvXr1Yvfu3TRv3pxBgwaV2vx2+3863q9n8PPzu+psBQUFANx7772sWrWKBx54gNWrVxeZy2azud8rIiIiIlJelPkCUqdOHSIiIhg+fDjnz58HLl/l2LBhA1arldatW/P3v/8dgB9//JFu3bqRl5dXrGPbbDYcDgdnz57lyJEjDBs2jPbt27Nu3TocDodhn+m/1axZk3/+85+4XC6OHTvGgQMHAJgyZQrLly8nOjqaMWPG8P3335s2k4iIiIiIEcrFEqxx48bxwQcf0KdPHxwOBzk5OQQFBfHuu+9SpUoVxowZQ7du3YDL37RXrXrl9Wb/7cEHH2Ts2LFMnjyZ7t2706VLF+x2O61btyY/P5/c3FwjP5Zb27ZtWbJkCZ07d6Zhw4bce++9wOWb0Z977jmWLl2KzWZj8uTJpswjIiIiImIUi+tafpmGlGvh87twIvukp8fwSle7CT0tIRVbfhUPTORdvO0GvbJG+RpPGRtL+RpL+RrL2/It9zehe1p+fj49evS44r6hQ4e6f69IeTEvei4Ol56CZQSb1YrD+dtsbfpfTURERARQASkWPz8/UlJSPD1GqbFerAxOXfgygrf99EJERESktJX5m9BFRERERMR7qICIiIiIiIhpVEBERERERMQ0KiAiIiIiImIaFRARERERETGNCoiIiIiIiJhGBUREREREREyjAiIiIiIiIqZRAREREREREdOogIiIiIiIiGlUQERERERExDQqICIiIiIiYhq7pwcQ8zl983C4nJ4ewytl5eTj8Lv2bG3YId+nFCcSERERKVtUQCqgvsn9OJF90tNjeCW73Uph4bUXkLSEVGyogIiIiIj30hIsERERERExTYUvIP3792ft2rXurydPnsw999zDpUuX3NseeOABMjIySnTc4ODgEr9HRERERMTbVfgC0rp1a3bs2OH++quvvuLuu+92bzt69ChVqlShXr16nhpRRERERMRrVPh7QNq0acPEiRMByMzMxMfHh9DQUDZv3kybNm345ptvaNeuHcuWLWPevHk4nU6aNWvG2LFj8fX15aOPPiIlJYW8vDwqVarEtGnTuO2229zHP3z4ME8++SRTpkzh0KFDbNq0iXPnznHs2DHatWvHuHHjAJgzZw6pqak4HA4eeOABkpKSyMnJ4dlnn+X06dMADB48mE6dOvHBBx+QnJyM1WqlRYsWvPTSS6bnJiIiIiJyLSp8AWnWrBn/+te/uHjxIps3b6Zdu3a0a9eOxMREkpKS+Oabb6hfvz6LFy9m0aJF+Pr6Mm3aNN5//336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5/XXXwdg6NChJSofIiIiIiKe5JVXQOT3ZV3IwuHSjexGsFmtODz4kAAbdsj38dj5jeZtPx0qa5Sv8ZSxsZSvsZSvsbwt3wp3BUR+n/ViZXCqdxrB2/7xEBERESltZeopWCIiIiIi4t1UQERERERExDQqICIiIiIiYhoVEBERERERMY0KiIiIiIiImEYFRERERERETKMCIiIiIiIiplEBERERERER06iAiIiIiIiIaVRARERERETENCogIiIiIiJiGrunBxDzOX3zcLicnh7DK2Xl5OPwKzvZ2rBDvo+nxxARERFxUwGpgPom9+NE9tvuMv8AACAASURBVElPj+GV7HYrhYVlp4CkJaRiQwVEREREyg4twRIREREREdOogIiIiIiIiGlUQEpRYGAgANnZ2QwePPh3XztixAiWLl36m+0LFy5k4cKFhswnIiIiIuJpugfEAOfOnWPfvn3X9N74+PhSnkZEREREpOzQFRADjB8/nlOnTrmvgsydO5fQ0FDCw8OZOnWq+3UbNmyge/fudOzYkY8//hiAmTNnMnPmTAAeeOABXn75ZaKiooiNjeXYsWMApKen061bN6Kiohg3bhwJCQkmf0IRERERkWujKyAGGD16NH369OGtt95i9+7d/P3vf2fJkiVUrlyZxx9/nL179wJw6dIlPvnkEw4ePEifPn3o0aNHkeNkZWXRpk0bXnjhBSZNmsSCBQt47rnneP7553nnnXdo3Lgx48ePL/F8NpsVu13d0yhlKVub1UpAQDVPj1GqvO3zlDXK13jK2FjK11jK11gVJV8VEINt376djh07Uq3a5b9Qc+fOde/r1KkTFouFO+64gzNnzlzx/Q8++CAAd9xxB9988w0//PAD/v7+NG7cGIDu3bszYcKEEs3kcDjL1KNivUlZewyvw+kkKyvb02OUmoCAal71ecoa5Ws8ZWws5Wss5Wssb8vXarXg71/1ivtUQAxmt9uxWCzurzMzM6lcuTIANpsNoMj+/+br6+t+jcvlwmaz4XSWnW9wRURERERKouysFfEidrudwsJCAO677z6+/PJLcnJyKCws5LnnnnMvwboWt912G+fPn+fAgQMArFixolRmFhERERExg66AGMDf3586deqQkJDA/Pnz6d27Nz179sTpdPLnP/+Ztm3bsnz58ms6to+PD1OmTGH48OFYrVYaNmyIn59fKX8CERERERFjWFwul8vTQ0jxOZ1OXn31VRITE6lSpQoffPABmZmZjBgxotjHCJ/fhRPZJw2csuIqa/eApCWkYsuv4ukxSo23rY8ta5Sv8ZSxsZSvsZSvsbwtX90D4kWsVis1atSge/fuVKpUibp165b4JnQREREREU/RFZAKKOtCFg5X2fkpvTexWa04ytBDAmzYId/H02OUGm/76VBZo3yNp4yNpXyNpXyN5W356gqIFGG9WBmc6p1G8LZ/PERERERKm56CJSIiIiIiplEBERERERER06iAiIiIiIiIaVRARERERETENCogIiIiIiJiGhUQERERERExjQqIiIiIiIiYRgVERERERERMowIiIiIiIiKmUQERERERERHTqICIiIiIiIhp7J4eQMzn9M3D4XJ6egyvlJWTj8Ov7GZrww75Pp4eQ0RERCowFZAKqG9yP05kn/T0GF7JbrdSWFh2C0haQio2VEBERETEc7QES0RERERETKMCIiIiIiIipqmQBSQjI4PmzZsTGRlJVFQUXbp0oX///vz0009XfU9CQgLp6eklPteIESNYunTp9YwLwJ49exg1atR1H0dERERExJMq7D0gtWrVIiUlxf31pEmTmDJlCq+99poHp7q6u+66i7vuusvTY4iIiIiIXJcKeQXkSoKCgjh48CC7du3ikUceISIigr59+3L06NEir0tKSmLx4sXurxMSEvjuu+9ISEhgwoQJREdHEx4ezubNm92v2bBhA927d6djx458/PHHAGRmZjJgwADi4uLo0KEDb7zxBgAFBQX89a9/JTQ0lD59+tC3b1/S09NJT08nISEBgG3bthEfH090dDSdOnVi7dq1RscjIiIiIlIqKuwVkF8rKChgzZo1NG/enGeffZbXX3+dFi1akJqayrPPPsuSJUvcr42NjWXmzJnExcVx/PhxfvnlF1q2bAnAhQsXSE5OZt++fTzxxBN88cUXAFy6dIlPPvmEgwcP0qdPH3r06MHKlSvp2rUr0dHRZGdn89BDD5GQkMCqVavIy8sjLS2NEydO0K1bt9/M+9FHHzF+/HgaNWrE1q1bmThxIiEhIcX+vDabFbtd3dMoZTlbm9VKQEA1T49xXcr7/GWd8jWeMjaW8jWW8jVWRcm3whaQU6dOERkZCVwuCC1atCA2NpZ9+/bRokULAMLCwhgzZgzZ2dnu9wUF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p04dEhISSExMLHLuf2/79bHvuOMOXC4X//d//wfAiBEjaN++PeHh4aZnIyIiIiJSEiogxXTkyBHWr19PtWrVmDlzJpcuXWL16tUApKamAjB69Gj69OnDW2+9xdGjRzl06BCLFi3CarXy/PPPs3z5ch577DEAWrVqxcsvv8yCBQuYMGECb7311u+e/9fHPnbsGH379uWZZ54hPz+fr7/+mhdffLHYn8Vms2K3a/WdUSpqtjarlYCAaoafx4xzVGTK13jK2FjK11jK11gVJV8VkGJq2LAh1ar95y9FixYtfvf1DRo0YPjw4XzyySccPnyYXbt2Ub9+fQD8/PyIiIgAIDIyktdff71Es9xyyy3UrVuX7du3c+LECR566CF8fX2L/X6Hw1lhn9RktIr8FCyH00lWVrah5wgIqGb4OSoy5Ws8ZWws5Wss5Wssb8vXarXg71/1yvtMnqXc8vPz+92v/9vevXsZMGAATqeT0NBQQkJCcLlcAFit/4nd5XJht5e8B8bGxrJy5UpWrlxJTExMid8vIiIiIuIJKiClyG63U1hYCMD27du5//77iY+P59Zbb2XDhg04HA4AcnNzWbduHQBLliyhbdu2JTo2QOfOndm6dSunT5+mZcuWBnwaEREREZHSpwJSivz9/d03k4eHh7N//366detGnz59aN68ORkZGQDceOONrF27loiICLZs2cLIkSNLdGy4fAXm7rvvpkuXLoZ+JhERERGR0mRx/XtdkJQbLpeLnJwcevTowdy5cwkICCjR+8Pnd9FvQjdIRb4HJC0hFVt+FUPP4W3rY8sa5Ws8ZWws5Wss5Wssb8tX94B4mT179hAcHExcXFyJy4eIiIiIiCfpKVjlUIsWLdi2bds1v39e9Fwcror5U3qj2axWHM6Kma1N/5yIiIhIMeg7hgrIerEyOLXyzgjedvlUREREpLRpCZaIiIiIiJhGBUREREREREyjAiIiIiIiIqZRAREREREREdOogIiIiIiIiGlUQERERERExDQqICIiIiIiYhoVEBERERERMY0KiIiIiIiImEYFRERERERETKMCIiIiIiIiplEBERERERER09g9PYCYz+mbh8Pl9PQYXikrJx+Hn7ItDht2yPfx9BgiIiJiMhWQCqhvcj9OZJ/09BheyW63UlioAlIcaQmp2FABERERqWi0BEtEREREREyjAlIC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\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Plot a visualization for the Feature Importance Strengths\n",
    "\n",
    "plt.figure(figsize = (12,8))\n",
    "feat_importances = pd.Series(feature_importances, index=df.columns[:16])\n",
    "feat_importances.nlargest(16).plot(kind='barh', alpha=0.8, color='Green')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Polyuria, Polydipsia, Age, Gender and Sudden weight loss,  proves to be major contributing factors to diabetes detection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random Forest Regression. mean_squared_error:  0.12888638482427792\n",
      "Random Forest Regression. mean_absolute_error:  0.06645526459356246\n",
      "Random Forest Regression. r2_score:  0.923315343880382\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestRegressor\n",
    "\n",
    "rand2 = RandomForestRegressor(max_features=2, n_estimators=282, random_state=1)\n",
    "\n",
    "# Train the classifier on the training set\n",
    "rand2.fit(training_inputs, training_classes)\n",
    "\n",
    "# Predict the model\n",
    "pred_rf = rand2.predict(testing_inputs)\n",
    "\n",
    "#mean square error\n",
    "#pred_dt = regressor.predict(X_pre_test)\n",
    "rd_mse = mean_squared_error(testing_classes, pred_rf)\n",
    "rd_rmse = np.sqrt(rd_mse)\n",
    "\n",
    "#mean absolute error\n",
    "rd_mae = mean_absolute_error(testing_classes, pred_rf)\n",
    "\n",
    "\n",
    "# r2 score\n",
    "rd_r2 = r2_score(testing_classes, pred_rf)\n",
    "\n",
    "\n",
    "print('Random Forest Regression. mean_squared_error: ', rd_rmse)\n",
    "print('Random Forest Regression. mean_absolute_error: ', rd_mae)\n",
    "print('Random Forest Regression. r2_score: ', rd_r2)\n",
    "\n",
    "#pred_rf"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Compute 95% confidence interval on the RMSE value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.09276678, 0.15690037])"
      ]
     },
     "execution_count": 198,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scipy import stats\n",
    "\n",
    "confidence = 0.95\n",
    "squared_errors = (pred_rf - testing_classes) ** 2\n",
    "np.sqrt(stats.t.interval(confidence, len(squared_errors) - 1,\n",
    "                         loc=squared_errors.mean(),\n",
    "                         scale=stats.sem(squared_errors)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "# open a file, where you ant to store the data\n",
    "file = open('diabet_rf.pkl', 'wb')\n",
    "\n",
    "# dump information to that file\n",
    "pickle.dump(rand2, file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = open('diabet_rf.pkl','rb')\n",
    "forest = pickle.load(model)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.25531915]\n"
     ]
    }
   ],
   "source": [
    "print(forest.predict([[18, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Irrespective of the age and gender, symptoms such as Polyuria, Polydipsia, Sudden Weight Loss, Visual Bearing seems to be the overriding factor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Age', 'Gender', 'Polyuria', 'Polydipsia', 'Sudden_Weight_Loss',\n",
       "       'Weakness', 'Polyphagia', 'Genital_Thrush', 'Visual_Blurring',\n",
       "       'Itching', 'Irritability', 'Delayed_Healing', 'Partial_Paresis',\n",
       "       'Muscle_Stiffness', 'Alopecia', 'Obesity', 'class'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 183,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
