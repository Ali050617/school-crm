from django.shortcuts import render, get_object_or_404, redirect
from .models import Group


def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/groups-list.html', ctx)


def group_create(request):
    if request.method == 'POST':
        class_leader = request.POST.get('class_leader')
        group_name = request.POST.get('group_name')
        if class_leader and group_name:
            Group.objects.create(
                class_leader=class_leader,
                group_name=group_name
            )
            return redirect('groups:groups_list')
    return render(request, 'groups-add.html')


def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        class_leader = request.POST.get('class_leader')
        group_name = request.POST.get('group_name')
        if class_leader and group_name:
            group.class_leader = class_leader
            group.group_name = group_name
            group.save()
            return redirect(group.get_detail_url())
    ctx = {'group': group}
    return render(request, 'groups/group-add.html',ctx)


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group': group}
    return render(request, 'groups/group-detail.html', ctx)


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('groups:group_list')

