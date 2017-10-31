from django import forms
from .models import Constants


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
                             label="stream", required=False)
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
                                  label="description", required=False)
    license_no = forms.CharField(widget=forms.TextInput(attrs={'max_length': 250,
                                                                'class': 'field'}),
                                 label="license_no", required=False)
    sdate = forms.DateField(label='sdate', widget=forms.widgets.DateInput())
    edate = forms.DateField(label='edate', widget=forms.widgets.DateInput())


class AddExperience(forms.Form):

    title = forms.CharField(widget=forms.TextInput(attrs={'max_length': 100,
                                                          'class': 'field'}),
                            label="title")
    status = forms.ChoiceField(choices = Constants.RESUME_TYPE, label="status",
                               widget=forms.Select())
    description = forms.CharField(widget=forms.TextInput(attrs={'max_length': 500,
                                                                'class': 'form-control'}),
                                  label="description", required=False)
    company = forms.CharField(widget=forms.TextInput(attrs={'max_length': 200,
                                                            'class': 'form-control'}),
                              label="company")
    location = forms.CharField(widget=forms.TextInput(attrs={'max_length': 200,
                                                             'class': 'form-control'}),
                               label="location")
    sdate = forms.DateField(label='sdate', widget=forms.widgets.DateInput())
    edate = forms.DateField(label='edate', widget=forms.widgets.DateInput())


class AddProject(forms.Form):

    project_name = forms.CharField(widget=forms.TextInput(attrs={'max_length': 50,
                                                                 'class': 'field'}),
                                   label="title")
    project_status = forms.ChoiceField(choices = Constants.RESUME_TYPE, label="project_status",
                               widget=forms.Select())
    summary = forms.CharField(widget=forms.TextInput(attrs={'max_length': 1000,
                                                            'class': 'form-control'}),
                              label="summary", required=False)
    project_link = forms.CharField(widget=forms.TextInput(attrs={'max_length': 200,
                                                                 'class': 'form-control'}),
                                   label="project_link", required=False)
    sdate = forms.DateField(label='sdate', widget=forms.widgets.DateInput())
    edate = forms.DateField(label='edate', widget=forms.widgets.DateInput())


class AddAchievement(forms.Form):

    achievement = forms.CharField(widget=forms.TextInput(attrs={'max_length': 100,
                                                                'class': 'field'}),
                                  label="achievement")
    achievement_type = forms.ChoiceField(choices = Constants.ACHIEVEMENT_TYPE,
                                         label="achievement_type", widget=forms.Select())
    description = forms.CharField(widget=forms.TextInput(attrs={'max_length': 1000,
                                                                'class': 'form-control'}),
                                  label="description", required=False)
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
                                  label="description", required=False)
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
                                  label="description", required=False)
    patent_office = forms.CharField(widget=forms.TextInput(attrs={'max_length': 250,
                                                                  'class': 'form-control'}),
                                    label="patent_office")
    patent_date = forms.DateField(label='patent_date', widget=forms.widgets.DateInput())


class AddProfile(forms.Form):

    about_me = forms.CharField(widget=forms.TextInput(attrs={'max_length': 250,
                                                              'class': 'field'}),
                                label="about_me", required=False)
    age = forms.IntegerField(label="age")
    address = forms.CharField(widget=forms.TextInput(attrs={'max_length': 250,
                                                          'class': 'form-control'}),
                            label="address")


class AddChairmanVisit(forms.Form):

    company_name = forms.CharField(widget=forms.TextInput(attrs={'max_length': 100,
                                                              'class': 'field'}),
                                label="company_name")
    location = forms.CharField(widget=forms.TextInput(attrs={'max_length': 100,
                                                           'class': 'field'}),
                             label="location")
    description = forms.CharField(widget=forms.TextInput(attrs={'max_length': 1000,
                                                          'class': 'form-control'}),
                            label="description")

    visiting_date = forms.DateField(label='visiting_date', widget=forms.widgets.DateInput())
