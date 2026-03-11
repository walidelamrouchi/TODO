from  .models import Task
from django.utils import timezone
from .forms import TaskForm
def sidebar_data(request):
    if not request.user.is_authenticated:
        return {}
    return {
    'inbox_count': Task.objects.filter(
            user=request.user,
            is_done=False
        ).count(),
    'today_count': Task.objects.filter(
        user=request.user,
        due_date__date= timezone.now().date(),
        is_done = False
        ).count(),
    'add_task_form': TaskForm(),
    }