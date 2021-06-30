from pycaret.classification import *
from pycaret.regression import *
import pandas as pd
import os

class Inference:
    def inference(self,pickleFileLocation,newDataLocation,storeLocation):    #isAuto parameter removed because of error
        
        
        data=pd.read_csv(data_location)
        clf=load_model(filelocation)
        results=predict_model(clf,data=data)

        csvresults=results.to_csv()

        inferenceDataResultsPath=os.path.join(storeLocation,"inference.csv")
        inference=open(inferenceDataResultsPath,"w+")
        inference.write(csvresults)
        inference.close()
    
        return inferenceDataResultsPath