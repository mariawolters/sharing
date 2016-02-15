#!/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sklearn
<<<<<<< Local Changes
<<<<<<< Local Changes
import pydot
from sklearn.externals.six import StringIO

from sklearn import metrics, preprocessing, crossvalidation
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.naive_bayes import GaussianNB
from IPython.display import Image 


def get_code(tree, feature_names):
    left      = tree.tree_.children_left
    right     = tree.tree_.children_right
    threshold = tree.tree_.threshold
    features  = [feature_names[i] for i in tree.tree_.feature]
    value = tree.tree_.value
    def recurse(left, right, threshold, features, node):
        if (threshold[node] != -2):
            print "if ( " + features[node] + " <= " + str(threshold[node]) + " ) {"
            if left[node] != -1:
                recurse (left, right, threshold, features,left[node])
            print "} else {"
            if right[node] != -1:
                recurse (left, right, threshold, features,right[node])
            print "}"
        else:
            print "return " + str(value[node])

    recurse(left, right, threshold, features, 0)

data =  np.loadtxt(fname ="./data/spambase.data", delimiter = ',')
feat_names = open("./data/spambase.header").readline().strip().split(",")


spamFeat = data[:,0:55]
spamSpam = data[:,57]

spamcl = GaussianNB()

spamClass = spamcl.fit(spamFeat,spamSpam)
spamPred = spamClass.predict(spamFeat)

print(metrics.classification_report(spamPred,spamSpam))

spamClass.theta_[:,3]
spamClass.class_prior_

# testing is pretty much a repeat of this 

# for Decision Tree and 10-fold CV, I'm using spambase to demo 

spamcltree = DecisionTreeClassifier()
spamClassTree = spamcltree.fit(spamFeat,spamSpam)
spamPredTree = spamClassTree.predict(spamFeat)

dot_data = StringIO()  
sklearn.tree.export_graphviz(spamClassTree, out_file=dot_data,  
                         feature_names=feat_names,    
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = pydot.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())  
# graph.write_png('titanic.png') is the iPython command, alternatively use get_code 

scores = cross_validation.cross_val_score(spamcltree, spamFeat, spamSpam, cv=10)

print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

=======
>>>>>>> External Changes
=======
>>>>>>> External Changes

data =  np.loadtxt(fname = f, delimiter = ',')

