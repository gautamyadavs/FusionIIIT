from cgi import escape
from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template
from xhtml2pdf import pisa

from applications.academic_information.models import Student
from applications.globals.models import ExtraInfo

from .forms import (AddEducation, AddProfile, AddSkill, AddCourse, AddAchievement, AddProject,
                    AddPublication, AddPatent, AddExperience)
from .models import (Achievement, Course, Education, Experience, Has, Project, Publication, Skill,
                     StudentPlacement, Patent)


@login_required
def placement(request, username):
    user = get_object_or_404(User, Q(username=username))
    profile = get_object_or_404(ExtraInfo, Q(user=user))
    if profile.user_type == 'student':
        context = {'user': user, 'profile': profile}
        return render(request, "placementModule/placement.html", context)
    elif profile.designation == 'placement officer':
        context = {'user': user, 'profile': profile}
        return render(request, "placementModule/placement.html", context)
    elif profile.designation == 'placement chairman':
        context = {'user': user, 'profile': profile}
        return render(request, "placementModule/placement.html", context)


@login_required
def profile(request, username):
    user = get_object_or_404(User, Q(username=username))
    profile = get_object_or_404(ExtraInfo, Q(user=user))
    if profile.user_type == 'student':
        student = get_object_or_404(Student, Q(id=profile.id))
        if request.method == 'POST':
            if 'educationsubmit' in request.POST:
                form = AddEducation(request.POST)
                if form.is_valid():
                    institute = form.cleaned_data['institute']
                    degree = form.cleaned_data['degree']
                    grade = form.cleaned_data['grade']
                    stream = form.cleaned_data['stream']
                    sdate = form.cleaned_data['sdate']
                    edate = form.cleaned_data['edate']
                    education_obj = Education.objects.create(unique_id=student, degree=degree,
                                                             grade=grade, institute=institute,
                                                             stream=stream, sdate=sdate, edate=edate)
                    education_obj.save()
            if 'profilesubmit' in request.POST:
                form = AddProfile(request.POST)
                if form.is_valid():
                    about_me = form.cleaned_data['about_me']
                    age = form.cleaned_data['age']
                    address = form.cleaned_data['address']
                    extrainfo_obj = ExtraInfo.objects.get(user=user)
                    extrainfo_obj.about_me = about_me
                    extrainfo_obj.age = age
                    extrainfo_obj.address = address
                    extrainfo_obj.save()
            if 'skillsubmit' in request.POST:
                form = AddSkill(request.POST)
                if form.is_valid():
                    skill = form.cleaned_data['skill']
                    skill_rating = form.cleaned_data['skill_rating']
                    has_obj = Has.objects.create(unique_id=student,
                                                 skill_id=Skill.objects.get(skill=skill),
                                                 skill_rating = skill_rating)
                    has_obj.save()
            if 'achievementsubmit' in request.POST:
                form = AddAchievement(request.POST)
                if form.is_valid():
                    achievement = form.cleaned_data['achievement']
                    achievement_type = form.cleaned_data['achievement_type']
                    description = form.cleaned_data['description']
                    issuer = form.cleaned_data['issuer']
                    date_earned = form.cleaned_data['date_earned']
                    achievement_obj = Achievement.objects.create(unique_id=student,
                                                                 achievement=achievement,
                                                                 achievement_type=achievement_type,
                                                                 description=description,
                                                                 issuer=issuer,
                                                                 date_earned=date_earned)
                    achievement_obj.save()
            if 'publicationsubmit' in request.POST:
                form = AddPublication(request.POST)
                if form.is_valid():
                    publication_title = form.cleaned_data['publication_title']
                    description = form.cleaned_data['description']
                    publisher = form.cleaned_data['publisher']
                    publication_date = form.cleaned_data['publication_date']
                    publication_obj = Publication.objects.create(unique_id=student,
                                                                 publication_title=
                                                                 publication_title,
                                                                 publisher=publisher,
                                                                 description=description,
                                                                 publication_date=publication_date)
                    publication_obj.save()
            if 'patentsubmit' in request.POST:
                form = AddPatent(request.POST)
                if form.is_valid():
                    patent_name = form.cleaned_data['patent_name']
                    description = form.cleaned_data['description']
                    patent_office = form.cleaned_data['patent_office']
                    patent_date = form.cleaned_data['patent_date']
                    patent_obj = Patent.objects.create(unique_id=student, patent_name=patent_name,
                                                       patent_office=patent_office,
                                                       description=description,
                                                       patent_date=patent_date)
                    patent_obj.save()
            if 'coursesubmit' in request.POST:
                form = AddCourse(request.POST)
                if form.is_valid():
                    course_name = form.cleaned_data['course_name']
                    description = form.cleaned_data['description']
                    license_no = form.cleaned_data['license_no']
                    sdate = form.cleaned_data['sdate']
                    edate = form.cleaned_data['edate']
                    course_obj = Course.objects.create(unique_id=student, course_name=course_name,
                                                       license_no=license_no,
                                                       description=description,
                                                       sdate=sdate, edate=edate)
                    course_obj.save()
            if 'projectsubmit' in request.POST:
                form = AddProject(request.POST)
                if form.is_valid():
                    project_name = form.cleaned_data['project_name']
                    project_status = form.cleaned_data['project_status']
                    summary = form.cleaned_data['summary']
                    project_link = form.cleaned_data['project_link']
                    sdate = form.cleaned_data['sdate']
                    edate = form.cleaned_data['edate']
                    project_obj = Project.objects.create(unique_id=student, summary=summary,
                                                         project_name=project_name,
                                                         project_status=project_status,
                                                         project_link=project_link,
                                                         sdate=sdate, edate=edate)
                    project_obj.save()
            if 'experiencesubmit' in request.POST:
                form = AddExperience(request.POST)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    status = form.cleaned_data['status']
                    company = form.cleaned_data['company']
                    location = form.cleaned_data['location']
                    description = form.cleaned_data['description']
                    sdate = form.cleaned_data['sdate']
                    edate = form.cleaned_data['edate']
                    experience_obj = Experience.objects.create(unique_id=student, title=title,
                                                         company=company, location=location,
                                                         status=status, description=description,
                                                         sdate=sdate, edate=edate)
                    experience_obj.save()
        form = AddEducation(initial={})
        form1 = AddProfile(initial={})
        form2 = AddSkill(initial={})
        form3 = AddCourse(initial={})
        form4 = AddAchievement(initial={})
        form5 = AddPublication(initial={})
        form6 = AddProject(initial={})
        form7 = AddPatent(initial={})
        form8 = AddExperience(initial={})
        studentplacement = get_object_or_404(StudentPlacement, Q(unique_id=student))
        skills = Has.objects.filter(Q(unique_id=student))
        education = Education.objects.filter(Q(unique_id=student))
        course = Course.objects.filter(Q(unique_id=student))
        experience = Experience.objects.filter(Q(unique_id=student))
        project = Project.objects.filter(Q(unique_id=student))
        achievement = Achievement.objects.filter(Q(unique_id=student))
        publication = Publication.objects.filter(Q(unique_id=student))
        patent = Patent.objects.filter(Q(unique_id=student))
        context = {'user': user, 'profile': profile, 'student': studentplacement, 'skills': skills,
                   'educations': education, 'courses': course, 'experiences': experience,
                   'projects': project, 'achievements': achievement, 'publications': publication,
                   'patent': patent, 'form': form, 'form1': form1, 'form2': form2, 'form3': form3,
                   'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8}
        return render(request, "placementModule/placement.html", context)


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


def cv(request, username):
    # Retrieve data or whatever you need
    user = get_object_or_404(User, Q(username=username))
    profile = get_object_or_404(ExtraInfo, Q(user=user))
    student = get_object_or_404(Student, Q(id=profile.id))
    studentplacement = get_object_or_404(StudentPlacement, Q(unique_id=student))
    skills = Has.objects.filter(Q(unique_id=student))
    education = Education.objects.filter(Q(unique_id=student))
    course = Course.objects.filter(Q(unique_id=student))
    experience = Experience.objects.filter(Q(unique_id=student))
    project = Project.objects.filter(Q(unique_id=student))
    achievement = Achievement.objects.filter(Q(unique_id=student))
    publication = Publication.objects.filter(Q(unique_id=student))
    return render_to_pdf('placementModule/cv.html', {'pagesize': 'A4', 'user': user,
                                                     'profile': profile, 'projects': project,
                                                     'student': studentplacement,
                                                     'skills': skills, 'educations': education,
                                                     'courses': course, 'experiences': experience,
                                                     'achievements': achievement,
                                                     'publications': publication})
