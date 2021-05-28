from edc_base.model_mixins import BaseUuidModel, ListModelMixin


class SubjectRace(ListModelMixin, BaseUuidModel):
    pass


class ParticipantMedications(ListModelMixin, BaseUuidModel):
    pass


class MaternalDiagnosesList(ListModelMixin, BaseUuidModel):
    pass


class PriorArv(ListModelMixin, BaseUuidModel):
    pass


class WcsDxAdult(ListModelMixin, BaseUuidModel):
    pass


class SAECriteria(ListModelMixin, BaseUuidModel):
    pass


class COVIDSymptoms(ListModelMixin, BaseUuidModel):
    pass
