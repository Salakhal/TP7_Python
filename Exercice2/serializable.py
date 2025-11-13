import json

class Serializable:
    def to_json(self):
        # On ignore 'historique' pour éviter les références circulaires
        state = {k: v for k, v in self.__dict__.items() if k != 'historique'}
        return json.dumps(state, default=str)

    @classmethod
    def from_json(cls, json_str):
        return cls(**json.loads(json_str))
