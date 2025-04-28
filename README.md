# Sports_perons_classifier

ML Project on Spirts Persons' images classification  
5 Celebriries - Ekterina Gamova, Fedor Yemelyanenko, Kilian Mbappe, Maria Sharapova, Yusuf Dikec.  
Used linear models, chose the best according to the learning results.  

Best model turned to be SVM - Support vectors model - 73% accuracy  
Random forest and logistic regression showed 2-3% worse. But results were close.  

Tried to make a bigger dataset but results became worse- maybe beacuse of overlearning.  
Catboost - couldn't finish learning because of technical issues.  
Didn't use neural networks because wanted to focus on linear models.  

Space for enhancing:  
1 taking skin color into consideration (now it turns image black and white and for Kilian Mbappe it would make things better)  
2 repairing the catboost  
3 taking more patterns into consideration - now the model looks at eyes and mouth only