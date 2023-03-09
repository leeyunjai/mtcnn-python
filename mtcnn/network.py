import tensorflow as tf

class Network(object):

    def __init__(self, session, trainable: bool=True):
        self._session = session
        self.__trainable = trainable
        self.__layers = {}
        self.__last_layer_name = None

        with tf.compat.v1.variable_scope(self.__class__.__name__.lower()):
            self._config()

    def _config(self):
        raise NotImplementedError("This method must be implemented by the network.")

    def add_layer(self, name: str, layer_output):
        self.__layers[name] = layer_output
        self.__last_layer_name = name

    def get_layer(self, name: str=None):
        if name is None:
            name = self.__last_layer_name

        return self.__layers[name]

    def is_trainable(self):
        return self.__trainable

    def set_weights(self, weights_values: dict, ignore_missing=False):
        network_name = self.__class__.__name__.lower()

        with tf.compat.v1.variable_scope(network_name):
            for layer_name in weights_values:
                with tf.compat.v1.variable_scope(layer_name, reuse=True):
                    for param_name, data in weights_values[layer_name].items():
                        try:
                            var = tf.compat.v1.get_variable(param_name, use_resource=False)
                            self._session.run(var.assign(data))

                        except ValueError:
                            if not ignore_missing:
                                raise

    def feed(self, image):
        network_name = self.__class__.__name__.lower()

        with tf.compat.v1.variable_scope(network_name):
            return self._feed(image)

    def _feed(self, image):
        raise NotImplementedError("Method not implemented.")