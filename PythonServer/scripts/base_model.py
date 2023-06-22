import abc


class BaseModel(abc.ABC):
    def load_model(self):
        """
        Load the model.
        """
        pass

    def predict(self, input_data):
        """
        Make a prediction using the model.

        :param input_data: The input data for the model.
        :return: The prediction result.
        """
        pass



