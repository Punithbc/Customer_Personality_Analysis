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
            encoded = self.encoded.transform(x)
            scaling = self.scaled.tranform(encoded)
            pca = self.pca_obj.transform(scaling)
            y_hat = self.model_obj.predict(pca)
            return y_hat
        except Exception as e:
            raise e
                