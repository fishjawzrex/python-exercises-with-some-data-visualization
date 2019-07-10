from sklearn import datasets, svm
digits = datasets.load_digits()


x,y = digits.data[:-10], digits.target[:-10]

#set the learning rate(gamma) to .01,
#set 
clf = svm.SVC(gamma = .01, C=100).fit(x,y)


print 'predictions:', clf.predict(digits.data[-10:])

print 'target:', digits.target[-10:]