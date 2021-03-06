import featuretools as ft
import categorical_encoding as ce
from featuretools.tests.testing_utils import make_ecommerce_entityset


def create_feature_matrix():
    es = make_ecommerce_entityset()
    f1 = ft.Feature(es["log"]["product_id"])
    f2 = ft.Feature(es["log"]["value"])
    features = [f1, f2]
    ids = [0, 1, 2, 3, 4, 5]
    feature_matrix = ft.calculate_feature_matrix(features, es, instance_ids=ids)

    return feature_matrix, features, f1, f2, es, ids