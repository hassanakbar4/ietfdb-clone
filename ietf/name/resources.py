# Autogenerated by the makeresources management command 2015-08-27 11:01 PDT
from tastypie.resources import ModelResource
from ietf.api import ToOneField         # pyflakes:ignore
from tastypie.fields import ToManyField  # pyflakes:ignore
from tastypie.constants import ALL, ALL_WITH_RELATIONS  # pyflakes:ignore
from tastypie.cache import SimpleCache

from ietf import api

from ietf.name.models import (TimeSlotTypeName, GroupStateName, DocTagName, IntendedStdLevelName,
    LiaisonStatementPurposeName, DraftSubmissionStateName, DocTypeName, RoleName,
    IprDisclosureStateName, StdLevelName, LiaisonStatementEventTypeName, GroupTypeName,
    IprEventTypeName, GroupMilestoneStateName, SessionStatusName, DocReminderTypeName,
    ConstraintName, MeetingTypeName, DocRelationshipName, RoomResourceName, IprLicenseTypeName,
    LiaisonStatementTagName, FeedbackTypeName, LiaisonStatementState, StreamName,
    BallotPositionName, DBTemplateTypeName, NomineePositionStateName,
    ReviewRequestStateName, ReviewTypeName, ReviewResultName)


class TimeSlotTypeNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = TimeSlotTypeName.objects.all()
        #resource_name = 'timeslottypename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(TimeSlotTypeNameResource())

class GroupStateNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = GroupStateName.objects.all()
        #resource_name = 'groupstatename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(GroupStateNameResource())

class DocTagNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = DocTagName.objects.all()
        #resource_name = 'doctagname'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(DocTagNameResource())

class IntendedStdLevelNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = IntendedStdLevelName.objects.all()
        #resource_name = 'intendedstdlevelname'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(IntendedStdLevelNameResource())

class LiaisonStatementPurposeNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = LiaisonStatementPurposeName.objects.all()
        #resource_name = 'liaisonstatementpurposename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(LiaisonStatementPurposeNameResource())

class DraftSubmissionStateNameResource(ModelResource):
    next_states      = ToManyField('ietf.name.resources.DraftSubmissionStateNameResource', 'next_states', null=True)
    class Meta:
        cache = SimpleCache()
        queryset = DraftSubmissionStateName.objects.all()
        #resource_name = 'draftsubmissionstatename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
            "next_states": ALL_WITH_RELATIONS,
        }
api.name.register(DraftSubmissionStateNameResource())

class DocTypeNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = DocTypeName.objects.all()
        #resource_name = 'doctypename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(DocTypeNameResource())

class RoleNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = RoleName.objects.all()
        #resource_name = 'rolename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(RoleNameResource())

class IprDisclosureStateNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = IprDisclosureStateName.objects.all()
        #resource_name = 'iprdisclosurestatename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(IprDisclosureStateNameResource())

class StdLevelNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = StdLevelName.objects.all()
        #resource_name = 'stdlevelname'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(StdLevelNameResource())

class LiaisonStatementEventTypeNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = LiaisonStatementEventTypeName.objects.all()
        #resource_name = 'liaisonstatementeventtypename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(LiaisonStatementEventTypeNameResource())

class GroupTypeNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = GroupTypeName.objects.all()
        #resource_name = 'grouptypename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(GroupTypeNameResource())

class IprEventTypeNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = IprEventTypeName.objects.all()
        #resource_name = 'ipreventtypename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(IprEventTypeNameResource())

class GroupMilestoneStateNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = GroupMilestoneStateName.objects.all()
        #resource_name = 'groupmilestonestatename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(GroupMilestoneStateNameResource())

class SessionStatusNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = SessionStatusName.objects.all()
        #resource_name = 'sessionstatusname'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(SessionStatusNameResource())

class DocReminderTypeNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = DocReminderTypeName.objects.all()
        #resource_name = 'docremindertypename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(DocReminderTypeNameResource())

class ConstraintNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = ConstraintName.objects.all()
        #resource_name = 'constraintname'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
            "penalty": ALL,
        }
api.name.register(ConstraintNameResource())

class MeetingTypeNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = MeetingTypeName.objects.all()
        #resource_name = 'meetingtypename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(MeetingTypeNameResource())

class DocRelationshipNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = DocRelationshipName.objects.all()
        #resource_name = 'docrelationshipname'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
            "revname": ALL,
        }
api.name.register(DocRelationshipNameResource())

class RoomResourceNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = RoomResourceName.objects.all()
        resource_name = 'roomresourcename' # Needed because tastypie otherwise removes 'resource' from the name
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(RoomResourceNameResource())

class IprLicenseTypeNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = IprLicenseTypeName.objects.all()
        #resource_name = 'iprlicensetypename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(IprLicenseTypeNameResource())

class LiaisonStatementTagNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = LiaisonStatementTagName.objects.all()
        #resource_name = 'liaisonstatementtagname'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(LiaisonStatementTagNameResource())

class FeedbackTypeNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = FeedbackTypeName.objects.all()
        #resource_name = 'feedbacktypename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(FeedbackTypeNameResource())

class LiaisonStatementStateResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = LiaisonStatementState.objects.all()
        #resource_name = 'liaisonstatementstate'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(LiaisonStatementStateResource())

class StreamNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = StreamName.objects.all()
        #resource_name = 'streamname'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(StreamNameResource())

class BallotPositionNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = BallotPositionName.objects.all()
        #resource_name = 'ballotpositionname'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
            "blocking": ALL,
        }
api.name.register(BallotPositionNameResource())

class DBTemplateTypeNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = DBTemplateTypeName.objects.all()
        #resource_name = 'dbtemplatetypename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(DBTemplateTypeNameResource())

class NomineePositionStateNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = NomineePositionStateName.objects.all()
        #resource_name = 'nomineepositionstatename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(NomineePositionStateNameResource())

class ReviewRequestStateNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = ReviewRequestStateName.objects.all()
        #resource_name = 'reviewrequeststatename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(ReviewRequestStateNameResource())

class ReviewTypeNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = ReviewTypeName.objects.all()
        #resource_name = 'reviewtypename'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(ReviewTypeNameResource())

class ReviewResultNameResource(ModelResource):
    class Meta:
        cache = SimpleCache()
        queryset = ReviewResultName.objects.all()
        #resource_name = 'reviewresultname'
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "desc": ALL,
            "used": ALL,
            "order": ALL,
        }
api.name.register(ReviewResultNameResource())

