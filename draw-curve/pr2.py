import _pickle as cPickle
import matplotlib.pyplot as plt

fr1= open('results/anquanmao_pr.pkl', 'rb')  # 这里open中第一个参数需要修改成自己生产的pkl文件
inf1 = cPickle.load(fr1)
fr1.close()

x1= inf1['rec']
y1= inf1['prec']



fr2= open('results/cap_pr.pkl', 'rb')  # 这里open中第一个参数需要修改成自己生产的pkl文件
inf2 = cPickle.load(fr2)
fr2.close()

x2= inf2['rec']
y2= inf2['prec']


plt.figure()
plt.xlabel('recall')
plt.ylabel('precision')
plt.title('PR cruve')
plt.plot(x1, y1, color="red")
plt.plot(x2, y2, color="blue")
plt.show()

#print('AP：', inf['ap'])
