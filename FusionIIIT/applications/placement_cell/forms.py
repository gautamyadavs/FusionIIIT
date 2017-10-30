from django import forms


class AddEducation(forms.Form):

    institute = forms.CharField(widget=forms.TextInput(attrs={'max_length': 250,
                                                              'class': 'field'}),
                                label="institute")
    degree = forms.CharField(widget=forms.TextInput(attrs={'max_length': 40,
                                                           'class': 'field'}),
                             label="degree")
    grade = forms.CharField(widget=forms.TextInput(attrs={'max_length': 10,
                                                          'class': 'form-control'}),
                            label="grade")
    stream = forms.CharField(widget=forms.TextInput(attrs={'max_length': 150,
                                                           'class': 'form-control'}),
                             label="stream")
    sdate = forms.DateField(label='sdate', widget=forms.widgets.DateInput())
    edate = forms.DateField(label='edate', widget=forms.widgets.DateInput())


class AddSkill(forms.Form):

    skill = forms.CharField(widget=forms.TextInput(attrs={'max_length': 30,
                                                          'class': 'field'}),
                            label="skill")
    skill_rating = forms.IntegerField(label="skill_rating")


class AddCourse(forms.Form):

    course_name = forms.CharField(widget=forms.TextInput(attrs={'max_length': 100,
                                                                'class': 'field'}),
                                  label="course_name")
    description = forms.CharField(widget=forms.TextInput(attrs={'max_length': 250,
                                                                'class': 'field'}),
                                  label="description")
    license_no = forms.IntegerField(label="license_no")
    sdate = forms.DateField(label='sdate', widget=forms.widgets.DateInput())
    edate = forms.DateField(label='edate', widget=forms.widgets.DateInput())


class AddExperience(forms.Form):

    title = forms.CharField(widget=forms.TextInput(attrs={'max_length': 100,
                                                          'class': 'field'}),
                            label="title")
    status = forms.CharField(widget=forms.TextInput(attrs={'max_length': 20,
                                                           'class': 'field'}),
                             label="status")
    description = forms.CharField(widget=forms.TextInput(attrs={'max_length': 500,
                                                                'class': 'form-control'}),
                                  label="description")
    company = forms.CharField(widget=forms.TextInput(attrs={'max_length': 200,
                                                            'class': 'form-control'}),
                              label="company")
    location = forms.CharField(widget=forms.TextInput(attrs={'max_length': 200,
                                                             'class': 'form-control'}),
                               label="location")
    sdate = forms.DateField(label='sdate', widget=forms.widgets.DateInput())
    edate = forms.DateField(label='edate', widget=forms.widgets.DateInput())


class AddProject(forms.Form):

    project_name = forms.CharField(widget=forms.TextInput(attrs={'max_length': 40,
                                                                 'class': 'field'}),
                                   label="title")
    project_status = forms.CharField(widget=forms.TextInput(attrs={'max_length': 20,
                                                                   'class': 'field'}),
                                     label="project_status")
    summary = forms.CharField(widget=forms.TextInput(attrs={'max_length': 500,
                                                            'class': 'form-control'}),
                              label="summary")
    project_link = forms.CharField(widget=forms.TextInput(attrs={'max_length': 200,
                                                                 'class': 'form-control'}),
                                   label="project_link")
    sdate = forms.DateField(label='sdate', widget=forms.widgets.DateInput())
    edate = forms.DateField(label='edate', widget=forms.widgets.DateInput())


class AddAchievement(forms.Form):

    achievement = forms.CharField(widget=forms.TextInput(attrs={'max_length': 100,
                                                                'class': 'field'}),
                                  label="achievement")
    achievement_type = forms.CharField(widget=forms.TextInput(attrs={'max_length': 20,
                                                                     'class': 'field'}),
                                       label="achievement_type")
    description = forms.CharField(widget=forms.TextInput(attrs={'max_length': 1000,
                                                                'class': 'form-control'}),
                                  label="description")
    issuer = forms.CharField(widget=forms.TextInput(attrs={'max_length': 200,
                                                                 'class': 'form-control'}),
                             label="issuer")
    date_earned = forms.DateField(label='date_earned', widget=forms.widgets.DateInput())


class AddPublication(forms.Form):

    publication_title = forms.CharField(widget=forms.TextInput(attrs={'max_length': 100,
                                                                      'class': 'field'}),
                                        label="publication_title")
    description = forms.CharField(widget=forms.TextInput(attrs={'max_length': 250,
                                                                'class': 'form-control'}),
                                  label="description")
    publisher = forms.CharField(widget=forms.TextInput(attrs={'max_length': 250,
                                                              'class': 'form-control'}),
                                label="publisher")
    publication_date = forms.DateField(label='publication_date', widget=forms.widgets.DateInput())


class AddPatent(forms.Form):

    patent_name = forms.CharField(widget=forms.TextInput(attrs={'max_length': 100,
                                                                'class': 'field'}),
                                  label="patent_name")
    description = forms.CharField(widget=forms.TextInput(attrs={'max_length': 250,
                                                                'class': 'form-control'}),
                                  label="description")
    patent_office = forms.CharField(widget=forms.TextInput(attrs={'max_length': 250,
                                                                  'class': 'form-control'}),
                                    label="patent_office")
    patent_date = forms.DateField(label='patent_date', widget=forms.widgets.DateInput())


class AddProfile(forms.Form):

    about_me = forms.CharField(widget=forms.TextInput(attrs={'max_length': 250,
                                                              'class': 'field'}),
                                label="about_me")
    age = forms.IntegerField(label="age")
    address = forms.CharField(widget=forms.TextInput(attrs={'max_length': 250,
                                                          'class': 'form-control'}),
                            label="address")
