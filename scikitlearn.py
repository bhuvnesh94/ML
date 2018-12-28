#!/usr/bin/python3
import mpld3
# laoding  iris dataset from  sklearn 
from sklearn.datasets import load_iris
# loading  tree factor for decisiontree Classifier 
from sklearn import tree

# loading  dataset 
iris=load_iris()
print(dir(iris))

'''
 dataset explaination 
here features store under ---->   iris.data
     label               ---->    iris.target - 0 mean setosa , 1 versicolor                                                 2 - virginica 
iris.target_names == contains flower name
iris.feature_names = contains flower attribute 
'''      
# split datasets into training and testing 
#                  features ,  label      testsize 10%
from sklearn.model_selection import  train_test_split
train_data,test_data,train_target,test_target=(train_test_split(iris.data,iris.target,test_size=0.1))

train_data1,test_data1,train_target1,test_target1=(train_test_split(iris.data,iris.target,test_size=0.2))
print(test_data.shape)
print(test_target.shape)
'''
above train_data -- training features that is 90%
      test_data ---- remaining  10%  of  data that you can use to test 
      train_target --- training label that is  90% 
      test_target ----  remaining  10%  of label 
'''

#  calling  decision tree
clf=tree.DecisionTreeClassifier()
#  training  data
trained_algo10=clf.fit(train_data,train_target)
trained_algo20=clf.fit(train_data1,train_target1)
# time for prediction 
output10=trained_algo10.predict(test_data)
output20=trained_algo20.predict(test_data1)
print("predicted output",output10)
print("predicted output",output20)

# loading KNN 
from  sklearn.neighbors  import  KNeighborsClassifier
clf=KNeighborsClassifier(n_neighbors=5)
trained10=clf.fit(train_data,train_target)
trained20=clf.fit(train_data1,train_target1)
outputk10=trained10.predict(test_data)
outputk20=trained20.predict(test_data1)



# calculating  accuracy for  decisiontree 
from  sklearn.metrics  import  accuracy_score
acc10=accuracy_score(test_target,output10)
acc20=accuracy_score(test_target1,output20)
print("accuracy of DSC Tree with 10 % ",acc10)
print("accuracy of DSC Tree with 20%  ",acc20)

# calculating  accuracy for  KNN
from  sklearn.metrics  import  accuracy_score
acck10=accuracy_score(test_target,outputk10)
acck20=accuracy_score(test_target1,outputk20)
print("accuracy of  KNN with 10 % ",acck10)
print("accuracy of KNN Tree with 20%  ",acck20)

# plotting graph
import matplotlib.pyplot  as plt
plt.plot(acc10,acck10)
plt.plot(acc20,acck20)
plt.bar(acc10,acck10)
plt.bar(acc10,acck20)
mpld3.show()
