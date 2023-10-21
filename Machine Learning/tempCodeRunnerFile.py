)
clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
AS=accuracy_score(y_test,y_pred)
print(AS)

