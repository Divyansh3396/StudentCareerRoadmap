from sklearn.tree import DecisionTreeClassifier

# training data
X = [
[5,1,1,1,1],
[1,5,1,1,1],
[1,1,5,1,1],
[1,1,1,5,1],
[1,1,1,1,5],
[4,2,1,1,2],
[3,1,2,1,3],
[2,3,1,1,4]
]

y = [
"AI Engineer",
"Doctor",
"Lawyer",
"Sportsperson",
"Artist",
"Data Scientist",
"Civil Engineer",
"Photographer"
]

model = DecisionTreeClassifier()
model.fit(X,y)

def predict_career(values):
    result = model.predict([values])
    return result[0]