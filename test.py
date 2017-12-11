from matplotlib.pylab import *
import data_factory
import perceptron

data=data_factory.DataFactory()
trainset = data.generateUpData( 40, 5, 2, 1)+data.generateDownData(40, 5, 2, -2)# train set generation
#trainset = trainset+data.generateDownData( 40, 5, 1, 2)
testset = data.generateUpData(100,5,2,1)+data.generateDownData( 100, 5, 2, -2) # test set generation
#testset = testset+data.generateDownData( 100, 5, 1, 2)
p = perceptron.Perceptron() # use a short
p.train(trainset)

#Perceptron test
figure()
hit=0
nothit=0
for x in testset:
    r = p.response(x)
    if r != x[2]: # if the response is not correct
        #print 'not hit.'
        nothit+=1
    else:
        #print 'hit'
        hit+=1
    if r == 1:
        plot(x[0], x[1], 'ob')
    else:
        plot(x[0], x[1], 'or')
    
print 'hit:'+str(hit)
print 'not hit:'+str(nothit)

# plot of the separation line. 
# The centor of line is the coordinate origin
# So the length of line is 2
# The separation line is orthogonal to w
n = norm(p.w) # aka the length of p.w vector
ww = p.w / n # a unit vector
ww1 = [ww[1], -ww[0]]
ww2 = [-ww[1], ww[0]]
plot([10*ww1[0], 10*ww2[0]], [10*ww1[1], 10*ww2[1]], '--k')
#show()

savefig("testset.png")