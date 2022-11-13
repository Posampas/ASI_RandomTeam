from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_data, train_model , evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["car_price", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            )
            ,
            node(
                func = train_model,
                inputs = ["X_train","y_train"],
                outputs = "regressor",
                name="tran_model_node"
            )
            ,
            node(
                func = evaluate_model,
                inputs = ["regressor", "X_test","y_test"],
                outputs = None,
                name="evaluate_model_node"
            )

        ]
    )
