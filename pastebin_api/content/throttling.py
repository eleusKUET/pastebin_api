from rest_framework.throttling import UserRateThrottle


class LimitedRateThrottle(UserRateThrottle):
    rate = '30/min'