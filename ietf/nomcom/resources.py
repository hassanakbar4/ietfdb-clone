# Copyright The IETF Trust 2014-2019, All Rights Reserved
# Autogenerated by the mkresources management command 2014-11-13 23:53
from ietf.api import ModelResource
from ietf.api import ToOneField
from tastypie.fields import ToManyField
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.cache import SimpleCache

from ietf import api

from ietf.nomcom.models import (NomCom, Position, Nominee, ReminderDates, NomineePosition,
    Feedback, Nomination, FeedbackLastSeen, Topic, TopicFeedbackLastSeen, )

from ietf.group.resources import GroupResource
class NomComResource(ModelResource):
    group            = ToOneField(GroupResource, 'group')
    class Meta:
        cache = SimpleCache()
        queryset = NomCom.objects.all()
        serializer = api.Serializer()
        #resource_name = 'nomcom'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "public_key": ALL,
            "send_questionnaire": ALL,
            "reminder_interval": ALL,
            "initial_text": ALL,
            "show_nominee_pictures": ALL,
            "show_accepted_nominees": ALL,
            "group": ALL_WITH_RELATIONS,
        }
api.nomcom.register(NomComResource())

from ietf.dbtemplate.resources import DBTemplateResource
class PositionResource(ModelResource):
    nomcom           = ToOneField(NomComResource, 'nomcom')
    requirement      = ToOneField(DBTemplateResource, 'requirement', null=True)
    questionnaire    = ToOneField(DBTemplateResource, 'questionnaire', null=True)
    class Meta:
        cache = SimpleCache()
        queryset = Position.objects.all()
        serializer = api.Serializer()
        #resource_name = 'position'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "name": ALL,
            "is_open": ALL,
            "accepting_nominations": ALL,
            "accepting_feedback": ALL,
            "nomcom": ALL_WITH_RELATIONS,
            "requirement": ALL_WITH_RELATIONS,
            "questionnaire": ALL_WITH_RELATIONS,
        }
api.nomcom.register(PositionResource())

from ietf.person.resources import EmailResource
class NomineeResource(ModelResource):
    email            = ToOneField(EmailResource, 'email')
    duplicated       = ToOneField('ietf.nomcom.resources.NomineeResource', 'duplicated', null=True)
    nomcom           = ToOneField(NomComResource, 'nomcom')
    nominee_position = ToManyField(PositionResource, 'nominee_position', null=True)
    class Meta:
        cache = SimpleCache()
        queryset = Nominee.objects.all()
        serializer = api.Serializer()
        #resource_name = 'nominee'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "email": ALL_WITH_RELATIONS,
            "duplicated": ALL_WITH_RELATIONS,
            "nomcom": ALL_WITH_RELATIONS,
            "nominee_position": ALL_WITH_RELATIONS,
        }
api.nomcom.register(NomineeResource())

class ReminderDatesResource(ModelResource):
    nomcom           = ToOneField(NomComResource, 'nomcom')
    class Meta:
        cache = SimpleCache()
        queryset = ReminderDates.objects.all()
        serializer = api.Serializer()
        #resource_name = 'reminderdates'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "date": ALL,
            "nomcom": ALL_WITH_RELATIONS,
        }
api.nomcom.register(ReminderDatesResource())

from ietf.name.resources import NomineePositionStateNameResource
class NomineePositionResource(ModelResource):
    position         = ToOneField(PositionResource, 'position')
    nominee          = ToOneField(NomineeResource, 'nominee')
    state            = ToOneField(NomineePositionStateNameResource, 'state')
    class Meta:
        cache = SimpleCache()
        queryset = NomineePosition.objects.all()
        serializer = api.Serializer()
        #resource_name = 'nomineeposition'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "time": ALL,
            "position": ALL_WITH_RELATIONS,
            "nominee": ALL_WITH_RELATIONS,
            "state": ALL_WITH_RELATIONS,
        }
api.nomcom.register(NomineePositionResource())

from ietf.name.resources import FeedbackTypeNameResource
from ietf.utils.resources import UserResource
class FeedbackResource(ModelResource):
    nomcom           = ToOneField(NomComResource, 'nomcom')
    type             = ToOneField(FeedbackTypeNameResource, 'type', null=True)
    user             = ToOneField(UserResource, 'user', null=True)
    positions        = ToManyField(PositionResource, 'positions', null=True)
    nominees         = ToManyField(NomineeResource, 'nominees', null=True)
    class Meta:
        cache = SimpleCache()
        queryset = Feedback.objects.all()
        serializer = api.Serializer()
        #resource_name = 'feedback'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "author": ALL,
            "subject": ALL,
            "comments": ALL,
            "time": ALL,
            "nomcom": ALL_WITH_RELATIONS,
            "type": ALL_WITH_RELATIONS,
            "user": ALL_WITH_RELATIONS,
            "positions": ALL_WITH_RELATIONS,
            "nominees": ALL_WITH_RELATIONS,
        }
api.nomcom.register(FeedbackResource())

from ietf.utils.resources import UserResource
class NominationResource(ModelResource):
    position         = ToOneField(PositionResource, 'position')
    nominee          = ToOneField(NomineeResource, 'nominee')
    comments         = ToOneField(FeedbackResource, 'comments')
    user             = ToOneField(UserResource, 'user', null=True)
    class Meta:
        cache = SimpleCache()
        queryset = Nomination.objects.all()
        serializer = api.Serializer()
        #resource_name = 'nomination'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "candidate_name": ALL,
            "candidate_email": ALL,
            "candidate_phone": ALL,
            "nominator_email": ALL,
            "time": ALL,
            "position": ALL_WITH_RELATIONS,
            "nominee": ALL_WITH_RELATIONS,
            "comments": ALL_WITH_RELATIONS,
            "user": ALL_WITH_RELATIONS,
        }
api.nomcom.register(NominationResource())

from ietf.person.resources import PersonResource
class FeedbackLastSeenResource(ModelResource):
    reviewer         = ToOneField(PersonResource, 'reviewer')
    nominee          = ToOneField(NomineeResource, 'nominee')
    class Meta:
        cache = SimpleCache()
        queryset = FeedbackLastSeen.objects.all()
        serializer = api.Serializer()
        ordering = ['id', ]
        filtering = {
            "id": ALL,
            "time": ALL,
            "reviewer": ALL_WITH_RELATIONS,
            "nominee": ALL_WITH_RELATIONS,
        }
api.nomcom.register(FeedbackLastSeenResource())


from ietf.name.resources import TopicAudienceNameResource
from ietf.dbtemplate.resources import DBTemplateResource
class TopicResource(ModelResource):
    nomcom           = ToOneField(NomComResource, 'nomcom')
    description      = ToOneField(DBTemplateResource, 'description', null=True)
    audience         = ToOneField(TopicAudienceNameResource, 'audience')
    class Meta:
        queryset = Topic.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'topic'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "subject": ALL,
            "accepting_feedback": ALL,
            "nomcom": ALL_WITH_RELATIONS,
            "description": ALL_WITH_RELATIONS,
            "audience": ALL_WITH_RELATIONS,
        }
api.nomcom.register(TopicResource())


from ietf.person.resources import PersonResource
class TopicFeedbackLastSeenResource(ModelResource):
    reviewer         = ToOneField(PersonResource, 'reviewer')
    topic            = ToOneField(TopicResource, 'topic')
    class Meta:
        queryset = TopicFeedbackLastSeen.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'topicfeedbacklastseen'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "time": ALL,
            "reviewer": ALL_WITH_RELATIONS,
            "topic": ALL_WITH_RELATIONS,
        }
api.nomcom.register(TopicFeedbackLastSeenResource())
