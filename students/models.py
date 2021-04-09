from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Profile(models.Model):
    btech = '01'
    mtech = '41'
    phd = '61'
    msc = '21'
    msr = '43'
    ma = '22'
    bdes = '02'
    mdes = '42'
    error = '00'

    program_values = (
        (btech, 'BTech'),
        (mtech, 'MTech'),
        (phd, 'PhD'),
        (msc, 'MSc'),
        (msr, 'MS-R'),
        (ma, 'MA'),
        (bdes, 'BDes'),
        (mdes, 'MDes'),
        (error, 'Error')
    )

    cse = '01'
    ece = '02'
    me = '03'
    ce = '04'
    dd = '05'
    bsbe = '06'
    cl = '07'
    cst = '22'
    eee = '08'
    ma = '23'
    ph = '21'
    rt = '54'
    hss = '41'
    enc = '51'
    env = '52'
    nt = '53'
    lst = '55'

    department_values = (
        (cse, 'Computer Science & Engineering'),
        (ece, 'Electronics & Communication Engineering'),
        (me, 'Mechanical Engineering'),
        (ce, 'Civil Engineering'),
        (dd, 'Design'),
        (bsbe, 'Biosciences & Bioengineering'),
        (cl, 'Chemical Engineering'),
        (cst, 'Chemical Science & Technology'),
        (eee, 'Electronics & Electrical Engineering'),
        (ma, 'Mathematics & Computing'),
        (ph, 'Engineering Physics'),
        (rt, 'Rural Technology'),
        (hss, 'Humanities & Social Sciences'),
        (enc, 'Centre for Energy'),
        (env, 'Centre for Environment'),
        (nt, 'Centre for Nanotechnology'),
        (lst, 'Centre for Linguistic Science & Technology'),
        (error, 'Error')
    )
    profile_pic = models.ImageField(upload_to='profile_pics/', default='profile_pics/no-profile-pic.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    program = models.CharField(max_length=2, choices=program_values)
    department = models.CharField(max_length=3, choices=department_values)
    bio = models.TextField(max_length=500)
    graduating = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class Testimonial(models.Model):
    favourite = models.BooleanField(default=False)
    given_by = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, related_name='given_by')
    content = models.TextField(max_length = 400)
    given_to = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, related_name='given_to')

    def __str__(self):
        return self.given_by.full_name+" -> "+self.given_to.full_name


class PollQuestion (models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class PollAnswer (models.Model):
    answer = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, related_name='voted_to')
    question = models.ForeignKey(PollQuestion, null=True, on_delete=models.SET_NULL)
    voted_by = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, related_name='voted_by')

    def __str__(self):
        if self.question:
            return self.question.question+" "+self.voted_by.full_name+" -> "+self.answer.full_name
        else:
            return "Deleted Poll "+self.voted_by.full_name+" -> "+self.answer.full_name


class ProfileQuestion (models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class ProfileAnswers (models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    question = models.ForeignKey(ProfileQuestion, null=True, on_delete=models.SET_NULL)
    answer = models.TextField(max_length = 300)

    def __str__(self):
        if self.question:
            return self.question.question+" "+self.profile.full_name
        else:
            return "Deleted Profile Question "+self.profile.full_name


class Announcement(models.Model):
    content = models.TextField(max_length=150)
    pub_date = models.DateTimeField(default=timezone.now)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.content

def get_cnt_default():
    return list([10,10,10,10,10,10,10,10,10,10])

class Leaderboard(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    profile_0 = models.ForeignKey(Profile,null=True,related_name='profile_0',on_delete=models.SET_NULL)
    profile_1 = models.ForeignKey(Profile,null=True,related_name='profile_1',on_delete=models.SET_NULL)
    profile_2 = models.ForeignKey(Profile,null=True,related_name='profile_2',on_delete=models.SET_NULL)
    profile_3 = models.ForeignKey(Profile,null=True,related_name='profile_3',on_delete=models.SET_NULL)
    profile_4 = models.ForeignKey(Profile,null=True,related_name='profile_4',on_delete=models.SET_NULL)
    profile_5 = models.ForeignKey(Profile,null=True,related_name='profile_5',on_delete=models.SET_NULL)
    profile_6 = models.ForeignKey(Profile,null=True,related_name='profile_6',on_delete=models.SET_NULL)
    profile_7 = models.ForeignKey(Profile,null=True,related_name='profile_7',on_delete=models.SET_NULL)
    profile_8 = models.ForeignKey(Profile,null=True,related_name='profile_8',on_delete=models.SET_NULL)
    profile_9 = models.ForeignKey(Profile,null=True,related_name='profile_9',on_delete=models.SET_NULL)
    cnt_0 = models.IntegerField(default=0)
    cnt_1 = models.IntegerField(default=0)
    cnt_2 = models.IntegerField(default=0)
    cnt_3 = models.IntegerField(default=0)
    cnt_4 = models.IntegerField(default=0)
    cnt_5 = models.IntegerField(default=0)
    cnt_6 = models.IntegerField(default=0)
    cnt_7 = models.IntegerField(default=0)
    cnt_8 = models.IntegerField(default=0)
    cnt_9 = models.IntegerField(default=0)