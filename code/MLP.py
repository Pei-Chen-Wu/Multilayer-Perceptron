# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:31:12 2020

@author: Nclab
"""

from sklearn.neural_network import MLPClassifier

X = [[0., 0.,0.], [1., 1.,1.],[2., 2.,2.]]

y = [0, 1, 2]

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                     hidden_layer_sizes=(5,3), random_state=1)

clf.fit(X, y)    

y_predict=clf.predict([[2., 2., 2.], [-1., -2.,0.],[1., 1.,0.]])
print('y_predict:',y_predict)
print('score_train:',clf.score(X,y))


