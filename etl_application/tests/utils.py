class MockPrometheusClient:
    def __init__(self):
        self.registry = "registry"
        self.pubsub_counter = "pubsub_counter"
        self.api_call_gauge = "api_call_gauge"

    def write_to_registry(self, metric_name, value):
        pass

    def push_batch(self):
        pass