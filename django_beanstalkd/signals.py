from django.dispatch import Signal

beanstalk_job_started = Signal(providing_args=['name', 'arg'])
beanstalk_job_finished = Signal(providing_args=['name',])