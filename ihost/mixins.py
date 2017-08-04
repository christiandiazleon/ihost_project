class UserProfileDataMixin(object):
    def get_context_data(self, **kwargs):
        context = super(UserProfileDataMixin, self).get_context_data(**kwargs)
        # messages.info(self.request, 'hello http://example.com')
        user = self.request.user
        #context['userprofile'] = user.profile
        if user.is_authenticated():
            context['userprofile'] = user.profile
        return context
