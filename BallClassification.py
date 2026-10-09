from sklearn import tree
from sklearn.metrics import accuracy_score

# Rough = 1
# Smooth = 0

# Tennis = 1
# Cricket = 2

def main():
    print("Ball classification case study")

    # Original encoded dataset
    # Independent variables
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    # dependent variables
    Y = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # Independent variables for training
    Xtrain = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]

    # Independent variables for testing
    Xtest =[[35,1],[95,0]]

    # dependent variables for training
    Ytrain = [1,1,2,1,2,1,2,1,1,1,2,1,2]

    # dependent variables for testing
    Ytest = [1,2]

    modelobj = tree.DecisionTreeClassifier()

    trainedmodel = modelobj.fit(Xtrain,Ytrain)

    Result = trainedmodel.predict(Xtest)                   # 1  2

    print("Model predicts the object as : ",Result)

    Accuracy = accuracy_score(Ytest, Result)
    print("Accuracy Score : ", Accuracy*100, "%")

if __name__ == "__main__":
    main()