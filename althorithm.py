import pandas as pd
#effective field goal perentage difference: 0.16118265
#turnover percentage difference: -0.05958713
#offensive rebound percentage difference: 0.07061777
#free throws to field goals attempts difference: 0.03267933
#offensive rating difference: 0.17885523
#defensive rating difference: -0.33924331

#effective field goal perentage difference (court): 0.10808104
#turnover percentage difference (court):  -0.09548481
#offensive rebound percentage difference (court):   0.07055131
#free throws to field goals attempts difference (court): 0.0748545
#offensive rating difference (court): 0.14822224
#defensive rating difference (court): -0.21756487

#court means: considering court situation means:
#if team A is the host and team B is the visitor,
#effective field goal percentage is A efgp home - B efgp road

col_names = ['efgpd', 'tpd', 'orpd', 'ftfgad', 'ord', 'drd', 
'efgpdc', 'tpdc', 'orpdc', 'ftfgadc', 'ordc', 'drdc'];

pima = dataset;
pima.head();

X = pima[col_names];
Y = pima.label;

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
