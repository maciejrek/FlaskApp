from ma import ma
from marshmallow import pre_dump
from models.user import UserModel


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id", "confirmation")

    # for dump purposes:
    # set "list" containing last conf only to user.confirmation
    @pre_dump
    def _pre_dump(self, user: UserModel, **kwargs):
        user.confirmation = [user.most_recent_confirmation]
        return user
