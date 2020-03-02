from django.db import models

# Create your models here.
class Aircraft(models.Model):
    AIRCRAFT_TYPE_CHOICES = [
        ('FW', '固定翼'),
        ('MR', '多旋翼'),
        ('HE', '直升机'),
    ]

    aircraft_number = models.CharField(max_length=20, primary_key=True,
            verbose_name='飞机编号', help_text='20个字符以内')
    aircraft_type = models.CharField(max_length=2, choices=AIRCRAFT_TYPE_CHOICES,
            verbose_name='类型')
    production_date = models.DateField(verbose_name='制造日期')
    init_flight_hour = models.DecimalField(max_digits=7, decimal_places=2,
            verbose_name='飞行小时数初值', help_text='精度为0.01h')

    def __str__(self):
        return self.aircraft_number

    class Meta:
        verbose_name = verbose_name_plural = '飞行器'


class Duty(models.Model):
    name = models.CharField(max_length=20, verbose_name='职务名称', help_text='20字以内')
    description = models.CharField(max_length=200, verbose_name='职务描述',
            blank=True, help_text='200字以内')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '职务'


class Crew(models.Model):
    SEX_CHOICES = [
        ('F', '男性'),
        ('M', '女性'),
    ]

    employee_id = models.CharField(max_length=4, primary_key=True, verbose_name='工号',
            help_text='4位数字')
    name = models.CharField(max_length=20, verbose_name='姓名')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birthday = models.DateField(verbose_name='出生日期')
    joined_day = models.DateField(verbose_name='入职日期')
    duty = models.ManyToManyField(Duty)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '人员'


class Mission(models.Model):
    MISSION_TYPE_CHOICES = [
        ('1', '常规作业'),
        ('2', '维护'),
        ('3', '试验'),
        ('4', '其他'),
    ]
    WEATHER_TYPE_CHOICES = [
        ('1', '晴朗'),
        ('2', '多云'),
        ('3', '阴'),
        ('4', '雨天'),
        ('5', '雪天'),
        ('6', '其他'),
    ]
    
    mission_date = models.DateTimeField(verbose_name='任务日期')
    aircraft = models.ForeignKey(Aircraft, on_delete=models.DO_NOTHING)
    place = models.CharField(max_length=50, verbose_name='任务地点')
    mission_type = models.CharField(max_length=1, choices=MISSION_TYPE_CHOICES,
            verbose_name='任务类型')
    duration = models.DecimalField(max_digits=7, decimal_places=2,
            verbose_name='飞行时间', help_text='单位：h，精度：0.01')
    weather_type = models.CharField(max_length=1, choices=WEATHER_TYPE_CHOICES,
            verbose_name='天气类型')
    weather_description = models.CharField(max_length=100, verbose_name='天气描述',
            help_text='100字以内')
    mission_description = models.CharField(max_length=300, verbose_name='任务描述',
            help_text='300字以内')
    mission_situation = models.CharField(max_length=1000, verbose_name='任务实际状况',
            help_text='1000字以内')
    commander = models.ForeignKey(Crew, on_delete=models.DO_NOTHING)
    pilot = models.ManyToManyField(Crew, related_name='mission_pilot')
    gcs_operator = models.ManyToManyField(Crew, related_name='mission_gcs_op')
    groundservice = models.ManyToManyField(Crew, related_name='mission_gservice')
    maintenance = models.ManyToManyField(Crew, related_name='mission_mai')
    security = models.ManyToManyField(Crew, related_name='mission_sec')
    recorder = models.ManyToManyField(Crew, related_name='mission_rec')
    other_people = models.CharField(max_length=100, verbose_name='其他人员',
            blank=True, help_text='100字以内')
    data_file = models.FileField(verbose_name='飞行数据文件',
            upload_to='mission-data-files', help_text='上传飞行数据文件')

    def __str__(self):
        return str(self.mission_date)

    class Meta:
        verbose_name = verbose_name_plural = '飞行任务'
