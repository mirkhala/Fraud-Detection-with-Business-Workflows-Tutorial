from joblib import load
import pandas as pd
import botocore
import boto3

class ModelFull(object):
    def __init__(self):
        print("Initializing")
        # Variables needed for metric collection
        self.V3=0
        self.V4=0
        self.V10=0
        self.V11=0
        self.V12=0
        self.V14=0
        self.V17=0
        self.Amount=0
        self.proba_1 = 0
        #///////// Loading mode from filesystem
        # Create an S3 client
        s3 = boto3.client(
            service_name='s3',
            aws_access_key_id='DUCLUBW5EOGUTIM5UU83',
            aws_secret_access_key='hPSyLCEOfgkY6xPmAPf846n71EEMiNI1YHWyZjyW', 
            endpoint_url='http://s3-rook-ceph.apps.cluster-mlops-4f2f.mlops-4f2f.sandbox1485.opentlc.com'
        )
        key = "uploaded/modelfull.joblib"
        try:
            print("Trying to download model")
            s3.download_file(
                Bucket='ccdata-1f48081f-efe6-423e-9381-301a05bafc6c', 
                Key=key, Filename="/tmp/modelfull_1.joblib"
            )
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

        # Replace with path of trained model
        print("Loading model to seldon")
        model_path = '/tmp/modelfull_1.joblib'
        self.clf = load(model_path)
        print("Model uploaded to class")
        
        
    def predict(self,x,features_names):
        print(x)
        print(type(x))
        result = "PASS"
        featurearray=[float(i) for i in x.split(',')]
        print(featurearray)
        # grabbing features for metric to be scraped by prometheus
        self.V3 = featurearray[0]
        self.V4 = featurearray[1]
        self.V10 = featurearray[2]
        self.V11 = featurearray[3]
        self.V12 = featurearray[4]
        self.V14 = featurearray[5]
        self.V17 = featurearray[6]
        self.Amount = featurearray[7]
        
        rowdf = pd.DataFrame([featurearray], columns = ['V3','V4','V10','V11','V12','V14','V17','Amount'])
        print(rowdf)
        self.proba_1 = self.clf.predict_proba(rowdf)[:,1]
        predictions = self.clf.predict(rowdf)
        # initialize list of lists
        return predictions
        
    def metrics(self):
        return [
            {"type":"GAUGE","key":"V3","value":self.V3},
            {"type":"GAUGE","key":"V4","value":self.V4},
            {"type":"GAUGE","key":"V10","value":self.V10},
            {"type":"GAUGE","key":"V11","value":self.V11},
            {"type":"GAUGE","key":"V12","value":self.V12},
            {"type":"GAUGE","key":"V14","value":self.V14},
            {"type":"GAUGE","key":"V17","value":self.V17},
            {"type":"GAUGE","key":"Amount","value":self.Amount},
            {"type":"GAUGE","key":"proba_1","value":self.proba_1[0]},
            ]

    
if __name__ == "__main__":
    model_full = ModelFull()
    print(model_full.clf)