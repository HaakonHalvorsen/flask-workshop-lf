from marshmallow import Schema, fields

class PlainAthleteSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)

class PlainEventSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)

class PlainResultSchema(Schema):
    athlete_id = fields.Int(required=True)
    event_id = fields.Int(required=True)
    rank = fields.Int(required=True)
    
class AthleteSchema(PlainAthleteSchema):
    results = fields.List(fields.Nested(PlainResultSchema()), dump_only=True)
    
class EventSchema(PlainEventSchema):
    results = fields.List(fields.Nested(PlainResultSchema()), dump_only=True)
    
class ResultSchema(PlainResultSchema):
    athlete = fields.Nested(PlainAthleteSchema(), load_only=True)
    event = fields.Nested(PlainEventSchema(), load_only=True)