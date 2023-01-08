from customer.entity.artifact_entity import ClassificationMetricArtifact
from sklearn.metrics import f1_score, precision_score, recall_score
import os, sys


def get_classification_score(y_true, y_pred)->ClassificationMetricArtifact:
    try:
        model_f1_score = f1_score(y_true, y_pred)
        model_recall_score = recall_score(y_true, y_pred)
        model_precision_score = precision_score(y_true, y_pred)
        print(f"f1 score = {model_f1_score}  recall score = {model_recall_score}  precision_score = {model_precision_score}")


        classfication_metric = ClassificationMetricArtifact(f1_score=model_f1_score,
                   recall_score=model_recall_score, 
                   precision_score=model_precision_score)
        return classfication_metric
    except Exception as e:
        raise e