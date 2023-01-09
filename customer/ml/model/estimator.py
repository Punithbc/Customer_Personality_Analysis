import os


class CustomerModel:
    def __init__(self,encoder_obj, scaled_obj, pca_obj, model_obj):
        try:
            self.encoded = encoder_obj
            self.scaled = scaled_obj
            self.pca_obj = pca_obj
            self.model_obj = model_obj

        except Exception as e:
            raise e    
    

    def predict(self, x):
        try:
            s = (x.dtypes == 'object')
            print(f"shape of dataset {x.shape}")
            object_cols = list(s[s].index)

            print("Categorical variables in the dataset:", object_cols)
            
            x[object_cols[0]] = self.encoded.obj1.transform(x[object_cols[0]])
            x[object_cols[1]] = self.encoded.obj2.transform(x[object_cols[1]])
            
            scaling = self.scaled.transform(x)
            pca = self.pca_obj.transform(scaling)
            y_hat = self.model_obj.predict(pca)
            return y_hat
        except Exception as e:
            raise e
                