from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def test_response(request):
    return HttpResponse("OCW4IQ1")

def toppage(request):
    d = {'default_input_value' : '授業名'}
    return render(request,'topPage.html',d)

def search_and_result(request):

    result_head = {'quarter': 'クォーター', 'lecname': '講義名', 'teacher': '教員名'}

    content = [('1Q', '講義名1', '教員名3'), ('2Q', '講義名2', '教員名2'), ('1Q', '講義名3', '教員名3')]
    result_content = []
    for item in content:
        result_content.append({'quarter': item[0], 'lecname': item[1], 'teacher': item[2]})

    d = {
        'result_head': result_head,
        'result_content': result_content


    }
    return render(request, 'searchAndResult.html', d)
