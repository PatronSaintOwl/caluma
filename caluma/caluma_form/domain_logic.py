from typing import Optional

from django.db import transaction

from caluma.caluma_core.models import BaseModel
from caluma.caluma_form import models, validators
from caluma.caluma_user.models import BaseUser
from caluma.utils import update_model


class BaseLogic:
    @staticmethod
    @transaction.atomic
    def create(model: BaseModel, user: Optional[BaseUser] = None, **kwargs):
        if user:
            kwargs["created_by_user"] = user
            kwargs["created_by_group"] = user.group

        return model.objects.create(**kwargs)


class SaveAnswerLogic:
    @staticmethod
    def validate_for_save(
        data: dict, user: BaseUser, answer: models.Answer = None, origin: bool = False
    ) -> dict:
        question = data["question"]

        if question.type == models.Question.TYPE_TABLE:
            data["documents"] = models.Document.objects.filter(pk__in=data["value"])
            del data["value"]
        elif question.type == models.Question.TYPE_FILE:
            data["file"] = data["value"]
            del data["value"]
        elif question.type == models.Question.TYPE_DATE:
            data["date"] = data["value"]
            del data["value"]

        validators.AnswerValidator().validate(
            **data, user=user, instance=answer, origin=origin
        )

        return data

    @staticmethod
    def pre_save(validated_data: dict) -> dict:
        # TODO emit events
        return validated_data

    @staticmethod
    def post_save(answer: models.Answer) -> models.Answer:
        # TODO emit events
        return answer

    @staticmethod
    @transaction.atomic
    def create(validated_data: dict, user: Optional[BaseUser] = None) -> models.Answer:
        if validated_data["question"].type == models.Question.TYPE_FILE:
            validated_data = __class__.set_file(validated_data)

        if validated_data["question"].type == models.Question.TYPE_TABLE:
            documents = validated_data.pop("documents")

        answer = BaseLogic.create(models.Answer, user, **validated_data)

        if answer.question.type == models.Question.TYPE_TABLE:
            answer.create_answer_documents(documents)

        return answer

    @staticmethod
    @transaction.atomic
    def update(validated_data, answer):
        if answer.question.type == models.Question.TYPE_TABLE:
            documents = validated_data.pop("documents")
            answer.unlink_unused_rows(docs_to_keep=documents)

        if (
            answer.question.type == models.Question.TYPE_FILE
            and answer.file.name is not validated_data["file"]
        ):
            answer.file.delete()
            validated_data = __class__.set_file(validated_data)

        update_model(answer, validated_data)

        if answer.question.type == models.Question.TYPE_TABLE:
            answer.create_answer_documents(documents)

    @staticmethod
    def set_file(validated_data):
        file_name = validated_data.get("file")
        file = models.File.objects.create(name=file_name)
        validated_data["file"] = file
        return validated_data


class SaveDocumentLogic:
    @staticmethod
    @transaction.atomic
    def create(
        # form: models.Form, meta: Optional[dict] = None, user: Optional[BaseUser] = None
        **kwargs,
    ):
        # return BaseLogic.create(models.Document, form=form, meta=meta, user=user)
        return BaseLogic.create(models.Document, **kwargs)

    @staticmethod
    @transaction.atomic
    def update(document, **kwargs):
        update_model(document, kwargs)
