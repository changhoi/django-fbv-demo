from django.shortcuts import render, redirect
from django.urls import reverse
from .words import eng, kor
# Create your views here.

def get_quiz(request):
    if request.method == 'GET':
        index = int(request.GET.get('index', 0));
        correct = int(request.GET.get('correct', 0));

        print(index, correct)
        action = ""
        if index == 4:
            action += reverse('result')

        context = {
            "quiz": eng[index], 
            "index": index, 
            "correct": correct, 
            "action": action
        }

        return render(request, 'words/index.html', context)
    
    if request.method == 'POST':
        index = int(request.POST.get('index'))
        before_correct = int(request.POST.get('correct'))
        answer = request.POST.get('answer')

        correct = before_correct
        next_url = 'quiz' if int(index) < 4 else 'result'
        # 연산 ? 참값 : 거짓값

        if answer == kor[index]:
            correct+=1
            
        return redirect(
            reverse(next_url) + 
            '?index={index}&correct={correct}'
            .format(index=index + 1, correct=correct)
        )
        
def get_result(request):
    if request.method == 'POST':
        correct = int(request.POST.get('correct'))
        index = int(request.POST.get('index'))
        answer = request.POST.get('answer')

        result = correct
        if answer == kor[index]:
            result += 1

        context = {
            "correct": result
        }
        return render(request, 'words/result.html', context)